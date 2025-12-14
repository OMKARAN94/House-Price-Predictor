# Activity Diagram - House Price Prediction Project

## Activity Diagram: Data Analyzer Workflow

```mermaid
flowchart TD
    Start([Start: User Opens Data Analyzer]) --> Upload[Upload CSV/Excel File]
    Upload --> Validate{File Valid?}
    Validate -->|No| Error[Display Error Message]
    Error --> Upload
    Validate -->|Yes| ReadData[Read Data into DataFrame]
    ReadData --> Preview[Display Data Preview<br/>First 5 Rows]
    Preview --> ShowInfo[Display Dataset Information<br/>- Column Types<br/>- Summary Statistics<br/>- Missing Values<br/>- Duplicates]
    ShowInfo --> UserChoice{User Action?}
    
    UserChoice -->|Clean Data| CleanOptions[Select Cleaning Options]
    UserChoice -->|Visualize| VizOptions[Select Visualization Type]
    UserChoice -->|Download| DownloadData[Download Cleaned Data]
    
    CleanOptions --> RemoveDup{Remove Duplicates?}
    RemoveDup -->|Yes| DropDup[Drop Duplicate Rows]
    RemoveDup -->|No| HandleMissing
    DropDup --> HandleMissing[Select Missing Value Strategy]
    
    HandleMissing --> NumStrategy{Strategy for Numeric?}
    NumStrategy -->|Mean| FillMean[Fill with Mean]
    NumStrategy -->|Median| FillMedian[Fill with Median]
    NumStrategy -->|Drop| DropRows[Drop Rows]
    NumStrategy -->|Nothing| CatStrategy
    
    FillMean --> CatStrategy
    FillMedian --> CatStrategy
    DropRows --> CatStrategy
    
    CatStrategy{Strategy for Categorical?}
    CatStrategy -->|Mode| FillMode[Fill with Mode]
    CatStrategy -->|Drop| DropRows
    CatStrategy -->|Nothing| ApplyClean
    FillMode --> ApplyClean[Apply Cleaning]
    
    ApplyClean --> CleanedData[Data Cleaned Successfully]
    CleanedData --> UserChoice
    
    VizOptions --> VizType{Visualization Type?}
    VizType -->|Pie Chart| SelectCat[Select Categorical Column]
    VizType -->|Bar Chart| SelectNum[Select Numeric Column]
    VizType -->|Heatmap| CreateHeatmap[Create Correlation Heatmap]
    
    SelectCat --> CreatePie[Create Pie Chart]
    SelectNum --> ChartType{Chart Type?}
    ChartType -->|Histogram| CreateHist[Create Histogram]
    ChartType -->|Bar by Category| SelectGroup[Select Grouping Column]
    SelectGroup --> CreateBar[Create Bar Chart]
    
    CreatePie --> DisplayViz[Display Visualization]
    CreateHist --> DisplayViz
    CreateBar --> DisplayViz
    CreateHeatmap --> DisplayViz
    
    DisplayViz --> UserChoice
    
    DownloadData --> ExportCSV[Export as CSV]
    ExportCSV --> End([End])
    
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style Error fill:#FF6B6B
    style CleanedData fill:#87CEEB
```

## Activity Diagram: House Price Prediction Workflow

```mermaid
flowchart TD
    Start([Start: User Opens House Predictor]) --> LoadModel[Load ML Model<br/>from pickle file]
    LoadModel --> LoadData[Load House Data<br/>from CSV]
    LoadData --> CheckCoords{Coordinates Exist?}
    CheckCoords -->|No| GenerateCoords[Generate Synthetic Coordinates<br/>latitude & longitude]
    CheckCoords -->|Yes| GetInput
    GenerateCoords --> GetInput[Get User Input<br/>- Location<br/>- Total Sqft<br/>- Bedrooms<br/>- Bathrooms<br/>- Balconies]
    
    GetInput --> ValidateInput{Input Valid?}
    ValidateInput -->|No| ShowError[Display Validation Error]
    ShowError --> GetInput
    ValidateInput -->|Yes| ClickPredict{User Clicks<br/>Predict Button?}
    ClickPredict -->|No| GetInput
    ClickPredict -->|Yes| Preprocess[Preprocess Input Data<br/>- OneHotEncode Location<br/>- Standard Scale Features]
    
    Preprocess --> Predict[Run ML Model<br/>model.predict]
    Predict --> CalculatePrice[Calculate Price in Rupees<br/>prediction * 100000]
    CalculatePrice --> DisplayPrice[Display Predicted Price<br/>Format: ₹ X,XXX.XX]
    DisplayPrice --> ShowBalloons[Show Celebration Animation]
    
    ShowBalloons --> FilterLocation[Filter Data by Selected Location]
    FilterLocation --> CreateViz[Create Visualizations]
    
    CreateViz --> ScatterPlot[Create Scatter Plot<br/>Price vs Sqft]
    CreateViz --> BarChart[Create Bar Chart<br/>Avg Price by Bedrooms]
    CreateViz --> PriceSlider[Display Price Range Slider]
    
    ScatterPlot --> DisplayScatter[Display Scatter Plot]
    BarChart --> DisplayBar[Display Bar Chart]
    PriceSlider --> UserAdjust{User Adjusts Slider?}
    
    UserAdjust -->|Yes| FilterPrice[Filter Data by Price Range]
    UserAdjust -->|No| CreateMap
    FilterPrice --> CreateMap[Create Interactive Map<br/>Plotly Scatter Mapbox]
    CreateMap --> DisplayMap[Display Interactive Map]
    
    DisplayScatter --> End
    DisplayBar --> End
    DisplayMap --> End([End])
    
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style ShowError fill:#FF6B6B
    style DisplayPrice fill:#87CEEB
    style ShowBalloons fill:#FFD700
```

## Activity Diagram: Complete Application Flow

```mermaid
flowchart TD
    Start([User Opens Application]) --> MainPage[Display Main Page<br/>Welcome Message]
    MainPage --> SelectTool{Select Tool}
    
    SelectTool -->|Data Analyzer| DataAnalyzerFlow[Data Analyzer Module]
    SelectTool -->|House Predictor| HousePredictorFlow[House Predictor Module]
    
    subgraph DataAnalyzerFlow["📊 Data Analyzer Activities"]
        DA1[Upload File] --> DA2[Read & Validate]
        DA2 --> DA3[Preview Data]
        DA3 --> DA4[Show Dataset Info]
        DA4 --> DA5{User Action}
        DA5 -->|Clean| DA6[Clean Data]
        DA5 -->|Visualize| DA7[Create Visualizations]
        DA5 -->|Download| DA8[Export CSV]
        DA6 --> DA5
        DA7 --> DA5
        DA8 --> DAEnd([End])
    end
    
    subgraph HousePredictorFlow["🏡 House Predictor Activities"]
        HP1[Load Model & Data] --> HP2[Get User Input]
        HP2 --> HP3[Validate Input]
        HP3 --> HP4[Preprocess Data]
        HP4 --> HP5[Make Prediction]
        HP5 --> HP6[Display Results]
        HP6 --> HP7[Create Visualizations]
        HP7 --> HP8[Display Map]
        HP8 --> HPEnd([End])
    end
    
    DataAnalyzerFlow --> MainPage
    HousePredictorFlow --> MainPage
    MainPage --> End([End])
    
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style MainPage fill:#87CEEB
```

## Activity Diagram: Machine Learning Model Training Process

```mermaid
flowchart TD
    Start([Start: Model Training]) --> LoadRawData[Load Raw Data<br/>Bengaluru_House_Data.csv]
    LoadRawData --> CleanData[Data Cleaning<br/>- Remove duplicates<br/>- Handle missing values]
    CleanData --> FeatureExtract[Feature Engineering<br/>- Extract bedrooms from size<br/>- Normalize total_sqft]
    FeatureExtract --> SelectFeatures[Select Features<br/>location, total_sqft,<br/>bath, balcony, bedrooms]
    SelectFeatures --> SplitData[Train-Test Split<br/>train_test_split]
    
    SplitData --> TrainSet[Training Set]
    SplitData --> TestSet[Test Set]
    
    TrainSet --> BuildPipeline[Build ML Pipeline<br/>- ColumnTransformer<br/>- OneHotEncoder<br/>- StandardScaler<br/>- LinearRegression]
    BuildPipeline --> TrainModel[Train Model<br/>model.fit]
    TrainModel --> Evaluate[Evaluate Model<br/>model.score]
    
    TestSet --> Evaluate
    Evaluate --> CheckScore{Score Acceptable?}
    CheckScore -->|No| TuneModel[Hyperparameter Tuning]
    TuneModel --> TrainModel
    CheckScore -->|Yes| SaveModel[Save Model<br/>pickle.dump]
    SaveModel --> SaveData[Save Cleaned Data<br/>cleaned_data.csv]
    SaveData --> End([End: Model Ready])
    
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style CheckScore fill:#FFD700
    style SaveModel fill:#87CEEB
```

## Activity Diagram: Data Processing Pipeline

```mermaid
flowchart LR
    Start([Input Data]) --> CheckFormat{File Format?}
    CheckFormat -->|CSV| ReadCSV[pandas.read_csv]
    CheckFormat -->|Excel| ReadExcel[pandas.read_excel]
    
    ReadCSV --> Analyze[Analyze Structure]
    ReadExcel --> Analyze
    
    Analyze --> IdentifyTypes[Identify Column Types<br/>Numeric vs Categorical]
    IdentifyTypes --> CheckQuality[Check Data Quality<br/>- Missing values<br/>- Duplicates<br/>- Outliers]
    
    CheckQuality --> Clean[Apply Cleaning<br/>- Fill missing<br/>- Remove duplicates<br/>- Handle outliers]
    Clean --> Transform[Transform Data<br/>- Encode categorical<br/>- Scale numeric]
    Transform --> Validate[Validate Cleaned Data]
    Validate --> Export[Export Cleaned Data]
    Export --> End([Output Data])
    
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style Clean fill:#87CEEB
    style Transform fill:#FFD700
```

## Activity Diagram: Prediction Process (Detailed)

```mermaid
flowchart TD
    Start([User Input Received]) --> CollectInput[Collect Input Features<br/>location, sqft, beds, bath, balc]
    CollectInput --> LoadModel[Load Trained Model<br/>pickle.load]
    LoadModel --> LoadRefData[Load Reference Data<br/>for visualization]
    
    CollectInput --> PrepareInput[Prepare Input DataFrame<br/>columns: location, total_sqft,<br/>bath, balcony, bedrooms]
    PrepareInput --> EncodeLocation[OneHotEncode Location<br/>ColumnTransformer]
    EncodeLocation --> ScaleFeatures[Standard Scale Features<br/>StandardScaler]
    ScaleFeatures --> Predict[Run Prediction<br/>LinearRegression.predict]
    
    Predict --> FormatResult[Format Result<br/>Convert to Rupees<br/>prediction * 100000]
    FormatResult --> DisplayResult[Display to User<br/>₹ X,XXX.XX]
    
    LoadRefData --> FilterByLocation[Filter by Selected Location]
    FilterByLocation --> CreateCharts[Create Charts<br/>- Scatter Plot<br/>- Bar Chart]
    CreateCharts --> CreateMap[Create Map Visualization]
    CreateMap --> DisplayAll[Display All Visualizations]
    
    DisplayResult --> DisplayAll
    DisplayAll --> End([End])
    
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style Predict fill:#FFD700
    style DisplayResult fill:#87CEEB
```

## Activity Diagram: User Interaction Flow

```mermaid
stateDiagram-v2
    [*] --> MainPage
    MainPage --> DataAnalyzer: Select Data Analyzer
    MainPage --> HousePredictor: Select House Predictor
    
    state DataAnalyzer {
        [*] --> UploadFile
        UploadFile --> ViewData: File Uploaded
        ViewData --> CleanData: User Chooses
        ViewData --> Visualize: User Chooses
        ViewData --> Download: User Chooses
        CleanData --> Visualize: After Cleaning
        Visualize --> Download: After Visualization
        Download --> [*]
    }
    
    state HousePredictor {
        [*] --> EnterDetails
        EnterDetails --> Predict: Click Predict
        Predict --> ViewResults: Prediction Complete
        ViewResults --> ViewCharts: View Charts
        ViewResults --> ViewMap: View Map
        ViewCharts --> ViewMap: Continue
        ViewMap --> FilterMap: Adjust Slider
        FilterMap --> ViewMap: Map Updated
        ViewMap --> [*]
    }
    
    DataAnalyzer --> MainPage: Return to Main
    HousePredictor --> MainPage: Return to Main
    MainPage --> [*]: Close Application
```

## Activity Diagram: Error Handling Flow

```mermaid
flowchart TD
    Start([Operation Starts]) --> TryOperation[Execute Operation]
    TryOperation --> CheckError{Error Occurred?}
    
    CheckError -->|No| Success[Operation Successful]
    CheckError -->|Yes| CatchError[Catch Exception]
    
    CatchError --> IdentifyError{Error Type?}
    
    IdentifyError -->|File Error| FileError[Display File Error<br/>Invalid format or<br/>File not found]
    IdentifyError -->|Data Error| DataError[Display Data Error<br/>Invalid data format or<br/>Missing required columns]
    IdentifyError -->|Model Error| ModelError[Display Model Error<br/>Model not found or<br/>Invalid input shape]
    IdentifyError -->|Validation Error| ValidationError[Display Validation Error<br/>Invalid input values]
    IdentifyError -->|Other Error| GenericError[Display Generic Error<br/>Unexpected error occurred]
    
    FileError --> LogError[Log Error Details]
    DataError --> LogError
    ModelError --> LogError
    ValidationError --> LogError
    GenericError --> LogError
    
    LogError --> ShowMessage[Show User-Friendly Message]
    ShowMessage --> AllowRetry{Allow Retry?}
    
    AllowRetry -->|Yes| RetryOperation[Return to Operation]
    AllowRetry -->|No| EndError([End with Error])
    
    RetryOperation --> TryOperation
    Success --> EndSuccess([End Successfully])
    
    style Start fill:#90EE90
    style EndSuccess fill:#90EE90
    style EndError fill:#FF6B6B
    style CatchError fill:#FFB6C1
    style LogError fill:#FFD700
```

## Activity Diagram Notes

### Key Activities

1. **Data Analyzer Activities**:
   - File upload and validation
   - Data preview and analysis
   - Data cleaning operations
   - Visualization creation
   - Data export

2. **House Predictor Activities**:
   - Model and data loading
   - User input collection
   - Data preprocessing
   - Price prediction
   - Result visualization

3. **Common Activities**:
   - Error handling
   - User validation
   - Data transformation
   - Visualization rendering

### Decision Points

- File validation checks
- User action selections
- Data quality checks
- Model performance evaluation
- Input validation

### Parallel Activities

- Multiple visualizations can be created simultaneously
- Data loading and model loading can occur in parallel
- Chart creation and map creation are independent

### Swimlanes

The activities can be organized into swimlanes:
- **User Interface Layer**: User interactions
- **Application Layer**: Business logic
- **Processing Layer**: Data processing
- **ML Layer**: Model operations
- **Storage Layer**: Data persistence





