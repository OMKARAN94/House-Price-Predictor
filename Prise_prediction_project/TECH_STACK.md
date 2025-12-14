# Tech Stack - House Price Prediction Project

## Overview
This document outlines the technology stack used in the **Alpha Analytics Multi-Tool Platform** for house price prediction and data analysis.

---

## Frontend & Web Framework

### **Streamlit** 🎨
- **Version**: Latest
- **Purpose**: Web application framework for building the interactive UI
- **Usage**: 
  - Main application interface (`app.py`)
  - Data Analyzer module (`pages/1_Data_Analyzer.py`)
  - House Price Predictor module (`pages/2_House_Predictor.py`)
- **Features Used**:
  - Multi-page application structure
  - File uploader
  - Interactive widgets (sliders, selectboxes, buttons)
  - Data visualization display
  - Custom CSS styling

---

## Data Processing & Analysis

### **Pandas** 📊
- **Purpose**: Data manipulation and analysis
- **Usage**:
  - Reading CSV/Excel files
  - Data cleaning (removing duplicates, handling missing values)
  - Data transformation and feature engineering
  - Data aggregation and grouping
  - Exporting cleaned data

### **NumPy** 🔢
- **Purpose**: Numerical computing
- **Usage**:
  - Mathematical operations
  - Array operations
  - Statistical calculations
  - Random number generation (for synthetic coordinates)

---

## Machine Learning

### **scikit-learn (sklearn)** 🤖
- **Purpose**: Machine learning model development and deployment
- **Components Used**:
  - `LinearRegression`: Main prediction model
  - `OneHotEncoder`: Categorical feature encoding (location)
  - `StandardScaler`: Feature scaling/normalization
  - `make_pipeline`: Model pipeline creation
  - `make_column_transformer`: Column-specific transformations
  - `train_test_split`: Data splitting for model evaluation
- **Model Architecture**:
  - Pipeline: OneHotEncoder → StandardScaler → LinearRegression

### **Pickle** 💾
- **Purpose**: Model serialization and persistence
- **Usage**: 
  - Saving trained model (`House_prediction_model.pkl`)
  - Loading model for predictions in production

---

## Data Visualization

### **Matplotlib** 📈
- **Purpose**: Static plotting and visualization
- **Usage**:
  - Scatter plots (Price vs Sqft)
  - Bar charts (Average price by bedrooms)
  - Histograms
  - Custom styling and theming

### **Plotly Express** 🗺️
- **Purpose**: Interactive visualizations and maps
- **Usage**:
  - Interactive pie charts
  - Interactive bar charts
  - Correlation heatmaps
  - Interactive map visualization (scatter_mapbox) for Bangalore house locations
  - Price range filtering on maps

---

## Data Storage

### **CSV Files** 📁
- **Format**: Comma-separated values
- **Files**:
  - `Bengaluru_House_Data.csv`: Raw dataset
  - `cleaned_data.csv`: Processed dataset for predictions
  - `cleaned_data1.csv`: Alternative cleaned dataset

---

## Development Tools

### **Jupyter Notebook** 📓
- **Purpose**: Model development and experimentation
- **File**: `Banglore_house_prediction.ipynb`
- **Usage**:
  - Data exploration
  - Feature engineering
  - Model training and evaluation
  - Data preprocessing pipeline development

---

## Project Structure

```
Prise_prediction_project/
├── app.py                          # Main Streamlit application
├── pages/
│   ├── 1_Data_Analyzer.py         # Data analysis module
│   ├── 2_House_Predictor.py       # House price prediction module
│   └── House_prediction_model.pkl # Trained ML model
├── models/
│   └── House_prediction_model.pkl  # Model backup
├── Banglore_house_prediction.ipynb # Model development notebook
├── Bengaluru_House_Data.csv        # Raw dataset
├── cleaned_data.csv                # Processed dataset
└── diagrams/                       # Project documentation
```

---

## Dependencies Summary

### Core Libraries
- `streamlit` - Web framework
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning
- `matplotlib` - Static plotting
- `plotly` - Interactive visualizations
- `pickle` - Model serialization (built-in)

### Optional/Additional
- `openpyxl` or `xlrd` - For Excel file reading (if needed)

---

## Recommended Installation

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
plotly>=5.17.0
openpyxl>=3.1.0
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Technology Highlights

### ✅ **Strengths**
- **Rapid Development**: Streamlit enables quick UI development
- **Interactive Visualizations**: Plotly provides rich, interactive charts
- **End-to-End Pipeline**: Complete ML pipeline from data cleaning to prediction
- **User-Friendly**: No-code interface for data analysis and predictions

### 🔄 **Potential Enhancements**
- Database integration (PostgreSQL, MySQL) for data persistence
- REST API (FastAPI/Flask) for model serving
- Cloud deployment (Streamlit Cloud, Heroku, AWS)
- Model versioning (MLflow, DVC)
- Advanced ML models (Random Forest, XGBoost, Neural Networks)
- Real-time data updates
- User authentication and session management

---

## Version Information

- **Python**: 3.x (recommended 3.8+)
- **Streamlit**: Latest stable version
- **scikit-learn**: 1.3.0+
- **Pandas**: 2.0.0+
- **NumPy**: 1.24.0+

---

*Last Updated: 2025*
*Project: Alpha Analytics Multi-Tool Platform*




