import os
from dotenv import load_dotenv
import joblib
import tensorflow as tf

# load .env file
load_dotenv(override=True)

APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

SRC_FOLDER_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# 
preprocessor = joblib.load(
    os.path.join(SRC_FOLDER_PATH, "src", "artifacts", "preprocessor.joblib")
)

# 
model = tf.keras.models.load_model(
    os.path.join(SRC_FOLDER_PATH, "src", "artifacts", "best_titanic_model.keras")
)
