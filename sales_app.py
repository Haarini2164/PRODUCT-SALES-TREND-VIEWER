import pandas as pd
import plotly.express as px
import streamlit as st
from prophet import Prophet

st.set_page_config(
    page_title=" Product Sales Trend Viewer",
    page_icon=":bar_chart:",
    layout="wide"
)

# ================== APP HEADER WITH STYLING ==================
st.markdown("""
<style>
.main-title {font-family: 'Arial Black', sans-serif; color:#087EA4; font-size:2.4em;}
.subtitle {color:#32337B; font-size:1.1em; font-weight:bold;}
.sidebar-title {color:#09AB5D; font-size:1.1em;}
div.stButton > button {background-color:#09AB5D; color:white; font-weight:bold;}
div.stButton > button:hover {background-color:#087EA4;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title"> Product Sales Trend Viewer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Easily upload any CSV, map columns, and explore product sales with instant charts & forecasts!</div>', unsafe_allow_html=True)
st.write("")

# ================== SIDEBAR ==================
st.sidebar.markdown('<div class="sidebar-title">Step 1: Upload and Map Columns</div>', unsafe_allow_html=True)

uploaded_file = st.sidebar.file_uploader("Choose your sales CSV", type=['csv'])

# ---------- DATA ACQUISITION ------------
if uploaded_file:
    df_sample = pd.read_csv(uploaded_file, nrows=0)
    columns = df_sample.columns.tolist()

    st.sidebar.write("Detected columns:", columns)

    col_product = st.sidebar.selectbox(" Product column", columns, index=0)
    col_sales = st.sidebar.selectbox(" Sales/Amount column", columns, index=1 if len(columns)>1 else 0)
    col_date = st.sidebar.selectbox(" Date column", columns, index=2 if len(columns)>2 else 0)

    optional_cols = columns + ["None"]
    col_region = None
    col_quantity = None
    col_customer = None

    if st.sidebar.checkbox("Map Region column (optional)"):
        col_region = st.sidebar.selectbox("Region column", optional_cols, index=len(optional_cols)-1)
        if col_region == "None":
            col_region = None

    if st.sidebar.checkbox("Map Quantity Sold column (optional)"):
        col_quantity = st.sidebar.selectbox("Quantity Sold column", optional_cols, index=len(optional_cols)-1)
        if col_quantity == "None":
            col_quantity = None

    if st.sidebar.checkbox("Map Customer Type column (optional)"):
        col_customer = st.sidebar.selectbox("Customer Type column", optional_cols, index=len(optional_cols)-1)
        if col_customer == "None":
            col_customer = None

    analyze_clicked = st.sidebar.button(" Load and Analyze Data", use_container_width=True)

    if analyze_clicked:
        with st.spinner("Processing CSV and generating dashboard..."):
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file)

            rename_map = {
                col_product: 'product',
                col_sales: 'sales',
                col_date: 'date'
            }

            if col_region:
                rename_map[col_region] = 'region'
            if col_quantity:
                rename_map[col_quantity] = 'quantity_sold'
            if col_customer:
                rename_map[col_customer] = 'customer_type'

            df = df.rename(columns=rename_map)

            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df = df.dropna(subset=['date'])

            df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
            df = df.dropna(subset=['sales'])

            if 'region' in df.columns:
                df['region'] = df['region'].astype(str)

            if 'quantity_sold' in df.columns:
                df['quantity_sold'] = pd.to_numeric(df['quantity_sold'], errors='coerce')

            if 'customer_type' in df.columns:
                df['customer_type'] = df['customer_type'].astype(str)

            df['year'] = df['date'].dt.year
            df['month'] = df['date'].dt.month_name()

else:
    # --------- DEFAULT CSV ---------
    DATA_PATH = "sales_data.csv"
    st.sidebar.write("No file uploaded. Using default CSV.")

    @st.cache_data
    def load_data():
        df = pd.read_csv(DATA_PATH)
        df.columns = df.columns.str.strip().str.lower()

        df = df.rename(columns={
            'sale_date': 'date',
            'order_date': 'date',
            'sales_amount': 'sales',
            'sales_value': 'sales',
            'product_category': 'product',
            'product_name': 'product'
        })

        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])

        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month_name()

        return df

    try:
        df = load_data()
    except Exception as e:
        st.error(f" Error loading file: {e}")
        st.stop()

# ================== DASHBOARD ==================
if (uploaded_file and analyze_clicked) or not uploaded_file:

    st.sidebar.markdown('<div class="sidebar-title">Step 2: Filter Options</div>', unsafe_allow_html=True)

    product_list = sorted(df['product'].dropna().unique())
    region_list = ['All'] + sorted(df['region'].dropna().unique()) if 'region' in df.columns else ['All']

    selected_products = st.sidebar.multiselect("Select Product(s)", product_list, default=product_list[:1])
    selected_region = st.sidebar.selectbox("Select Region", region_list)

    filtered_df = df[df['product'].isin(selected_products)]

    if selected_region != 'All' and 'region' in df.columns:
        filtered_df = filtered_df[filtered_df['region'] == selected_region]

    if filtered_df.empty:
        st.warning("No sales data available for your filter selection.")
        st.stop()

    st.markdown("---")
    st.markdown('<span class="subtitle">Key Performance Indicators</span>', unsafe_allow_html=True)

    total_sales = filtered_df['sales'].sum()

    monthly_sales_mean = filtered_df.groupby(
        filtered_df['date'].dt.to_period('M')
    )['sales'].sum().mean()

    best_month = filtered_df.groupby(
        filtered_df['date'].dt.month_name()
    )['sales'].sum().idxmax()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"{total_sales:,.0f}")
    col2.metric("Avg Sales/Month", f"{monthly_sales_mean:,.0f}")
    col3.metric("Best Month", best_month)

    st.markdown("---")
    st.subheader(" Monthly Sales Trend & Forecast")

    monthly_sales = filtered_df.groupby(
        filtered_df['date'].dt.to_period('M')
    )['sales'].sum().reset_index()

    monthly_sales['date'] = monthly_sales['date'].dt.to_timestamp()

    fig1 = px.line(monthly_sales, x='date', y='sales', markers=True, title="Historic Monthly Sales")
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("**Sales Forecast for Next 6 Months**")

    prophet_df = monthly_sales.rename(columns={'date': 'ds', 'sales': 'y'})

    if prophet_df.dropna().shape[0] < 2:
        st.warning("Not enough data for forecasting.")
    else:
        m = Prophet(yearly_seasonality=True)
        m.fit(prophet_df)

        future = m.make_future_dataframe(periods=6, freq='M')
        forecast = m.predict(future)

        fig2 = px.line(forecast, x='ds', y='yhat', title="Forecasted Sales")
        fig2.add_scatter(x=prophet_df['ds'], y=prophet_df['y'], mode='markers', name='Historical')

        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")
    st.subheader(" Top 5 Products by Total Sales")

    top_products = df.groupby('product')['sales'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_products)

    if 'region' in df.columns:
        st.markdown("---")
        st.subheader(" Region-wise Sales Distribution")

        region_sales = df.groupby('region')['sales'].sum().reset_index()
        fig3 = px.pie(region_sales, names='region', values='sales')

        st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")
    st.subheader(" Filtered Data Summary")

    show_cols = [col for col in ['date', 'region', 'product', 'sales', 'quantity_sold', 'customer_type'] if col in df.columns]

    st.dataframe(filtered_df[show_cols].sort_values('date', ascending=False))

    csv = filtered_df[show_cols].to_csv(index=False).encode('utf-8')

    st.download_button(" Download CSV", csv, "filtered_sales_data.csv", "text/csv")

else:
    st.info("Upload a CSV and click 'Load and Analyze Data'")