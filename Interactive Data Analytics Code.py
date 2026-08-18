import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Data Analytics Studio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL BLUE + RED THEME
# ============================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN APPLICATION
       ===================================================== */

    .stApp {
        background: #f4f7fb;
        color: #172033;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* =====================================================
       HEADER
       ===================================================== */

    .main-title {
        text-align: center;
        font-size: 44px;
        font-weight: 800;

        background: linear-gradient(
            90deg,
            #0b5ed7,
            #174ea6,
            #d62828
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #53657d;
        font-size: 17px;
        margin-bottom: 25px;
    }


    /* =====================================================
       HEADINGS
       ===================================================== */

    h1, h2, h3 {
        color: #14213d !important;
    }


    /* =====================================================
       KPI CARDS
       ===================================================== */

    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #d9e2ef;
        border-left: 5px solid #0b5ed7;
        border-radius: 14px;
        padding: 18px;

        box-shadow:
            0 5px 18px rgba(20, 50, 90, 0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #61738a !important;
    }

    div[data-testid="stMetricValue"] {
        color: #14213d !important;
        font-weight: 750;
    }


    /* =====================================================
       FILE UPLOADER
       ===================================================== */

    div[data-testid="stFileUploader"] {
        background: #ffffff;
        border: 2px dashed #3b82f6;
        border-radius: 14px;
        padding: 15px;

        box-shadow:
            0 4px 15px rgba(30, 90, 160, 0.08);
    }


    /* =====================================================
       BUTTONS
       ===================================================== */

    .stButton > button,
    .stDownloadButton > button {
        background: #0b5ed7;
        color: #ffffff;
        border: none;
        border-radius: 9px;

        font-weight: 700;
        padding: 10px 20px;

        transition: all 0.2s ease;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: #d62828;
        color: #ffffff;

        transform: translateY(-1px);

        box-shadow:
            0 5px 15px rgba(214, 40, 40, 0.25);
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background: #102a43;
        border-right: 1px solid #d9e2ef;
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }


    /* =====================================================
       DATA EDITOR
       ===================================================== */

    div[data-testid="stDataEditor"] {
        background: #ffffff;
        border: 1px solid #d9e2ef;
        border-radius: 12px;

        box-shadow:
            0 5px 18px rgba(20, 50, 90, 0.08);

        overflow: hidden;
    }


    /* =====================================================
       ALERTS
       ===================================================== */

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {
        text-align: center;
        color: #718096;

        margin-top: 40px;
        padding: 20px;
    }


    /* =====================================================
       VALIDATION BADGES
       ===================================================== */

    .good-badge {
        background: #e8f5e9;
        color: #137333;
        padding: 8px 14px;
        border-radius: 8px;
        font-weight: 700;
    }

    .warning-badge {
        background: #fff4e5;
        color: #b45309;
        padding: 8px 14px;
        border-radius: 8px;
        font-weight: 700;
    }

    .danger-badge {
        background: #fdecec;
        color: #c62828;
        padding: 8px 14px;
        border-radius: 8px;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 Data Analytics Studio</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Validate • Clean • Analyze • Visualize • Export'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Control Panel")

    st.write("Manage your dataset")

    st.divider()

    st.subheader("📁 Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    st.divider()

    st.caption(
        "Supported format: CSV"
    )


# ============================================================
# HOME SCREEN
# ============================================================

if uploaded_file is None:

    st.info(
        "👈 Upload a CSV file from the sidebar to begin."
    )

    st.markdown(
        """
        ### 🚀 Data Analytics Platform

        **🛡️ Data Quality**
        - Missing value detection
        - Duplicate detection
        - Negative value detection
        - Outlier detection
        - Empty column detection

        **✏️ Data Cleaning**
        - Edit cells
        - Add rows
        - Delete rows
        - Reset changes

        **📊 Analytics**
        - KPI dashboard
        - Interactive charts
        - Statistics
        - Correlation analysis

        **💡 Intelligence**
        - Automatic insights
        - Data quality score
        - Validation report

        **💾 Export**
        - Download cleaned data
        - Download filtered data
        """
    )

    st.stop()


# ============================================================
# LOAD DATASET
# ============================================================

try:

    df = pd.read_csv(uploaded_file)

except Exception as error:

    st.error(
        f"❌ Could not read this CSV file.\n\n{error}"
    )

    st.stop()


# ============================================================
# BASIC VALIDATION
# ============================================================

if df.empty:

    st.error(
        "❌ The uploaded dataset is empty."
    )

    st.stop()


if df.shape[1] == 0:

    st.error(
        "❌ No columns were found in the dataset."
    )

    st.stop()


# ============================================================
# SESSION STATE
# ============================================================

if "working_df" not in st.session_state:

    st.session_state.working_df = df.copy()


if "source_name" not in st.session_state:

    st.session_state.source_name = uploaded_file.name


# New uploaded file detection

if st.session_state.source_name != uploaded_file.name:

    st.session_state.working_df = df.copy()

    st.session_state.source_name = uploaded_file.name


working_df = st.session_state.working_df.copy()


# ============================================================
# RESET BUTTON
# ============================================================

reset_col, info_col = st.columns([1, 4])

with reset_col:

    if st.button("🔄 Reset Changes"):

        st.session_state.working_df = df.copy()

        st.rerun()

with info_col:

    st.caption(
        "Reset restores the original uploaded dataset."
    )


# ============================================================
# DATA QUALITY ENGINE
# ============================================================

def calculate_quality(dataframe):

    rows = dataframe.shape[0]
    columns = dataframe.shape[1]

    total_cells = rows * columns

    missing = int(
        dataframe.isnull().sum().sum()
    )

    duplicates = int(
        dataframe.duplicated().sum()
    )

    empty_columns = int(
        dataframe.isna().all().sum()
    )

    if total_cells > 0:

        missing_score = (
            missing / total_cells
        ) * 100

    else:

        missing_score = 100

    duplicate_score = (
        (duplicates / rows) * 100
        if rows > 0
        else 0
    )

    quality = (
        100
        - missing_score * 0.6
        - duplicate_score * 0.4
    )

    quality = max(
        0,
        min(100, quality)
    )

    return {
        "rows": rows,
        "columns": columns,
        "missing": missing,
        "duplicates": duplicates,
        "empty_columns": empty_columns,
        "quality": quality
    }


quality = calculate_quality(
    working_df
)


# ============================================================
# QUALITY STATUS
# ============================================================

if quality["quality"] >= 95:

    st.success(
        f"🟢 Excellent Data Quality — "
        f"{quality['quality']:.1f}%"
    )

elif quality["quality"] >= 80:

    st.warning(
        f"🟡 Data Quality Needs Attention — "
        f"{quality['quality']:.1f}%"
    )

else:

    st.error(
        f"🔴 Poor Data Quality — "
        f"{quality['quality']:.1f}%"
    )


# ============================================================
# KPI DASHBOARD
# ============================================================

st.subheader("📊 Dataset Overview")

k1, k2, k3, k4, k5 = st.columns(5)


with k1:

    st.metric(
        "Total Rows",
        f"{quality['rows']:,}"
    )


with k2:

    st.metric(
        "Total Columns",
        f"{quality['columns']:,}"
    )


with k3:

    st.metric(
        "Missing Values",
        f"{quality['missing']:,}"
    )


with k4:

    st.metric(
        "Duplicate Rows",
        f"{quality['duplicates']:,}"
    )


with k5:

    st.metric(
        "Quality Score",
        f"{quality['quality']:.1f}%"
    )


st.divider()


# ============================================================
# VALIDATION ENGINE
# ============================================================

st.subheader("🛡️ Data Validation Center")


validation_issues = []


# ------------------------------------------------------------
# 1. Missing Values
# ------------------------------------------------------------

for column in working_df.columns:

    missing_count = int(
        working_df[column].isnull().sum()
    )

    if missing_count > 0:

        validation_issues.append(
            {
                "Type": "Missing Values",
                "Column": column,
                "Count": missing_count,
                "Severity": "High"
            }
        )


# ------------------------------------------------------------
# 2. Empty Columns
# ------------------------------------------------------------

for column in working_df.columns:

    if working_df[column].isna().all():

        validation_issues.append(
            {
                "Type": "Empty Column",
                "Column": column,
                "Count": len(working_df),
                "Severity": "High"
            }
        )


# ------------------------------------------------------------
# 3. Duplicate Rows
# ------------------------------------------------------------

duplicate_count = int(
    working_df.duplicated().sum()
)

if duplicate_count > 0:

    validation_issues.append(
        {
            "Type": "Duplicate Rows",
            "Column": "Entire Row",
            "Count": duplicate_count,
            "Severity": "Medium"
        }
    )


# ------------------------------------------------------------
# 4. Negative Numeric Values
# ------------------------------------------------------------

numeric_columns = (
    working_df
    .select_dtypes(include=np.number)
    .columns
    .tolist()
)

negative_counts = {}

for column in numeric_columns:

    count = int(
        (working_df[column] < 0)
        .sum()
    )

    if count > 0:

        negative_counts[column] = count

        validation_issues.append(
            {
                "Type": "Negative Values",
                "Column": column,
                "Count": count,
                "Severity": "Medium"
            }
        )


# ------------------------------------------------------------
# 5. Outlier Detection using IQR
# ------------------------------------------------------------

outlier_counts = {}

for column in numeric_columns:

    series = (
        working_df[column]
        .dropna()
    )

    if len(series) < 4:

        continue

    q1 = series.quantile(0.25)

    q3 = series.quantile(0.75)

    iqr = q3 - q1

    if iqr == 0:

        continue

    lower = q1 - 1.5 * iqr

    upper = q3 + 1.5 * iqr

    count = int(
        (
            (working_df[column] < lower)
            |
            (working_df[column] > upper)
        )
        .sum()
    )

    if count > 0:

        outlier_counts[column] = count

        validation_issues.append(
            {
                "Type": "Possible Outliers",
                "Column": column,
                "Count": count,
                "Severity": "Low"
            }
        )


# ============================================================
# VALIDATION SUMMARY
# ============================================================

if len(validation_issues) == 0:

    st.success(
        "✅ No major data-quality issues detected."
    )

else:

    issue_df = pd.DataFrame(
        validation_issues
    )

    v1, v2, v3 = st.columns(3)

    with v1:

        st.metric(
            "Issues Detected",
            len(validation_issues)
        )

    with v2:

        high_count = sum(
            1
            for issue in validation_issues
            if issue["Severity"] == "High"
        )

        st.metric(
            "High Severity",
            high_count
        )

    with v3:

        medium_count = sum(
            1
            for issue in validation_issues
            if issue["Severity"] == "Medium"
        )

        st.metric(
            "Medium Severity",
            medium_count
        )

    st.dataframe(
        issue_df,
        width="stretch",
        hide_index=True
    )


st.divider()


# ============================================================
# MISSING VALUES REPORT
# ============================================================

st.subheader("🔍 Column-Level Data Profile")

profile_rows = []

for column in working_df.columns:

    missing = int(
        working_df[column].isnull().sum()
    )

    unique = int(
        working_df[column].nunique(
            dropna=True
        )
    )

    dtype = str(
        working_df[column].dtype
    )

    profile_rows.append(
        {
            "Column": column,
            "Data Type": dtype,
            "Missing": missing,
            "Unique Values": unique,
            "Status":
                "⚠️ Check"
                if missing > 0
                else "✅ Good"
        }
    )


profile_df = pd.DataFrame(
    profile_rows
)

st.dataframe(
    profile_df,
    width="stretch",
    hide_index=True
)


st.divider()


# ============================================================
# EDITABLE DATA CLEANING
# ============================================================

st.subheader("✏️ Interactive Data Cleaning")

st.caption(
    "Edit incorrect values directly in the table. "
    "You can add or delete rows."
)


edited_df = st.data_editor(
    working_df,
    width="stretch",
    height=450,
    num_rows="dynamic",
    key="data_editor"
)


# Save edited dataframe into session state

st.session_state.working_df = edited_df.copy()


# ============================================================
# RECHECK AFTER EDITING
# ============================================================

updated_quality = calculate_quality(
    edited_df
)


st.subheader("🔄 Updated Quality")

u1, u2, u3, u4 = st.columns(4)


with u1:

    st.metric(
        "Rows",
        f"{updated_quality['rows']:,}"
    )


with u2:

    st.metric(
        "Missing",
        f"{updated_quality['missing']:,}"
    )


with u3:

    st.metric(
        "Duplicates",
        f"{updated_quality['duplicates']:,}"
    )


with u4:

    st.metric(
        "Quality",
        f"{updated_quality['quality']:.1f}%"
    )


st.divider()


# ============================================================
# FILTERS
# ============================================================

st.subheader("🔎 Interactive Filters")

filtered_df = edited_df.copy()


categorical_columns = (
    filtered_df
    .select_dtypes(
        include=[
            "object",
            "category",
            "string"
        ]
    )
    .columns
    .tolist()
)


if len(categorical_columns) > 0:

    filter_column = st.selectbox(
        "Choose a column",
        ["None"] + categorical_columns
    )

    if filter_column != "None":

        available_values = (
            filtered_df[filter_column]
            .dropna()
            .unique()
            .tolist()
        )

        selected_values = st.multiselect(
            f"Select {filter_column}",
            available_values,
            default=available_values
        )

        if len(selected_values) > 0:

            filtered_df = filtered_df[
                filtered_df[filter_column]
                .isin(selected_values)
            ]

        else:

            filtered_df = filtered_df.iloc[0:0]

else:

    st.info(
        "ℹ️ No categorical columns found."
    )


st.info(
    f"Showing **{len(filtered_df):,}** records."
)


st.divider()


# ============================================================
# NUMERIC ANALYSIS
# ============================================================

numeric_columns = (
    filtered_df
    .select_dtypes(include=np.number)
    .columns
    .tolist()
)


if len(numeric_columns) > 0:

    st.subheader("📈 Numerical Analytics")

    selected_numeric = st.selectbox(
        "Select a numeric column",
        numeric_columns
    )

    series = (
        filtered_df[selected_numeric]
        .dropna()
    )


    # --------------------------------------------------------
    # STATISTICS
    # --------------------------------------------------------

    a1, a2, a3, a4 = st.columns(4)


    with a1:

        st.metric(
            "Average",
            f"{series.mean():,.2f}"
        )


    with a2:

        st.metric(
            "Minimum",
            f"{series.min():,.2f}"
        )


    with a3:

        st.metric(
            "Maximum",
            f"{series.max():,.2f}"
        )


    with a4:

        st.metric(
            "Median",
            f"{series.median():,.2f}"
        )


    # --------------------------------------------------------
    # HISTOGRAM
    # --------------------------------------------------------

    st.markdown("### 📊 Distribution")

    fig_hist = px.histogram(
        filtered_df,
        x=selected_numeric,
        title=f"{selected_numeric} Distribution",
        template="plotly_white"
    )

    fig_hist.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig_hist,
        width="stretch"
    )


    # --------------------------------------------------------
    # BOX PLOT
    # --------------------------------------------------------

    st.markdown("### 🚨 Outlier Visualization")

    fig_box = px.box(
        filtered_df,
        y=selected_numeric,
        title=f"{selected_numeric} Outlier Detection",
        template="plotly_white"
    )

    fig_box.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig_box,
        width="stretch"
    )


else:

    st.warning(
        "⚠️ No numeric columns found."
    )


st.divider()


# ============================================================
# CORRELATION ANALYSIS
# ============================================================

if len(numeric_columns) >= 2:

    st.subheader("🔗 Correlation Analysis")

    correlation = (
        filtered_df[numeric_columns]
        .corr()
    )

    fig_corr = px.imshow(
        correlation,
        text_auto=True,
        title="Numeric Column Correlation",
        color_continuous_scale=[
            "#d62828",
            "#ffffff",
            "#0b5ed7"
        ]
    )

    fig_corr.update_layout(
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig_corr,
        width="stretch"
    )


# ============================================================
# AUTOMATIC INSIGHTS
# ============================================================

st.divider()

st.subheader("💡 Automatic Insights")


if len(numeric_columns) > 0:

    for column in numeric_columns[:5]:

        values = (
            filtered_df[column]
            .dropna()
        )

        if len(values) == 0:

            continue

        average = values.mean()

        maximum = values.max()

        minimum = values.min()

        median = values.median()

        st.markdown(
            f"""
            **{column}**

            - Average: `{average:,.2f}`
            - Median: `{median:,.2f}`
            - Minimum: `{minimum:,.2f}`
            - Maximum: `{maximum:,.2f}`
            """
        )

else:

    st.info(
        "No numeric columns available "
        "for automatic insights."
    )


# ============================================================
# EXPORT
# ============================================================

st.divider()

st.subheader("💾 Export Center")


download_df = filtered_df.copy()

cleaned_csv = (
    download_df
    .to_csv(index=False)
    .encode("utf-8")
)


st.download_button(
    label="📥 Download Cleaned & Filtered CSV",
    data=cleaned_csv,
    file_name="cleaned_data.csv",
    mime="text/csv",
    width="stretch"
)


# ============================================================
# FINAL STATUS
# ============================================================

st.divider()

if updated_quality["quality"] >= 95:

    st.success(
        "✅ Dataset is ready for analysis."
    )

elif updated_quality["quality"] >= 80:

    st.warning(
        "⚠️ Dataset can be analyzed, but some "
        "quality issues remain."
    )

else:

    st.error(
        "🔴 Significant data-quality issues remain. "
        "Review the Validation Center before using "
        "the data for analysis."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        📊 Data Analytics Studio<br>
        Built with Python • Pandas • NumPy • Plotly • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)