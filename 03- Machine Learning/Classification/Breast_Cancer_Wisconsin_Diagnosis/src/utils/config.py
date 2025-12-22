# Import required libraries
from dotenv import load_dotenv  # Load environment variables from .env file
import os  # Operating system interface for file paths and environment variables
import joblib  # Library for loading serialized machine learning models


# Load environment variables from .env file
# override=True ensures that .env values take precedence over existing environment variables
load_dotenv(override=True)


# Retrieve application configuration from environment variables
# These values are stored in .env file for security and easy configuration management
APP_NAME = os.getenv("APP_NAME")  # Application name for identification
VERSION = os.getenv("VERSION")  # Current version of the application
API_SECRET_KEY = os.getenv("API_SECRET_KEY")  # Secret key for API authentication/security


# Construct the base directory path
# __file__ is the current script's path
# os.path.abspath() converts to absolute path
# os.path.dirname() gets the parent directory (called twice to go up two levels)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the models folder where trained models are stored
MODELS_FOLDER_PATH = os.path.join(BASE_DIR, 'models')



# Load the saved preprocessor object from disk
# This contains the fitted scaler and imputer with learned statistics from training
preprocessor = joblib.load(os.path.join(MODELS_FOLDER_PATH, 'preprocessor.pkl'))

# Load the trained Logistic Regression model from disk
# This is the model that will make predictions on new data
log_clf_model = joblib.load(os.path.join(MODELS_FOLDER_PATH, 'log_clf.pkl'))