# Sentiment Analysis API

A production-ready sentiment analysis system built with FastAPI and multiple NLP approaches including Bag-of-Words (BOW), TF-IDF, and Word2Vec with SVM classification.

## 🚀 Features

- **Multiple NLP Vectorization Techniques**:
  - Bag-of-Words (BOW) with SVM
  - TF-IDF vectorization
  - Custom Word2Vec embeddings
- **RESTful API** with FastAPI for real-time predictions
- **Advanced Text Preprocessing** pipeline
- **Model Versioning** with serialized artifacts
- **Scalable Architecture** following clean code principles

## 📁 Project Structure

```
.
│   main.py                 # FastAPI application entry point
│   requirements.txt        # Python dependencies
│   .env                    # Environment variables (not tracked)
│   .env.example           # Environment variables template
│
├───src
│   │   config.py          # Configuration management
│   │
│   ├───artifacts          # Trained models and vectorizers
│   │       bow_vectorizer.pkl
│   │       svm_bow.pkl
│   │       tfidf_vectorizer.pkl
│   │       w2vec_custom.model
│   │
│   ├───models            # Inference logic and schemas
│   │       inference.py
│   │       schemas.py
│   │
│   ├───notebook          # Development notebooks and datasets
│   │   │   notebook.ipynb
│   │   ├───cleaned-dataset
│   │   └───dataset
│   │
│   └───utils             # Text processing utilities
│           text_processor.py
```

## 🛠️ Technologies Used

### Core Framework
- **FastAPI** - High-performance web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

### Machine Learning & NLP
- **Scikit-learn** - ML algorithms and preprocessing
- **TensorFlow** - Deep learning framework
- **NLTK** - Natural language processing
- **Spacy** - Advanced NLP
- **Gensim** - Word2Vec and topic modeling
- **XGBoost** - Gradient boosting

### Data Processing
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Imbalanced-learn** - Handling imbalanced datasets

### Additional Tools
- **Joblib** - Model serialization
- **WordCloud** - Text visualization
- **TQDM** - Progress bars
- **Pillow** - Image processing

## 📋 Prerequisites

- Python 3.10 or higher
- pip package manager

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/mohamedzahran744/sentiment-analysis-api.git
cd sentiment-analysis-api
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download NLTK data** (if required)
```python
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

5. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

## 🚀 Usage

### Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Example API Request

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "text": "This product is amazing! I love it!"
}

response = requests.post(url, json=data)
print(response.json())
```

Expected Response:
```json
{
    "text": "This product is amazing! I love it!",
    "sentiment": "positive",
    "confidence": 0.95
}
```

## 🧠 Models

The system uses multiple trained models:

1. **SVM with BOW**: Traditional bag-of-words approach with Support Vector Machine
2. **TF-IDF Vectorizer**: Term frequency-inverse document frequency representation
3. **Custom Word2Vec**: Word embeddings trained on domain-specific data

All models are pre-trained and stored in the `src/artifacts/` directory.

## 📊 Dataset

The project uses sentiment analysis datasets stored in:
- `src/notebook/dataset/` - Original raw data
- `src/notebook/cleaned-dataset/` - Preprocessed and cleaned data

## 🔍 Text Processing Pipeline

The text preprocessing pipeline includes:
- Lowercasing
- Tokenization
- Stopword removal
- Special character removal
- Lemmatization/Stemming
- Vectorization (BOW/TF-IDF/Word2Vec)

## 🧪 Development

To work on the Jupyter notebook:

```bash
jupyter notebook src/notebook/notebook.ipynb
```

## 📝 Configuration

Environment variables can be configured in the `.env` file:

```env
# Add your configuration here
MODEL_PATH=src/artifacts/
DEBUG=True
```

## 👨‍💻 Author

**Mohamed Magdy Zahran**
- Machine Learning Engineer | AI & Data Science Specialist
- 📧 Email: mohamedzahran3008@gmail.com
- 💼 LinkedIn: [mohamed-zahran](https://www.linkedin.com/in/mohamed-zahran-b20125312/)
- 🐙 GitHub: [mohamedzahran744](https://github.com/mohamedzahran744)
- 📍 Location: Minufiya, Egypt

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built as part of continuous ML engineering learning journey
- Inspired by production-grade ML system design principles
- Thanks to the open-source community for the amazing tools and libraries

## 📞 Contact

For questions or collaboration opportunities, reach out via:
- Email: mohamedzahran3008@gmail.com
- LinkedIn: [Mohamed Zahran](https://www.linkedin.com/in/mohamed-zahran-b20125312/)

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!