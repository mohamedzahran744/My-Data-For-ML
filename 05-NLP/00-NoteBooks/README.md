# 📚 Natural Language Processing (NLP) Fundamentals

A comprehensive collection of Jupyter notebooks covering fundamental NLP concepts, techniques, and practical implementations using Python.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![NLTK](https://img.shields.io/badge/NLTK-3.8.1-orange.svg)](https://www.nltk.org/)
[![spaCy](https://img.shields.io/badge/spaCy-3.7.2-brightgreen.svg)](https://spacy.io/)

---

## 📖 Overview

This repository contains hands-on tutorials for learning Natural Language Processing from scratch. Each notebook is self-contained with theory, code examples, and practical exercises covering essential NLP techniques used in real-world applications.

**Perfect for:**
- 🎓 Students learning NLP
- 👨‍💻 Data scientists transitioning to NLP
- 🔬 Researchers exploring text processing
- 🚀 Practitioners building NLP applications

---

## 📂 Repository Structure

```
nlp-fundamentals/
│
├── 00-Regex.ipynb                    # Regular Expressions for Text
├── 01-Edit-Distance.ipynb            # Text Similarity Metrics
├── 02-Text-Normalization.ipynb       # Stemming & Lemmatization
├── 03-Feature-Extraction.ipynb       # BOW, TF-IDF, Text Classification
├── 04-NLP-NLTK-spaCy-intro.ipynb    # Tokenization, POS, NER
│
├── requirements.txt                   # Python dependencies
└── README.md                         # This file
```

---

## 📓 Notebook Contents

### [00 - Regular Expressions](00-Regex.ipynb)
**Duration:** ~45 minutes | **Difficulty:** ⭐⭐

Learn to search, match, and manipulate text using powerful regex patterns.

**Topics Covered:**
- Basic regex patterns and special characters
- Character classes and ranges `[a-z]`, `[0-9]`
- Quantifiers `*`, `+`, `?`, `{n,m}`
- Groups and capture `(pattern)`
- Practical examples: email extraction, hashtag detection, phone number validation

**Key Libraries:** `re`

---

### [01 - Edit Distance](01-Edit-Distance.ipynb)
**Duration:** ~30 minutes | **Difficulty:** ⭐⭐

Understand text similarity using distance metrics for spell checking and fuzzy matching.

**Topics Covered:**
- Levenshtein Distance (insertions, deletions, substitutions)
- Hamming Distance (equal-length strings)
- Damerau-Levenshtein Distance (transpositions)
- Applications: spell checkers, autocomplete, duplicate detection

**Key Libraries:** `jellyfish`

---

### [02 - Text Normalization](02-Text-Normalization.ipynb)
**Duration:** ~1 hour | **Difficulty:** ⭐⭐⭐

Transform text into standardized forms to improve NLP model performance.

**Topics Covered:**
- Lowercasing and punctuation removal
- Stemming (Porter, Snowball, Lancaster)
- Lemmatization with WordNet
- Stop word removal strategies
- Trade-offs: over-normalization vs under-normalization
- Multi-language support (Arabic stemming example)

**Key Libraries:** `nltk.stem`, `WordNetLemmatizer`

---

### [03 - Feature Extraction](03-Feature-Extraction.ipynb) ⭐ **Most Practical**
**Duration:** ~1.5 hours | **Difficulty:** ⭐⭐⭐

Convert text into numerical features for machine learning models.

**Topics Covered:**
- Bag of Words (BOW) representation
- N-grams for context capture
- TF-IDF weighting
- Stop words filtering
- Feature selection with `max_df` and `min_df`
- **Real Classification Project:** 20newsgroups dataset
- Distance metrics comparison: Cosine, Euclidean, Dot Product
- **Result:** 80.19% accuracy on news classification

**Key Libraries:** `sklearn.feature_extraction.text`, `CountVectorizer`, `TfidfVectorizer`

---

### [04 - NLTK & spaCy Introduction](04-NLP-NLTK-spaCy-intro.ipynb)
**Duration:** ~1 hour | **Difficulty:** ⭐⭐⭐

Master essential NLP preprocessing with two leading Python libraries.

**Topics Covered:**
- **Tokenization:** Sentence and word splitting
- **Stemming:** Porter vs Snowball vs Lancaster
- **Lemmatization:** WordNet-based normalization
- **Part-of-Speech (POS) Tagging:** Identifying word roles
- **Named Entity Recognition (NER):** Extracting people, organizations, locations
- **Library Comparison:** When to use NLTK vs spaCy
- Interactive NER visualization with displacy

**Key Libraries:** `nltk`, `spacy`, `displacy`

---

## 🚀 Quick Start

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/nlp-fundamentals.git
cd nlp-fundamentals
```

### 2️⃣ Create Virtual Environment
```bash
# Using venv
python -m venv nlp_env
source nlp_env/bin/activate  # macOS/Linux
nlp_env\Scripts\activate     # Windows

# OR using conda
conda create -n nlp_env python=3.10
conda activate nlp_env
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download Models & Data
```bash
python setup.py
```

This automatically downloads:
- ✅ NLTK corpora (punkt, stopwords, wordnet)
- ✅ spaCy English model (en_core_web_md)

### 5️⃣ Launch Jupyter
```bash
jupyter notebook
```

Navigate to any notebook and start learning! 🎉

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Core language |
| NLTK | 3.8.1 | Tokenization, stemming, POS tagging |
| spaCy | 3.7.2 | Advanced NLP pipeline |
| scikit-learn | 1.3.2 | Feature extraction, ML models |
| pandas | 2.1.4 | Data manipulation |
| NumPy | 1.26.2 | Numerical computing |
| jellyfish | 1.0.3 | Text distance metrics |
| Jupyter | 7.0+ | Interactive notebooks |

---

## 📊 Datasets Used

- **20 Newsgroups** (scikit-learn): 4 categories, 1,586 documents
  - `rec.autos`, `comp.windows.x`, `soc.religion.christian`, `rec.sport.baseball`
- **Custom examples**: Emails, tweets, product reviews

---

## 🎯 Learning Path

**Recommended order for beginners:**

```
00-Regex → 02-Text-Normalization → 04-NLP-NLTK-spaCy-intro → 03-Feature-Extraction → 01-Edit-Distance
```

**For practitioners with NLP background:**
Start with `03-Feature-Extraction` for hands-on classification.

---

## 💡 Key Takeaways

After completing these notebooks, you will:

✅ Clean and preprocess text data effectively  
✅ Extract meaningful features from unstructured text  
✅ Build text classification models  
✅ Understand when to use stemming vs lemmatization  
✅ Implement regex patterns for text extraction  
✅ Compare text similarity using multiple metrics  
✅ Perform Named Entity Recognition  
✅ Choose the right NLP library for your task  

---

## 🔧 Troubleshooting

### Common Issues

**❌ "Resource punkt not found"**
```python
import nltk
nltk.download('punkt')
```

**❌ "Can't find model 'en_core_web_md'"**
```bash
python -m spacy download en_core_web_md
```

**❌ Encoding errors in output**
Add at the beginning of notebooks:
```python
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

See [INSTALLATION.md](INSTALLATION.md) for detailed troubleshooting.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Ideas for contributions:**
- Additional notebooks (Word Embeddings, Transformers, etc.)
- Fix encoding issues in existing notebooks
- Add visualization examples
- Translate to other languages
- Add exercises with solutions

---

## 📚 Additional Resources

### Recommended Reading
- [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) - Jurafsky & Martin
- [Natural Language Processing with Python](https://www.nltk.org/book/) - NLTK Book
- [spaCy Course](https://course.spacy.io/) - Free interactive course

### Online Communities
- [r/LanguageTechnology](https://www.reddit.com/r/LanguageTechnology/)
- [NLP Progress](https://nlpprogress.com/) - Tracking SOTA models
- [Papers with Code - NLP](https://paperswithcode.com/area/natural-language-processing)

### Related Projects
- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [AllenNLP](https://github.com/allenai/allennlp)
- [Gensim](https://github.com/RaRe-Technologies/gensim)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mohammed Zahran**

- LinkedIn: [Mohammed Zahran](https://www.linkedin.com/in/mohamed-zahran-b20125312/)
- GitHub: [@mohamedzahran](https://github.com/mohamedzahran744)

---

## ⭐ Acknowledgments

- NLTK team for the comprehensive NLP toolkit
- spaCy team for the industrial-strength NLP library
- scikit-learn contributors for machine learning tools
- The NLP community for continuous knowledge sharing

---

## 📈 Project Stats

![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-2000%2B-blue)
![Notebooks](https://img.shields.io/badge/Notebooks-5-green)
![Completion](https://img.shields.io/badge/Completion-100%25-brightgreen)

---

<div align="center">

### ⭐ If you find this helpful, please star the repository! ⭐

**Happy Learning! 🚀**

</div>