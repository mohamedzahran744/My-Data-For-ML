# My-Data-For-ML
# Customer Churn Prediction System

A machine learning-based system for predicting customer churn using ensemble methods (Random Forest and XGBoost). This project provides a complete pipeline from data preprocessing to model inference.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Model Details](#model-details)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This system predicts customer churn probability using trained machine learning models. It includes:
- Pre-trained Random Forest and XGBoost models
- Data preprocessing pipeline
- Easy-to-use inference interface
- Configurable settings via environment variables

## Project Structure

```
.
├── .env                      # Environment variables (not tracked)
├── .env.example             # Example environment configuration
├── .gitignore               # Git ignore rules
├── main.py                  # Main application entry point
├── README.md                # Project documentation
├── Requirements.txt         # Python dependencies
├── t.ipynb                  # Testing notebook
│
├── dataset/
│   └── churn-data.csv       # Training/testing dataset
│
├── models/
│   ├── forest_tuned.pkl     # Trained Random Forest model
│   ├── preprocessor.pkl     # Data preprocessing pipeline
│   └── xgb-tuned.pkl        # Trained XGBoost model
│
├── notebooks/
│   └── notebook.ipynb       # Exploratory data analysis & training
│
└── utils/
    ├── __init__.py          # Package initializer
    ├── config.py            # Configuration management
    ├── CustomerData.py      # Customer data model/schema
    └── inference.py         # Model inference functions
```

## Features

- **Multiple Models**: Ensemble approach using Random Forest and XGBoost
- **Preprocessing Pipeline**: Automated data transformation and feature engineering
- **Modular Design**: Separated concerns with utility modules
- **Configuration Management**: Environment-based configuration
- **Easy Inference**: Simple API for making predictions
- **Jupyter Notebooks**: Interactive exploration and model training

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r Requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env with your configuration
   ```

## Configuration

Create a `.env` file in the root directory based on `.env.example`:

```env
# Model Configuration
MODEL_PATH=models/
PREPROCESSOR_PATH=models/preprocessor.pkl
RANDOM_FOREST_PATH=models/forest_tuned.pkl
XGBOOST_PATH=models/xgb-tuned.pkl

# Data Configuration
DATA_PATH=dataset/churn-data.csv

# Application Settings
DEBUG=False
LOG_LEVEL=INFO
```

## Usage

### Running the Main Application

```bash
python main.py
```

### Making Predictions

```python
from utils.inference import predict_churn
from utils.CustomerData import CustomerData

# Create customer data instance
customer = CustomerData(
    tenure=24,
    monthly_charges=70.50,
    total_charges=1692.00,
    # ... other features
)

# Get prediction
prediction = predict_churn(customer)
print(f"Churn Probability: {prediction['probability']:.2%}")
print(f"Prediction: {'Will Churn' if prediction['churn'] else 'Will Stay'}")
```

### Using Jupyter Notebooks

```bash
# Start Jupyter
jupyter notebook

# Open notebooks/notebook.ipynb for model training
# Open t.ipynb for testing
```

## Model Details

### Random Forest Classifier
- **File**: `models/forest_tuned.pkl`
- **Type**: Ensemble decision tree classifier
- **Features**: Hyperparameter tuned for optimal performance

### XGBoost Classifier
- **File**: `models/xgb-tuned.pkl`
- **Type**: Gradient boosting classifier
- **Features**: Optimized with grid search

### Preprocessor
- **File**: `models/preprocessor.pkl`
- **Features**: 
  - Handles missing values
  - Encodes categorical variables
  - Scales numerical features
  - Feature engineering transformations

## Development

### Project Modules

#### `utils/config.py`
Configuration management and environment variable loading.

#### `utils/CustomerData.py`
Data model defining customer attributes and validation.

#### `utils/inference.py`
Core prediction functions and model loading utilities.

### Adding New Features

1. Update `CustomerData.py` with new fields
2. Retrain models in `notebooks/notebook.ipynb`
3. Update preprocessing pipeline if needed
4. Save new models to `models/` directory

### Running Tests

```bash
# Run test notebook
jupyter notebook t.ipynb
```

## Dataset

The `churn-data.csv` file contains customer information including:
- Demographics
- Account information
- Service usage
- Billing details
- Churn status (target variable)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

### Common Issues

**Import Errors**
```bash
# Ensure all dependencies are installed
pip install -r Requirements.txt
```

**Model Loading Errors**
```bash
# Check that model files exist
ls models/*.pkl
```

**Environment Variable Issues**
```bash
# Verify .env file exists and is properly formatted
cat .env
```

## Contact

For questions or support, please open an issue in the repository.

---

**Note**: Remember to never commit your `.env` file or any sensitive credentials to version control.