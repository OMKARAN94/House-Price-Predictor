import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="📊 Smart Data Analyzer",
    page_icon="📈",
    layout="wide"
)

# --------------- Custom CSS (optional) ---------------
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main {
        background-color: #111827;
        padding: 20px;
        border-radius: 15px;
    }
    h1, h2, h3 {
        color: #22d3ee;
    }
    </style>
""", unsafe_allow_html=True)

# --------------- Header ----------------
st.title("📊 Smart Data Analyzer")
st.write("Upload your **Excel/CSV file** and automatically clean and visualize your data.")

st.markdown("---")

# --------------- Step 1: Upload File ----------------
st.header("Step 1️⃣ : Upload Your Data File")

uploaded_file = st.file_uploader(
    "Upload an Excel (.xlsx, .xls) or CSV file",
    type=["xlsx", "xls", "csv"]
)

if uploaded_file is not None:
    file_name = uploaded_file.name

    # Detect file type and read
    try:
        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"❌ Error while reading file: {e}")
        st.stop()

    st.success(f"✅ File uploaded successfully: **{file_name}**")
    
    st.subheader("🔍 Preview of Data")
    st.write("First 5 rows of your dataset:")
    st.dataframe(df.head())

    st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")

    # Make a copy to clean
    df_clean = df.copy()

    st.markdown("---")

    # --------------- Step 2: Data Info ----------------
    st.header("Step 2️⃣ : Dataset Information")

    with st.expander("📌 Basic Information", expanded=True):
        st.write("**Column Types:**")
        st.write(df_clean.dtypes)

        st.write("**Summary Statistics (Numeric Columns):**")
        st.write(df_clean.describe())

    with st.expander("❗ Missing Values & Duplicates", expanded=True):
        st.subheader("Missing Values per Column")
        missing = df_clean.isnull().sum()
        st.write(missing)

        st.subheader("Duplicates")
        st.write(f"Total duplicate rows: **{df_clean.duplicated().sum()}**")

    st.markdown("---")

    # --------------- Step 3: Data Cleaning ----------------
    st.header("Step 3️⃣ : Data Cleaning Options")

    # --- Remove duplicates ---
    if st.checkbox("🧹 Remove duplicate rows"):
        before = df_clean.shape[0]
        df_clean = df_clean.drop_duplicates()
        after = df_clean.shape[0]
        st.success(f"Removed {before - after} duplicate rows. New shape: {df_clean.shape}")

    # --- Handle missing values ---
    st.subheader("🩹 Handle Missing Values")

    numeric_cols = df_clean.select_dtypes(include=np.number).columns.tolist()
    cat_cols = df_clean.select_dtypes(exclude=np.number).columns.tolist()

    st.write("**Numeric columns:**", numeric_cols)
    st.write("**Categorical columns:**", cat_cols)

    # Strategy for numeric columns
    num_strategy = st.selectbox(
        "Select strategy for numeric columns with missing values",
        ["Do nothing", "Fill with Mean", "Fill with Median", "Drop rows with any missing values"]
    )

    # Strategy for categorical columns
    cat_strategy = st.selectbox(
        "Select strategy for categorical columns with missing values",
        ["Do nothing", "Fill with Mode", "Drop rows with any missing values (same as above)"]
    )

    if st.button("🚀 Apply Cleaning"):
        # Numeric
        if num_strategy == "Fill with Mean":
            for col in numeric_cols:
                df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
        elif num_strategy == "Fill with Median":
            for col in numeric_cols:
                df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        elif num_strategy == "Drop rows with any missing values":
            df_clean = df_clean.dropna()

        # Categorical
        if cat_strategy == "Fill with Mode":
            for col in cat_cols:
                if df_clean[col].isnull().sum() > 0:
                    df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

        st.success("✅ Data cleaning applied successfully!")
        st.write("New shape after cleaning:", df_clean.shape)

    st.markdown("---")

    # --------------- Step 4: Visualizations ----------------
    st.header("Step 4️⃣ : Visualizations")

    tab1, tab2, tab3 = st.tabs(["📊 Pie Chart", "📉 Bar/Histogram", "📈 Correlation Heatmap"])

    # --- Pie Chart (Categorical) ---
    with tab1:
        st.subheader("📊 Pie Chart for Categorical Column")
        if len(cat_cols) > 0:
            cat_col = st.selectbox("Select a categorical column", cat_cols, key="pie_cat")
            pie_data = df_clean[cat_col].value_counts().reset_index()
            pie_data.columns = [cat_col, "Count"]

            fig = px.pie(
                pie_data,
                names=cat_col,
                values="Count",
                title=f"Distribution of {cat_col}"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No categorical columns available for pie chart.")

    # --- Bar / Histogram (Numeric) ---
    with tab2:
        st.subheader("📉 Bar Chart / Histogram")
        if len(numeric_cols) > 0:
            num_col = st.selectbox("Select a numeric column", numeric_cols, key="num_col")

            chart_type = st.radio("Select chart type", ["Histogram", "Bar (by Category)"])

            if chart_type == "Histogram":
                fig, ax = plt.subplots()
                ax.hist(df_clean[num_col].dropna(), bins=20)
                ax.set_title(f"Histogram of {num_col}")
                ax.set_xlabel(num_col)
                ax.set_ylabel("Frequency")
                st.pyplot(fig)

            else:
                if len(cat_cols) == 0:
                    st.warning("No categorical columns to group by for bar chart.")
                else:
                    group_col = st.selectbox("Group by categorical column", cat_cols)
                    grouped = df_clean.groupby(group_col)[num_col].mean().reset_index()

                    fig = px.bar(
                        grouped,
                        x=group_col,
                        y=num_col,
                        title=f"Average {num_col} by {group_col}"
                    )
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No numeric columns available for visualization.")

    # --- Correlation Heatmap ---
    with tab3:
        st.subheader("📈 Correlation Heatmap (Numeric Columns)")
        if len(numeric_cols) > 1:
            corr = df_clean[numeric_cols].corr()

            fig = px.imshow(
                corr,
                text_auto=True,
                title="Correlation Heatmap"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Not enough numeric columns for correlation heatmap.")

    st.markdown("---")

    # --------------- Step 5: Download Cleaned Data ----------------
    st.header("Step 5️⃣ : Download Cleaned Data")

    csv_data = df_clean.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Cleaned Data as CSV",
        data=csv_data,
        file_name="cleaned_data_output.csv",
        mime="text/csv"
    )

    st.success("🎉 Your data analysis and cleaning is complete!")

else:
    st.info("👆 Please upload a file to start analysis.")
