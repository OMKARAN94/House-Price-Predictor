# Project Diagrams Documentation

This directory contains comprehensive diagrams for the **House Price Prediction Project** by Alpha Analytics.

## 📊 Available Diagrams

### 1. **Class Diagram** (`class_diagram.md`)
Shows the module structure, classes, and relationships between components:
- Main Application (`app.py`)
- Data Analyzer Module
- House Predictor Module
- Machine Learning Model
- Data Processing Components
- Visualization Components
- Data Storage Structure

### 2. **ER Diagram** (`er_diagram.md`)
Entity-Relationship diagram showing the data model:
- **HOUSE** entity (main entity)
- **LOCATION** entity
- Relationships between entities
- Attribute details and data types
- Feature engineering structure

### 3. **Flow Diagram** (`flow_diagram.md`)
Comprehensive flow diagrams including:
- **Application Flow**: User journey through the application
- **ML Pipeline Flow**: Model training and deployment process
- **Data Processing Flow**: Data cleaning and preprocessing steps
- **Prediction Flow**: Sequence diagram of prediction process
- **System Architecture Flow**: Overall system architecture

### 4. **Use Case Diagram** (`use_case_diagram.md`)
UML-style use case diagrams showing:
- **Actors**: User interactions with the system
- **Use Cases**: All functional requirements
  - Data Analyzer use cases (9 use cases)
  - House Predictor use cases (6 use cases)
- **Relationships**: Include, extend, and generalization relationships
- **Detailed Descriptions**: Preconditions, postconditions, and main flows for each use case

### 5. **Activity Diagram** (`activity_diagram.md`)
Detailed activity diagrams showing:
- **Data Analyzer Workflow**: Complete process from file upload to data export
- **House Price Prediction Workflow**: End-to-end prediction process
- **Complete Application Flow**: Overall system workflow
- **ML Model Training Process**: Model development pipeline
- **Data Processing Pipeline**: Data transformation activities
- **Prediction Process**: Detailed prediction activities
- **User Interaction Flow**: State-based user interactions
- **Error Handling Flow**: Error management activities

## 🎯 Project Overview

### Project Structure
```
Prise_prediction_project/
├── app.py                          # Main application entry point
├── pages/
│   ├── 1_Data_Analyzer.py         # Data analysis and cleaning tool
│   └── 2_House_Predictor.py       # House price prediction tool
├── models/
│   └── House_prediction_model.pkl  # Trained ML model
├── cleaned_data.csv                # Processed house data
├── Bengaluru_House_Data.csv        # Raw house data
└── diagrams/                       # This directory
```

### Key Features

1. **Data Analyzer Tool**
   - Upload CSV/Excel files
   - Automatic data cleaning
   - Multiple visualization options
   - Export cleaned data

2. **House Price Predictor**
   - ML-based price prediction
   - Interactive visualizations
   - Geographic map visualization
   - Real-time price estimation

### Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (Linear Regression)
- **Visualization**: Matplotlib, Plotly
- **Model Storage**: Pickle

### Machine Learning Model

- **Algorithm**: Linear Regression
- **Preprocessing**:
  - OneHotEncoder for location (categorical)
  - StandardScaler for numeric features
- **Features**: location, total_sqft, bath, balcony, bedrooms
- **Target**: price (in Lakhs ₹)
- **Performance**: R² Score ≈ 0.695

## 📖 How to View Diagrams

### Option 1: GitHub/GitLab
These Mermaid diagrams will render automatically on GitHub/GitLab when viewing the markdown files.

### Option 2: VS Code
Install the "Markdown Preview Mermaid Support" extension to view diagrams in VS Code.

### Option 3: Online Mermaid Editor
1. Copy the Mermaid code from any diagram file
2. Paste it into [Mermaid Live Editor](https://mermaid.live/)
3. View and export as PNG/SVG

### Option 4: Mermaid CLI
```bash
npm install -g @mermaid-js/mermaid-cli
mmdc -i diagrams/class_diagram.md -o diagrams/class_diagram.png
```

## 🔍 Diagram Details

### Class Diagram
- Shows module dependencies
- Illustrates function relationships
- Displays data flow between components

### ER Diagram
- Defines data entities and attributes
- Shows relationships (1:1, 1:Many)
- Includes data types and constraints

### Flow Diagram
- Application user flow
- ML model training pipeline
- Data processing workflow
- Prediction sequence
- System architecture

### Use Case Diagram
- User (actor) interactions
- 15 total use cases across both modules
- Include and extend relationships
- Detailed use case specifications

### Activity Diagram
- Step-by-step activity flows
- Decision points and branching logic
- Parallel activities
- Error handling workflows
- State transitions

## 📝 Notes

- All diagrams use **Mermaid** syntax for easy rendering
- Diagrams are version-controlled and can be updated as the project evolves
- ER diagram represents the logical data model (not a physical database)
- Flow diagrams show both user-facing and backend processes

## 🤝 Contributing

When updating diagrams:
1. Maintain Mermaid syntax standards
2. Keep diagrams synchronized with code changes
3. Update this README if adding new diagram types

---

**Created by**: Omkaran & Team  
**Organization**: Alpha Analytics  
**Copyright**: © 2025 Alpha Analytics

