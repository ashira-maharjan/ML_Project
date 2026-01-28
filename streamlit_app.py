import streamlit as st
import pandas as pd
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import your existing prediction pipeline
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Student Exam Performance Indicator",
    page_icon="🎓",
    layout="centered"
)

# ============================================
# CUSTOM CSS - VISIBLE COLORS & BIG HEADLINES
# ============================================
st.markdown("""
    <style>
    /* Main container styling - LIGHT BLUE BACKGROUND */
    .stApp {
        background: #e8f4f8;
    }
    
    /* Content container */
    .main {
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        max-width: 650px;
        margin: 20px auto;
    }
    
    /* Title styling - BIGGER */
    h1 {
        color: #1e3a8a !important;
        text-align: center;
        font-size: 42px !important;
        font-weight: 700 !important;
        margin-bottom: 30px;
    }
    
    /* Legend/subtitle styling - BIGGER */
    .legend-text {
        color: #1e40af;
        font-size: 28px;
        font-weight: 600;
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* =============================================
       LABELS - DARK TEXT (VISIBLE!)
    ============================================= */
    label[data-testid="stWidgetLabel"] {
        color: #1a202c !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        text-shadow: none !important;
        background: none !important;
    }
    
    .stSelectbox label,
    .stNumberInput label {
        color: #1a202c !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }
    
    /* =============================================
       SELECT BOXES - WHITE BG WITH BLACK TEXT
    ============================================= */
    .stSelectbox [data-baseweb="select"] {
        background-color: #ffffff !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 2px solid #cbd5e0 !important;
        border-radius: 8px !important;
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    
    /* Select box text */
    .stSelectbox [data-baseweb="select"] span {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    
    /* Dropdown arrow */
    .stSelectbox [data-baseweb="select"] svg {
        fill: #000000 !important;
    }
    
    /* =============================================
       NUMBER INPUTS - WHITE BG WITH BLACK TEXT
    ============================================= */
    .stNumberInput input {
        background-color: #ffffff !important;
        border: 2px solid #cbd5e0 !important;
        border-radius: 8px !important;
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 12px 15px !important;
    }
    
    /* Placeholder - DARK GRAY */
    .stNumberInput input::placeholder {
        color: #4a5568 !important;
        font-weight: 500 !important;
        opacity: 1 !important;
    }
    
    /* Number input buttons */
    .stNumberInput button {
        color: #000000 !important;
    }
    
    /* =============================================
       FOCUS & HOVER STATES
    ============================================= */
    .stSelectbox [data-baseweb="select"] > div:hover,
    .stNumberInput input:hover {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 1px #3b82f6 !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div:focus-within,
    .stNumberInput input:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3) !important;
    }
    
    /* =============================================
       DROPDOWN MENU - WHITE WITH BLACK TEXT
    ============================================= */
    [data-baseweb="popover"] {
        background-color: #ffffff !important;
    }
    
    [role="listbox"] {
        background-color: #ffffff !important;
    }
    
    [role="option"] {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 600 !important;
    }
    
    [role="option"]:hover {
        background-color: #e0e7ff !important;
        color: #000000 !important;
    }
    
    [role="option"][aria-selected="true"] {
        background-color: #dbeafe !important;
        color: #000000 !important;
    }
    
    /* =============================================
       SUBMIT BUTTON
    ============================================= */
    .stButton > button {
        width: 100%;
        padding: 16px;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        font-weight: 700;
        background: #2563eb;
        color: white;
        transition: all 0.3s ease;
        margin-top: 10px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.4);
        background: #1d4ed8;
    }
    
    /* =============================================
       RESULT BOX
    ============================================= */
    .result-box {
        text-align: center;
        margin-top: 30px;
        padding: 25px;
        background: #10b981;
        color: white;
        border-radius: 12px;
        font-size: 26px;
        font-weight: 700;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    
    /* =============================================
       SUMMARY BOX
    ============================================= */
    .summary-box {
        background: #f0f9ff;
        border-left: 5px solid #3b82f6;
        padding: 20px;
        margin: 20px 0;
        border-radius: 8px;
    }
    
    .summary-title {
        color:#1e40af;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 15px;
        text-align: center;
    }
    
    /* =============================================
       DATAFRAME - BLACK TEXT
    ============================================= */
    [data-testid="stDataFrame"] {
        color: #000000 !important;
    }
    
    [data-testid="stDataFrame"] table {
        color: #000000 !important;
    }
    
    [data-testid="stDataFrame"] td,
    [data-testid="stDataFrame"] th {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    
    /* =============================================
       METRICS - BLACK TEXT
    ============================================= */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 24px !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #2d3748 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    
    div[data-testid="metric-container"] {
        background: #f8fafc;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }
    
    /* =============================================
       MARKDOWN TEXT - BLACK & BIGGER
    ============================================= */
    .main h3 {
        color: #000000  !important;
        font-size: 24px !important;
        font-weight: 700 !important;
    }
    
  
    /* =============================================
       ALERTS - GOOD CONTRAST
    ============================================= */
    .stAlert {
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    
    /* =============================================
       HIDE STREAMLIT BRANDING
    ============================================= */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    
    </style>
""", unsafe_allow_html=True)

# ============================================
# TITLE - BIGGER HEADLINES
# ============================================
st.markdown("<h1> Student Exam Performance Indicator</h1>", unsafe_allow_html=True)
st.markdown("<p class='legend-text'>Student Exam Performance Prediction</p>", unsafe_allow_html=True)

# ============================================
# FORM
# ============================================

# Gender
gender = st.selectbox(
    "Gender",
    options=["", "male", "female"],
    format_func=lambda x: "Select your Gender" if x == "" else x.capitalize()
)

# Race or Ethnicity
ethnicity = st.selectbox(
    "Race or Ethnicity",
    options=["", "group A", "group B", "group C", "group D", "group E"],
    format_func=lambda x: "Select Ethnicity" if x == "" else x.capitalize()
)

# Parental Level of Education
parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    options=[
        "",
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ],
    format_func=lambda x: "Select Parent Education" if x == "" else x.title()
)

# Lunch Type
lunch = st.selectbox(
    "Lunch Type",
    options=["", "free/reduced", "standard"],
    format_func=lambda x: "Select Lunch Type" if x == "" else x.title()
)

# Test Preparation Course
test_preparation_course = st.selectbox(
    "Test Preparation Course",
    options=["", "none", "completed"],
    format_func=lambda x: "Select Test Course" if x == "" else x.capitalize()
)

# Reading Score
reading_score = st.number_input(
    "Reading Score (out of 100)",
    min_value=0,
    max_value=100,
    value=None,
    step=1,
    placeholder="Enter your Reading score",
    help="Enter a score between 0 and 100"
)

# Writing Score
writing_score = st.number_input(
    "Writing Score (out of 100)",
    min_value=0,
    max_value=100,
    value=None,
    step=1,
    placeholder="Enter your Writing score",
    help="Enter a score between 0 and 100"
)

# Submit Button
submit_button = st.button(" Predict Your Math Score")

# ============================================
# PREDICTION LOGIC
# ============================================
if submit_button:
    # Validation
    if (gender == "" or ethnicity == "" or parental_level_of_education == "" or 
        lunch == "" or test_preparation_course == "" or 
        reading_score is None or writing_score is None):
        st.error("⚠️ Please fill in all fields before submitting!")
    else:
        try:
            # ============================================
            # DISPLAY INPUT SUMMARY
            # ============================================
            st.markdown("""
                <div class='summary-box'>
                    <div class='summary-title'>📋 Input Summary</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Create summary table
            summary_data = {
                "Field": [
                    "Gender",
                    "Race/Ethnicity",
                    "Parental Education",
                    "Lunch Type",
                    "Test Preparation",
                    "Reading Score",
                    "Writing Score"
                ],
                "Value": [
                    gender.capitalize(),
                    ethnicity.capitalize(),
                    parental_level_of_education.title(),
                    lunch.title(),
                    test_preparation_course.capitalize(),
                    f"{reading_score}/100",
                    f"{writing_score}/100"
                ]
            }
            
            summary_df = pd.DataFrame(summary_data)
            
            # Display as a nice table - FIXED: use width instead of use_container_width
            st.dataframe(
                summary_df,
                hide_index=True,
                width=600,  # Changed from use_container_width=True
                column_config={
                    "Field": st.column_config.TextColumn("Field", width="medium"),
                    "Value": st.column_config.TextColumn("Value", width="medium"),
                }
            )
            
            st.markdown("---")
            
            # Show loading spinner
            with st.spinner(' Predicting your math score...'):
                # Create CustomData object
                data = CustomData(
                    gender=gender,
                    race_ethnicity=ethnicity,
                    parental_level_of_education=parental_level_of_education,
                    lunch=lunch,
                    test_preparation_course=test_preparation_course,
                    reading_score=reading_score,
                    writing_score=writing_score
                )
                
                # Get dataframe
                pred_df = data.get_data_as_data_frame()
                
                # Make prediction
                predict_pipeline = PredictPipeline()
                results = predict_pipeline.predict(pred_df)
                
                # Round the result
                predicted_score = round(results[0], 2)
            
            # Display result
            st.markdown(f"""
                <div class='result-box'>
                    Predicted Math Score: {predicted_score}/100
                </div>
            """, unsafe_allow_html=True)
            
            # Additional metrics
            st.markdown("###  Complete Score Summary")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label="📝 Math Score",
                    value=f"{predicted_score}",
                    
                )
            
            with col2:
                st.metric(
                    label="📖 Reading Score",
                    value=f"{reading_score}",
                  
                )
            
            with col3:
                st.metric(
                    label="✍️ Writing Score",
                    value=f"{writing_score}",
                   
                )
            
            # Calculate average
            avg_score = round((predicted_score + reading_score + writing_score) / 3, 2)
            
            st.markdown("---")
            st.metric(
                label=" Average Score",
                value=f"{avg_score}/100",
                
            )
            
            # Performance analysis
            st.markdown("###  Performance Analysis")
            
            if avg_score >= 90:
                st.success("🌟 Outstanding Performance! Excellent work!")
            elif avg_score >= 80:
                st.success("⭐ Excellent Performance! Keep it up!")
            elif avg_score >= 70:
                st.info("👍 Good Performance! You're doing well!")
            elif avg_score >= 60:
                st.warning("⚠️ Average Performance. Room for improvement!")
            else:
                st.error("❗ Below Average. Consider additional support and study time.")
            
        except Exception as e:
            st.error(f"❌ Error making prediction: {str(e)}")
            st.info("Make sure your model files are in the artifacts folder!")
            
            # Debug information
            with st.expander("🔍 Debug Information"):
                st.code(str(e))
                st.write("**Current directory:**", os.getcwd())
                if os.path.exists('artifacts'):
                    st.write("**Files in artifacts:**", os.listdir('artifacts'))
                else:
                    st.write("❌ **Artifacts folder not found!**")
                
                st.write("**Expected files:**")
                st.code("""
                artifacts/
                ├── model.pkl
                └── preprocessor.pkl
                """)