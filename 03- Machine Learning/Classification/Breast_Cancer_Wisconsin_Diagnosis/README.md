# 🏥 Breast Cancer Diagnosis Prediction API

A machine learning-powered REST API for predicting breast cancer diagnosis (Benign vs Malignant) using Logistic Regression. Built with FastAPI and scikit-learn.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Model Information](#model-information)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project provides a production-ready API for breast cancer diagnosis prediction. The model analyzes 10 key features extracted from digitized images of fine needle aspirate (FNA) of breast mass to predict whether a tumor is benign or malignant.

**Key Highlights:**
- ⚡ Fast, async API built with FastAPI
- 🔒 Secure API key authentication
- 🎯 High accuracy Logistic Regression model
- 📊 Returns diagnosis with probability scores
- ✅ Input validation with Pydantic
- 🔄 Consistent preprocessing pipeline

---

## ✨ Features

- **RESTful API** with automatic interactive documentation
- **API Key Authentication** for secure access
- **Input Validation** using Pydantic models
- **CORS Support** for cross-origin requests
- **Error Handling** with descriptive messages
- **Model Persistence** using joblib
- **Probability Scores** for prediction confidence
- **Environment-based Configuration** with `.env` file

---

## 📁 Project Structure
```
breast-cancer-api/
│
├── src/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration and model loading
│   │   ├── inference.py        # Prediction logic
│   │   └── PatiantData.py      # Pydantic data models
│   │
├── models/
│   ├── preprocessor.pkl        # Trained preprocessing pipeline
│   └── log_clf.pkl             # Trained Logistic Regression model
│
├── notebooks/
│   └── training.ipynb          # Model training notebook
│
├── dataset/
│   └── data.csv                # Training dataset
│
├── main.py                     # FastAPI application
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/breast-cancer-api.git
cd breast-cancer-api
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your configuration
```

---

## ⚙️ Configuration

Create a `.env` file in the root directory with the following variables:
```env
# Application Configuration
APP_NAME=Breast Cancer Diagnosis API
VERSION=1.0.0

# Security
API_SECRET_KEY=your-secret-api-key-here-change-this-in-production
```

**⚠️ Security Note:** Always use a strong, unique API key in production. Never commit your `.env` file to version control.

---

## 💻 Usage

### Starting the Server

#### Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at: `http://localhost:8000`

### Interactive Documentation

Once the server is running, visit:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 📖 API Documentation

### Base URL
```
http://localhost:8000
```

### Authentication

All prediction endpoints require an API key in the request header:
```bash
X-API-Key: your-api-key-here
```

---

### Endpoints

#### 1. Health Check

**GET** `/`

Check if the API is running.

**Response:**
```json
{
  "message": "Welcome to Breast Cancer Diagnosis API v1.0.0"
}
```

**Example:**
```bash
curl http://localhost:8000/
```

---

#### 2. Predict Diagnosis

**POST** `/predict/Logistic_clf`

Predict breast cancer diagnosis based on cell nucleus features.

**Headers:**
```
X-API-Key: your-api-key-here
Content-Type: application/json
```

**Request Body:**
```json
{
  "concave_points_worst": 0.2654,
  "perimeter_worst": 184.60,
  "concave_points_mean": 0.1471,
  "radius_worst": 25.38,
  "perimeter_mean": 122.80,
  "area_worst": 2019.0,
  "radius_mean": 17.99,
  "area_mean": 1001.0,
  "concavity_mean": 0.3001,
  "concavity_worst": 0.7119
}
```

**Response:**
```json
{
  "Result": "Malignant",
  "Malignant Probability": 0.9245
}
```

**Example using cURL:**
```bash
curl -X POST http://localhost:8000/predict/Logistic_clf \
  -H "X-API-Key: your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "concave_points_worst": 0.2654,
    "perimeter_worst": 184.60,
    "concave_points_mean": 0.1471,
    "radius_worst": 25.38,
    "perimeter_mean": 122.80,
    "area_worst": 2019.0,
    "radius_mean": 17.99,
    "area_mean": 1001.0,
    "concavity_mean": 0.3001,
    "concavity_worst": 0.7119
  }'
```

**Example using Python:**
```python
import requests

url = "http://localhost:8000/predict/Logistic_clf"
headers = {
    "X-API-Key": "your-api-key-here",
    "Content-Type": "application/json"
}

data = {
    "concave_points_worst": 0.2654,
    "perimeter_worst": 184.60,
    "concave_points_mean": 0.1471,
    "radius_worst": 25.38,
    "perimeter_mean": 122.80,
    "area_worst": 2019.0,
    "radius_mean": 17.99,
    "area_mean": 1001.0,
    "concavity_mean": 0.3001,
    "concavity_worst": 0.7119
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

**Example using JavaScript:**
```javascript
const url = 'http://localhost:8000/predict/Logistic_clf';
const headers = {
  'X-API-Key': 'your-api-key-here',
  'Content-Type': 'application/json'
};

const data = {
  concave_points_worst: 0.2654,
  perimeter_worst: 184.60,
  concave_points_mean: 0.1471,
  radius_worst: 25.38,
  perimeter_mean: 122.80,
  area_worst: 2019.0,
  radius_mean: 17.99,
  area_mean: 1001.0,
  concavity_mean: 0.3001,
  concavity_worst: 0.7119
};

fetch(url, {
  method: 'POST',
  headers: headers,
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

---

### Error Responses

#### 403 Forbidden - Invalid API Key
```json
{
  "detail": "You are not authorized to use this API"
}
```

#### 422 Unprocessable Entity - Invalid Input
```json
{
  "detail": [
    {
      "loc": ["body", "radius_mean"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

#### 500 Internal Server Error
```json
{
  "detail": "Error message describing the issue"
}
```

---

## 🧠 Model Information

### Features Used

The model uses the **top 10 features** most correlated with breast cancer diagnosis:

| Feature | Description |
|---------|-------------|
| `concave_points_worst` | Largest mean of concave portions of cell nucleus contour |
| `perimeter_worst` | Largest perimeter measurement |
| `concave_points_mean` | Mean of concave portions of contour |
| `radius_worst` | Largest radius (distance from center to perimeter) |
| `perimeter_mean` | Mean perimeter measurement |
| `area_worst` | Largest area measurement |
| `radius_mean` | Mean radius measurement |
| `area_mean` | Mean area measurement |
| `concavity_mean` | Mean severity of concave portions |
| `concavity_worst` | Largest concavity measurement |

### Model Performance

- **Algorithm:** Logistic Regression
- **Training Accuracy:** ~96%
- **Testing Accuracy:** ~95%
- **Regularization:** C=1.5
- **Max Iterations:** 1000

### Preprocessing Pipeline

1. **Imputation:** Missing values filled with median
2. **Standardization:** Features scaled using StandardScaler
3. **Feature Selection:** Top 10 correlated features

---

## 🛠️ Development

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest

# Run tests with coverage
pytest --cov=src tests/
```

### Code Formatting
```bash
# Install formatting tools
pip install black isort flake8

# Format code
black .
isort .

# Check code style
flake8 .
```

### Training the Model

To retrain the model with new data:

1. Place your dataset in `dataset/data.csv`
2. Open `notebooks/training.ipynb`
3. Run all cells
4. New models will be saved in `models/` directory

---

## 🐳 Deployment

### Docker Deployment

#### Build Docker Image
```bash
docker build -t breast-cancer-api .
```

#### Run Container
```bash
docker run -d \
  --name breast-cancer-api \
  -p 8000:8000 \
  -e API_SECRET_KEY=your-secret-key \
  breast-cancer-api
```

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - APP_NAME=Breast Cancer Diagnosis API
      - VERSION=1.0.0
      - API_SECRET_KEY=${API_SECRET_KEY}
    volumes:
      - ./models:/app/models
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

---

## 📊 Requirements
```txt
fastapi==0.121.2
uvicorn==0.38.0
scikit-learn==1.7.2
xgboost==3.1.1
imbalanced-learn==0.14.0
python-dotenv==1.2.1
python-multipart==0.0.20
matplotlib==3.10.7
seaborn==0.13.2
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards

- Follow PEP 8 style guide
- Add docstrings to all functions
- Write unit tests for new features
- Update documentation as needed

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Dataset: [Wisconsin Breast Cancer Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
- FastAPI framework by Sebastián Ramírez
- scikit-learn for machine learning tools

---

## 📧 Contact

**Your Name**
- Email: mohamedzahran3008@gmail.com
- GitHub: [@Mohamed_Zahran](https://github.com/mohamedzahran744)
- LinkedIn: [Mohamed Zahran](https://www.linkedin.com/in/mohamed-zahran-b20125312/)

**Project Link:** [https://github.com/mohamedzahran744/breast-cancer-api](https://github.com/mohamedzahran744/breast-cancer-api)

---

## ⚠️ Disclaimer

**This application is for educational and research purposes only. It should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical decisions.**

---

## 🗺️ Roadmap

- [ ] Add more ML models (Random Forest, XGBoost)
- [ ] Implement model versioning
- [ ] Add comprehensive logging
- [ ] Create unit and integration tests
- [ ] Add rate limiting
- [ ] Implement monitoring and metrics
- [ ] Add user authentication system
- [ ] Create frontend dashboard
- [ ] Deploy to cloud platform (AWS/GCP/Azure)

---

## 📈 Version History

- **v1.0.0** (2024-12-08)
  - Initial release
  - Logistic Regression model
  - API key authentication
  - Basic prediction endpoint

---

Made with ❤️ and ☕