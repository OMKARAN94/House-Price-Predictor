# Flowchart Content for Report
## 3.1 Application Entry Flow

### 3.1.1 User Opens Application

When the user opens the application:

•	The Streamlit web application initializes

•	The main page (app.py) loads with navigation options

•	The system displays two primary tool options for the user to select

At this stage, the flow allows the user to choose between Data Analyzer and House Predictor modules.

### 3.1.2 Tool Selection

The user must select one of the available tools:

•	**Option 1:** Data Analyzer Module (pages/1_Data_Analyzer.py)

•	**Option 2:** House Predictor Module (pages/2_House_Predictor.py)

The flow branches based on the user's selection, directing them to the respective module workflow.

---

## 3.2 Data Analyzer Module Flow

### 3.2.1 Upload File

Inside the Data Analyzer module, users can:

•	Upload CSV or Excel files (.xlsx, .xls, .csv)

•	View file upload status and validation

•	See the uploaded file name confirmation

Before processing the file:

•	The system detects the file type (CSV or Excel)

If file reading fails:

•	The system displays an error message

•	The flow stops and prompts the user to upload a valid file

If file reading succeeds:

•	The data is loaded into a pandas DataFrame

•	The system displays a success message with the file name

### 3.2.2 Preview and Dataset Information

After successful file upload:

•	The system displays the first 5 rows of the dataset

•	Shows dataset dimensions (rows and columns count)

•	Presents basic information including:
  - Column data types
  - Summary statistics for numeric columns
  - Missing values count per column
  - Total duplicate rows count

At this stage, users can review the data structure and quality before proceeding to cleaning operations.

### 3.2.3 Data Cleaning Options

Users can choose to clean their data:

•	**Remove Duplicates:** Option to remove duplicate rows with immediate feedback on rows removed

•	**Handle Missing Values:** Select strategies for different column types:
  - For numeric columns: Fill with Mean, Fill with Median, or Drop rows
  - For categorical columns: Fill with Mode or Drop rows

Before applying cleaning:

•	The system identifies numeric and categorical columns automatically

•	Users select their preferred cleaning strategy for each column type

When "Apply Cleaning" button is clicked:

•	The system applies the selected cleaning strategies

•	Updates the dataset shape and displays success message

If cleaning is skipped:

•	The flow proceeds directly to visualization with the original data

### 3.2.4 Visualizations

After data cleaning (or if skipped), users can create visualizations:

•	**Pie Chart Tab:** Generate pie charts for categorical column distributions

•	**Bar Chart/Histogram Tab:** Create histograms for numeric columns or bar charts grouped by categories

•	**Correlation Heatmap Tab:** Display correlation matrix for numeric columns

For each visualization type:

•	Users select the appropriate column(s) from dropdown menus

•	The system generates interactive charts using Plotly or Matplotlib

•	Charts are displayed with full-width container for better visibility

If required columns are not available:

•	The system displays appropriate warning messages

•	Users can proceed to other visualization options

### 3.2.5 Download Cleaned Data

Once users complete their analysis:

•	The cleaned dataset is converted to CSV format

•	A download button is provided with the filename "cleaned_data_output.csv"

•	Users can download the processed data for further use

After download:

•	The system displays a completion success message

•	The Data Analyzer workflow reaches completion

---

## 3.3 House Predictor Module Flow

### 3.3.1 Load Model and Data

When the House Predictor module is accessed:

•	The system loads the pre-trained machine learning model (House_prediction_model.pkl) using pickle

•	The reference dataset (cleaned_data.csv) is loaded into memory

Before processing:

•	The system checks for coordinate columns (latitude, longitude) in the dataset

If coordinates are missing:

•	The system generates synthetic coordinates using numpy.random

•	Coordinates are generated within Bangalore's geographic bounds (latitude: 12.85-13.10, longitude: 77.45-77.75)

If coordinates exist:

•	The system uses the existing coordinate data

### 3.3.2 User Input Collection

Users provide house details through the sidebar interface:

•	**Location:** Select from available locations in the dataset

•	**Total Area:** Enter total square footage (minimum 200 sqft)

•	**Bedrooms:** Enter number of bedrooms (minimum 1)

•	**Bathrooms:** Enter number of bathrooms (minimum 1)

•	**Balconies:** Enter number of balconies (minimum 0)

The input form validates all entries before allowing prediction.

### 3.3.3 Price Prediction

When the "Predict Price" button is clicked:

•	The system collects all user inputs into a DataFrame

•	The input data is formatted to match the model's expected feature structure

•	The pre-trained model performs prediction using model.predict()

•	The predicted price is converted from model units to Lakhs (₹) format

After prediction:

•	The system displays a success message

•	The predicted price is shown as a metric card with formatted currency (₹ X,XXX.XX)

•	Celebration balloons animation is triggered

### 3.3.4 Visualization Display

After price prediction, the system generates multiple visualizations:

•	**Scatter Plot:** Price vs. Total Sqft for the selected location

•	**Bar Chart:** Average price by number of bedrooms in the selected location

•	**Interactive Map:** Geographic visualization of house prices across Bangalore

For the interactive map:

•	Users can adjust a price range slider to filter displayed houses

•	The map shows houses as colored markers based on price

•	Hover tooltips display location and price information

•	The map uses Plotly Scatter Mapbox with dark theme styling

All visualizations are displayed sequentially, allowing users to analyze price trends and geographic patterns.

### 3.3.5 End

Once the user completes all actions such as:

•	Viewing price predictions

•	Exploring visualizations

•	Analyzing geographic price distributions

The House Predictor workflow reaches completion, and users can return to the main page or make additional predictions.

---

## 3.4 Application End Flow

### 3.4.1 Process Completion

Once the user completes all desired actions in either module:

•	Data Analyzer: File uploaded, cleaned, visualized, and downloaded

•	House Predictor: Predictions made and visualizations reviewed

The process reaches the End node, completing the application workflow.

Users can:

•	Return to the main page to select a different tool

•	Upload new files or make additional predictions

•	Exit the application

The flow ensures all user actions are completed successfully before termination, providing a seamless user experience throughout the application lifecycle.

