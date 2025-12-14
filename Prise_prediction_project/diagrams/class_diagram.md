# Class Diagram - House Price Prediction Project

```mermaid
classDiagram
    class StreamlitApp {
        +st.set_page_config()
        +st.title()
        +st.write()
    }
    
    class MainApp {
        +app.py
        +welcome_page()
        +navigate_to_pages()
    }
    
    class DataAnalyzer {
        +pages/1_Data_Analyzer.py
        +upload_file()
        +read_data()
        +clean_data()
        +visualize_data()
        +download_cleaned_data()
    }
    
    class HousePredictor {
        +pages/2_House_Predictor.py
        +load_model()
        +load_data()
        +get_user_input()
        +predict_price()
        +visualize_results()
        +display_map()
    }
    
    class MLModel {
        +House_prediction_model.pkl
        +predict()
        +OneHotEncoder
        +StandardScaler
        +LinearRegression
    }
    
    class DataProcessor {
        +pandas.DataFrame
        +numpy.array
        +clean_data()
        +preprocess_data()
        +add_coordinates()
    }
    
    class Visualizer {
        +matplotlib.pyplot
        +plotly.express
        +create_scatter_plot()
        +create_bar_chart()
        +create_map()
        +create_pie_chart()
        +create_heatmap()
    }
    
    class DataStorage {
        +cleaned_data.csv
        +Bengaluru_House_Data.csv
        +location: string
        +total_sqft: float
        +bath: float
        +balcony: float
        +bedrooms: int
        +price: float
        +latitude: float
        +longitude: float
    }
    
    MainApp --> DataAnalyzer : uses
    MainApp --> HousePredictor : uses
    DataAnalyzer --> DataProcessor : uses
    DataAnalyzer --> Visualizer : uses
    HousePredictor --> MLModel : loads
    HousePredictor --> DataProcessor : uses
    HousePredictor --> Visualizer : uses
    HousePredictor --> DataStorage : reads
    DataProcessor --> DataStorage : processes
    MLModel --> DataProcessor : preprocesses
```

## Module Structure

### Main Application (`app.py`)
- Entry point of the Streamlit application
- Provides navigation to different tools

### Data Analyzer Module (`pages/1_Data_Analyzer.py`)
- **Functions:**
  - File upload handling (CSV/Excel)
  - Data reading and preview
  - Data cleaning (duplicates, missing values)
  - Data visualization (pie charts, bar charts, heatmaps)
  - Data export functionality

### House Predictor Module (`pages/2_House_Predictor.py`)
- **Functions:**
  - Model loading from pickle file
  - Data loading from CSV
  - User input collection
  - Price prediction
  - Result visualization
  - Interactive map display

### Machine Learning Pipeline
- **Components:**
  - ColumnTransformer (OneHotEncoder for location)
  - StandardScaler (feature scaling)
  - LinearRegression (prediction model)

### Data Processing
- Pandas for data manipulation
- NumPy for numerical operations
- Data cleaning and preprocessing

### Visualization
- Matplotlib for static plots
- Plotly for interactive visualizations
- Map visualization with geographic data





