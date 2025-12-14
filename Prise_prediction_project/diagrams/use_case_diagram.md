# Use Case Diagram - House Price Prediction Project

```mermaid
graph TB
    User[👤 User]
    
    subgraph System["🏠 Alpha Analytics Multi-Tool Platform"]
        UC1[Use Case 1:<br/>Access Main Application]
        UC2[Use Case 2:<br/>Upload Data File]
        UC3[Use Case 3:<br/>View Data Preview]
        UC4[Use Case 4:<br/>Analyze Dataset Information]
        UC5[Use Case 5:<br/>Clean Data]
        UC6[Use Case 6:<br/>Create Visualizations]
        UC7[Use Case 7:<br/>Download Cleaned Data]
        UC8[Use Case 8:<br/>Enter House Details]
        UC9[Use Case 9:<br/>Predict House Price]
        UC10[Use Case 10:<br/>View Price Visualizations]
        UC11[Use Case 11:<br/>Explore Interactive Map]
        UC12[Use Case 12:<br/>Filter by Price Range]
    end
    
    User -->|"Opens Application"| UC1
    User -->|"Selects Data Analyzer"| UC2
    User -->|"Uploads CSV/Excel"| UC2
    User -->|"Views Data"| UC3
    User -->|"Checks Dataset Info"| UC4
    User -->|"Removes Duplicates"| UC5
    User -->|"Handles Missing Values"| UC5
    User -->|"Creates Pie Chart"| UC6
    User -->|"Creates Bar Chart"| UC6
    User -->|"Creates Heatmap"| UC6
    User -->|"Downloads CSV"| UC7
    User -->|"Selects House Predictor"| UC8
    User -->|"Enters Location"| UC8
    User -->|"Enters House Features"| UC8
    User -->|"Clicks Predict Button"| UC9
    User -->|"Views Predicted Price"| UC9
    User -->|"Views Scatter Plot"| UC10
    User -->|"Views Bar Chart"| UC10
    User -->|"Interacts with Map"| UC11
    User -->|"Adjusts Price Slider"| UC12
    
    UC2 --> UC3
    UC3 --> UC4
    UC4 --> UC5
    UC5 --> UC6
    UC6 --> UC7
    UC8 --> UC9
    UC9 --> UC10
    UC10 --> UC11
    UC11 --> UC12
```

## Detailed Use Case Diagram (UML Style)

```mermaid
graph LR
    subgraph Actors
        User[👤 User<br/>End User]
    end
    
    subgraph System["🏠 Alpha Analytics System"]
        subgraph DataAnalyzer["📊 Data Analyzer Module"]
            UC1[UC1: Upload File]
            UC2[UC2: Preview Data]
            UC3[UC3: View Dataset Info]
            UC4[UC4: Remove Duplicates]
            UC5[UC5: Handle Missing Values]
            UC6[UC6: Create Pie Chart]
            UC7[UC7: Create Bar Chart]
            UC8[UC8: Create Heatmap]
            UC9[UC9: Download Cleaned Data]
        end
        
        subgraph HousePredictor["🏡 House Price Predictor Module"]
            UC10[UC10: Enter House Details]
            UC11[UC11: Predict Price]
            UC12[UC12: View Price vs Sqft Plot]
            UC13[UC13: View Avg Price by Bedrooms]
            UC14[UC14: Explore Interactive Map]
            UC15[UC15: Filter by Price Range]
        end
    end
    
    User -->|"interacts with"| UC1
    User -->|"interacts with"| UC2
    User -->|"interacts with"| UC3
    User -->|"interacts with"| UC4
    User -->|"interacts with"| UC5
    User -->|"interacts with"| UC6
    User -->|"interacts with"| UC7
    User -->|"interacts with"| UC8
    User -->|"interacts with"| UC9
    User -->|"interacts with"| UC10
    User -->|"interacts with"| UC11
    User -->|"interacts with"| UC12
    User -->|"interacts with"| UC13
    User -->|"interacts with"| UC14
    User -->|"interacts with"| UC15
    
    UC1 -.->|"extends"| UC2
    UC2 -.->|"extends"| UC3
    UC3 -.->|"extends"| UC5
    UC5 -.->|"extends"| UC6
    UC5 -.->|"extends"| UC7
    UC5 -.->|"extends"| UC8
    UC6 -.->|"extends"| UC9
    UC7 -.->|"extends"| UC9
    UC8 -.->|"extends"| UC9
    UC10 -.->|"extends"| UC11
    UC11 -.->|"extends"| UC12
    UC11 -.->|"extends"| UC13
    UC11 -.->|"extends"| UC14
    UC14 -.->|"extends"| UC15
```

## Use Case Descriptions

### Data Analyzer Module

#### UC1: Upload File
- **Actor**: User
- **Description**: User uploads a CSV or Excel file for analysis
- **Preconditions**: User has access to the application
- **Postconditions**: File is loaded into the system
- **Main Flow**: 
  1. User clicks file uploader
  2. User selects CSV/Excel file
  3. System validates file format
  4. System loads file into memory

#### UC2: Preview Data
- **Actor**: User
- **Description**: User views first 5 rows of uploaded data
- **Preconditions**: File has been uploaded (UC1)
- **Postconditions**: Data preview is displayed

#### UC3: View Dataset Information
- **Actor**: User
- **Description**: User views column types, summary statistics, missing values, and duplicates
- **Preconditions**: File has been uploaded (UC1)
- **Postconditions**: Dataset information is displayed

#### UC4: Remove Duplicates
- **Actor**: User
- **Description**: User removes duplicate rows from dataset
- **Preconditions**: Data has been loaded (UC1)
- **Postconditions**: Duplicate rows are removed

#### UC5: Handle Missing Values
- **Actor**: User
- **Description**: User handles missing values using selected strategy (Mean/Median/Mode/Drop)
- **Preconditions**: Data has been loaded (UC1)
- **Postconditions**: Missing values are handled according to strategy

#### UC6: Create Pie Chart
- **Actor**: User
- **Description**: User creates a pie chart for categorical column
- **Preconditions**: Data has been loaded (UC1)
- **Postconditions**: Pie chart is displayed

#### UC7: Create Bar Chart
- **Actor**: User
- **Description**: User creates bar chart or histogram for numeric column
- **Preconditions**: Data has been loaded (UC1)
- **Postconditions**: Bar chart/histogram is displayed

#### UC8: Create Heatmap
- **Actor**: User
- **Description**: User creates correlation heatmap for numeric columns
- **Preconditions**: Data has been loaded (UC1)
- **Postconditions**: Correlation heatmap is displayed

#### UC9: Download Cleaned Data
- **Actor**: User
- **Description**: User downloads cleaned dataset as CSV
- **Preconditions**: Data has been processed (UC4 or UC5)
- **Postconditions**: CSV file is downloaded

### House Price Predictor Module

#### UC10: Enter House Details
- **Actor**: User
- **Description**: User enters house location, area, bedrooms, bathrooms, and balconies
- **Preconditions**: User has access to House Predictor module
- **Postconditions**: Input data is collected

#### UC11: Predict Price
- **Actor**: User
- **Description**: System predicts house price based on user input using ML model
- **Preconditions**: User has entered house details (UC10)
- **Postconditions**: Predicted price is displayed
- **Main Flow**:
  1. User clicks "Predict Price" button
  2. System loads ML model
  3. System preprocesses input data
  4. System makes prediction
  5. System displays predicted price

#### UC12: View Price vs Sqft Plot
- **Actor**: User
- **Description**: User views scatter plot showing price vs square feet for selected location
- **Preconditions**: Price has been predicted (UC11)
- **Postconditions**: Scatter plot is displayed

#### UC13: View Avg Price by Bedrooms
- **Actor**: User
- **Description**: User views bar chart showing average price by number of bedrooms
- **Preconditions**: Price has been predicted (UC11)
- **Postconditions**: Bar chart is displayed

#### UC14: Explore Interactive Map
- **Actor**: User
- **Description**: User explores interactive map showing house prices across Bangalore
- **Preconditions**: Price has been predicted (UC11)
- **Postconditions**: Interactive map is displayed

#### UC15: Filter by Price Range
- **Actor**: User
- **Description**: User filters map data by adjusting price range slider
- **Preconditions**: Interactive map is displayed (UC14)
- **Postconditions**: Map is filtered by price range

## Use Case Relationships

### Include Relationships
- UC2 includes UC1 (Preview requires Upload)
- UC3 includes UC1 (Dataset Info requires Upload)
- UC6, UC7, UC8 include UC1 (Visualizations require Upload)
- UC12, UC13, UC14 include UC11 (Visualizations require Prediction)

### Extend Relationships
- UC9 extends UC6, UC7, UC8 (Download extends Visualizations)
- UC15 extends UC14 (Price Filter extends Map)

### Generalization
- All use cases are initiated by the User actor
- Use cases are grouped into two main modules: Data Analyzer and House Predictor





