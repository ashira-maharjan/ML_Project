# 🎓 Student Exam Performance Indicator

An end-to-end Machine Learning project that predicts student math scores based on various demographic and academic factors. The project includes data analysis, model training, and an interactive Streamlit web application for predictions.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange.svg)](https://scikit-learn.org/)

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Contact](#contact)

## 🎯 About

This project predicts student math exam scores based on various factors including:
- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type (standard/free-reduced)
- Test preparation course completion
- Reading score
- Writing score

The project demonstrates a complete ML pipeline from data ingestion to model deployment with both Flask and Streamlit interfaces.



## ✨ Features

- **Interactive Web Interface**: Two deployment options - Streamlit and Flask
- **Real-time Predictions**: Instant math score predictions based on input parameters
- **Comprehensive Analysis**: 
  - Input summary display
  - Complete score summary (Math, Reading, Writing)
  - Average score calculation
- **Modular Design**: Organized code structure for easy maintenance
- **Data Pipeline**: Complete ETL pipeline for data processing

## 📁 Project Structure

```
ML_Project/
│
├── artifacts/                      # Saved models and preprocessors
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── catboost_info/                  # CatBoost training logs
│
├── notebook/                       # Jupyter notebooks
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
|   └── EDA_STUDENT_PERFORMANCE.ipynb
|   └── data/ stud.csv
│
├── src/                            # Source code
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/                      # HTML templates for Flask
│   ├── home.html
│   └── index.html
│
├── app.py                         # Flask application
├── streamlit_app.py               # Streamlit application
├── try_app.py                     # Alternative Streamlit app
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup
├── .gitignore                     # Git ignore file
└── README.md                      # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- install required libraries using `requirements.txt`
``` python 
# To install 
pip install -r requirements.txt 
```

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/ashira-maharjan/ML_Project.git
cd ML_Project
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the package**
```bash
pip install -e .
```

## 💻 Usage

### Running the Streamlit App

```bash
streamlit run streamlit_app.py
```

The app will open in your default browser at `http://localhost:8501`

### Running the Flask App

```bash
python app.py
```

Visit `http://localhost:8000` in your browser

### Making Predictions

1. Fill in all the required fields:
   - Select gender
   - Choose race/ethnicity group
   - Select parental education level
   - Choose lunch type
   - Indicate test preparation course status
   - Enter reading score (0-100)
   - Enter writing score (0-100)

2. Click "Predict Your Math Score"

3. View your results:
   - Predicted math score
   - Complete score summary
   - Average score
   - Performance analysis

## 🧠 Model Details

### Algorithms Evaluated
The project evaluates multiple regression algorithms:
- Linear Regression
- Lasso Regression
- Ridge Regression
- K-Neighbors Regressor
- Decision Tree
- Random Forest
- XGBoost
- CatBoost
- AdaBoost

### Model Selection
The best performing model is automatically selected based on R² score during training.

### Features Used
- **Categorical Features**: 
  - Gender (male/female)
  - Race/Ethnicity (Group A-E)
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course

- **Numerical Features**:
  - Reading Score
  - Writing Score

### Performance Metrics
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.8+**: Primary programming language
- **scikit-learn**: Machine learning algorithms and preprocessing
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing

### ML Libraries
- **XGBoost**: Gradient boosting framework
- **CatBoost**: Gradient boosting with categorical features
- **dill**: Model serialization

### Web Frameworks
- **Streamlit**: Interactive web application
- **Flask**: Web application framework

### Development Tools
- **Jupyter Notebook**: Exploratory data analysis
- **Git**: Version control

##  Dataset

The dataset contains information about student performance including:
- **Size**: ~1000 student records
- **Features**: 8 input features
- **Target**: Math score (0-100)

### Data Sources
The data is stored in the `notebook/data/` directory (if applicable) and includes:
- Training data
- Testing data


##  Acknowledgments

- Dataset source: [Student Performance Dataset]
- Inspiration from various ML tutorials and courses
- scikit-learn documentation
- Streamlit community

---

##  Screenshots
### Streamlit Interface
The application features a modern, user-friendly interface with:
- Clean and intuitive form inputs
- Real-time prediction results
- Performance analysis
- Score summary visualizations

```python 
streamlit run streamlit_app.py

```
![Form](images\streamlit1.png "Form")
---
![Input](images\image.png "Summary")
---
![Input](images\streamlit3.png "Summary")


### Flask Interface
Traditional web application with HTML templates for predictions.
``` python 
python app.py
```

- Open web page and type if you have use ``` app.run(port=8000,debug=True)```
```
http://localhost:8000/
```

- For predictdata view 
```
http://localhost:8000/predictdata
```



### Results Display
- Predicted math score prominently displayed
- Comprehensive metrics including reading and writing scores
- Average score calculation


---

## 🔄 Future Enhancements

- [ ] Add user authentication
- [ ] Implement batch prediction capability
- [ ] Add model retraining interface
- [ ] Include data visualization dashboard
- [ ] Deploy to cloud platform (AWS/Azure/Heroku)
- [ ] Add API documentation
- [ ] Implement A/B testing for models
- [ ] Add explanation for predictions (SHAP values)

---

## 📧 Contact

**Ashira Maharjan**

- GitHub: [@ashira-maharjan](https://github.com/ashira-maharjan)
- Project Link: [https://github.com/ashira-maharjan/ML_Project](https://github.com/ashira-maharjan/ML_Project)