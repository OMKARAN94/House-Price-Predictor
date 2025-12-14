# ER Diagram - House Price Prediction Project

```mermaid
erDiagram
    HOUSE ||--o{ LOCATION : located_in
    HOUSE ||--|| FEATURES : has
    HOUSE ||--|| PRICE : priced_as

    HOUSE {
        int house_id PK
        string location FK
        float total_sqft
        int bedrooms
        float bath
        float balcony
        float price
    }

    LOCATION {
        string location_name PK
        string area_type
    }

    FEATURES {
        int bedrooms
        float bath
        float balcony
        float total_sqft
    }

    PRICE {
        float price_value PK
        string currency
    }
```

## Entity Descriptions

### HOUSE (Main Entity)
- **Primary Key:** house_id (implicit index)
- **Attributes:**
  - `location` (string): Location name in Bangalore
  - `total_sqft` (float): Total square footage of the house
  - `bedrooms` (int): Number of bedrooms
  - `bath` (float): Number of bathrooms
  - `balcony` (float): Number of balconies
  - `price` (float): Price in Lakhs (₹)

### LOCATION
- **Primary Key:** location_name
- **Attributes:** area_type (Super built-up, Plot, Built-up, etc.)

### Relationships
- **HOUSE → LOCATION:** Many houses share one location.
- **HOUSE → FEATURES:** Feature set belongs to a house record.
- **HOUSE → PRICE:** Each house has one price entry.

## Data Model Structure

### CSV Schema (cleaned_data.csv)
```
location, total_sqft, bath, balcony, price, bedrooms
```

### Feature Engineering
- **Categorical:** location (One-Hot Encoded)
- **Numerical:** total_sqft, bath, balcony, bedrooms (Standard Scaled)
- **Target:** price (in Lakhs ₹)





