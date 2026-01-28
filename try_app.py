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
    page_icon="📊",
    layout="centered"
)

# ============================================
# CUSTOM CSS - FIXED COLORS FOR VISIBILITY
# ============================================
st.markdown("""
    <style>
    /* Main container styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Content container */
    .main {
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        max-width: 600px;
        margin: 20px auto;
    }
    
    /* Title styling */
    h1 {
        color: #667eea !important;
        text-align: center;
        font-size: 28px !important;
        font-weight: 600 !important;
        margin-bottom: 30px;
    }
    
    /* Legend/subtitle styling */
    .legend-text {
        color: #333;
        font-size: 22px;
        font-weight: 500;
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* Form labels - DARK COLOR FOR VISIBILITY */
    .stSelectbox label, .stNumberInput label {
        color: #2d3748 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        margin-bottom: 8px !important;
    }
    
    /* Select boxes - WHITE BACKGROUND WITH DARK TEXT */
    .stSelectbox > div > div {
        border: 2px solid #cbd5e0 !important;
        border-radius: 8px !important;
        background-color: #ffffff !important;
        padding: 12px 15px !important;
        font-size: 15px !important;
        color: #2d3748 !important;
        font-weight: 500 !important;
    }
    
    /* Select box dropdown text */
    .stSelectbox div[data-baseweb="select"] > div {
        color: #2d3748 !important;
        background-color: #ffffff !important;
    }
    
    /* Number inputs - WHITE BACKGROUND WITH DARK TEXT */
    .stNumberInput > div > div > input {
        border: 2px solid #cbd5e0 !important;
        border-radius: 8px !important;
        background-color: #ffffff !important;
        padding: 12px 15px !important;
        font-size: 15px !important;
        color: #2d3748 !important;
        font-weight: 500 !important;
    }
    
    /* Placeholder text - GRAY BUT VISIBLE */
    input::placeholder {
        color: #718096 !important;
        opacity: 1 !important;
    }
    
    /* Focus states */
    .stSelectbox > div > div:focus-within,
    .stNumberInput > div > div > input:focus {
        border-color: #667eea !important;
        background-color: #ffffff !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    }
    
    /* Hover states */
    .stSelectbox > div > div:hover,
    .stNumberInput > div > div > input:hover {
        border-color: #667eea !important;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.15) !important;
    }
    
    /* Submit button */
    .stButton > button {
        width: 100%;
        padding: 14px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transition: all 0.3s ease;
        margin-top: 10px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Result box */
    .result-box {
        text-align: center;
        margin-top: 30px;
        padding: 20px;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border-radius: 10px;
        font-size: 20px;
        animation: pulse 2s infinite;
    }
    
    /* Summary box */
    .summary-box {
        background: #f8f9fa;
        border-left: 4px solid #667eea;
        padding: 20px;
        margin: 20px 0;
        border-radius: 8px;
    }
    
    .summary-title {
        color: #667eea;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 15px;
        text-align: center;
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.02);
        }
    }
    
    /* Dataframe styling - DARK TEXT */
    [data-testid="stDataFrame"] {
        color: #2d3748 !important;
    }
    
    [data-testid="stDataFrame"] td,
    [data-testid="stDataFrame"] th {
        color: #2d3748 !important;
        background-color: #ffffff !important;
    }
    
    /* Metrics - DARK TEXT */
    [data-testid="stMetricValue"] {
        color: #2d3748 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #4a5568 !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Adjust spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Remove number input arrows */
    input[type=number]::-webkit-inner-spin-button,
    input[type=number]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    input[type=number] {
        -moz-appearance: textfield;
    }
    
    /* Select dropdown menu */
    div[role="listbox"] {
        background-color: #ffffff !important;
    }
    
    div[role="option"] {
        color: #2d3748 !important;
        background-color: #ffffff !important;
    }
    
    div[role="option"]:hover {
        background-color: #edf2f7 !important;
    }
    
    /* Help icon color */
    .stNumberInput button {
        color: #718096 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# TITLE
# ============================================
st.markdown("<h1>📊 Student Exam Performance Indicator</h1>", unsafe_allow_html=True)
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
submit_button = st.button("Predict Your Math Score 🎯")

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
            
            # Display as a nice table
            st.dataframe(
                summary_df,
                hide_index=True,
                use_container_width=True,
                column_config={
                    "Field": st.column_config.TextColumn("Field", width="medium"),
                    "Value": st.column_config.TextColumn("Value", width="medium"),
                }
            )
            
            st.markdown("---")
            
            # Show loading spinner
            with st.spinner('🔮 Predicting your math score...'):
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
                    🎯 The Prediction is: {predicted_score}
                </div>
            """, unsafe_allow_html=True)
            
            # Additional metrics
            st.markdown("### 📊 Complete Score Summary")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label="📝 Math Score",
                    value=f"{predicted_score}",
                    delta="Predicted"
                )
            
            with col2:
                st.metric(
                    label="📖 Reading Score",
                    value=f"{reading_score}",
                    delta="Input"
                )
            
            with col3:
                st.metric(
                    label="✍️ Writing Score",
                    value=f"{writing_score}",
                    delta="Input"
                )
            
            # Calculate average
            avg_score = round((predicted_score + reading_score + writing_score) / 3, 2)
            
            st.markdown("---")
            st.metric(
                label="📊 Average Score",
                value=f"{avg_score}/100",
                delta=f"{avg_score:.1f}%"
            )
            
            # Performance analysis
            st.markdown("### 📈 Performance Analysis")
            
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