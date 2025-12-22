# Regression Project: Housing Price Prediction

## Overview
This project implements a **Machine Learning Regression pipeline** to predict housing prices using various algorithms.  
It covers data preprocessing, feature engineering, model training, evaluation, and deployment with **Flask**.

The project includes classical ML models, ensemble methods, and XGBoost, with hyperparameter tuning to achieve better performance.

---

## Project Structure

C:.
│ .gitignore
│ Read-Me.md
│ Requirements.txt
│
├───dataset
│ housing.csv
│
├───model
│ model_XGBoost.pkl
│
├───Notebooks
│ notebook.ipynb
│
├───static
│ │ models_comapre.png
│ │ Zahran.jpg
│ │
│ └───css
│ main.css
│
├───templates
│ about.html
│ base.html
│ index.html
│ predict.html
│
└───utils
│ router.py
│ utils.py
│
└───pycache
utils.cpython-310.pyc

markdown
Copy code

---

## Features
- Predict housing prices using multiple regression algorithms:
  - Linear Regression
  - SGD Regressor
  - Ridge Regression
  - Polynomial Regression
  - KNN Regressor
  - Random Forest
  - XGBoost
  - Voting Regressor (ensemble of tuned Random Forest & XGBoost)

- **Feature Engineering**:
  - Numerical and Categorical features preprocessing
  - One-Hot Encoding and Label Encoding
  - Handling missing values

- **Model Evaluation**:
  - RMSE (Root Mean Squared Error) using `cross_val_score`
  - Cross-validated predictions using `cross_val_predict`
  - Feature importance analysis

- **Deployment**:
  - Flask-based web application
  - Interactive UI for predicting new data
  - HTML templates with static CSS styling

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/Regression_Project.git
cd Regression_Project
Create a virtual environment (recommended):

bash
Copy code
conda create -n zahran python=3.10
conda activate zahran
Install required packages:

bash
Copy code
pip install -r Requirements.txt
Usage
Jupyter Notebook: Explore data, train models, and evaluate performance:

bash
Copy code
jupyter notebook Notebooks/notebook.ipynb
Flask Application:

bash
Copy code
python utils/router.py
Open browser and go to: http://127.0.0.1:5000

Use the interface to predict housing prices.

File Description
dataset/housing.csv: Dataset used for training and evaluation

model/model_XGBoost.pkl: Saved XGBoost model

Notebooks/notebook.ipynb: Jupyter notebook with complete ML workflow

utils/router.py: Flask routes for web app

utils/utils.py: Utility functions for data processing and ML

templates/: HTML templates for the web interface

static/: Static assets (images, CSS)

Requirements.txt: Python dependencies

Author
Mohamed Zahran
Junior Machine Learning Engineer
LinkedIn

Specialized in: Machine Learning, Deep Learning, NLP, AI applications, and ML pipelines.

License
This project is open-source and available under the MIT License.