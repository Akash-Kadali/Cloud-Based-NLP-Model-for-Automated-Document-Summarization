# 🧠 Text Summarization NLP App

An AI-powered tool to simplify **text analysis** and **document summarization** using cutting-edge Natural Language Processing (NLP) techniques. With just a few clicks, you can generate summaries, detect sentiment, and visualize text insights, making it easy to process and understand large volumes of content.

> ✅ **Live Demo:** [https://cloud-based-nlp-model-for-automated.onrender.com](https://cloud-based-nlp-model-for-automated.onrender.com)

---

## 🚀 Features

- 📝 **Text Summarization**  
  Generate concise, relevant summaries using:
  - Frequency-based NLP methods  
  - Pegasus (transformer-based) model via Modal API

- 📊 **Sentiment Analysis**  
  Analyze emotional tone — positive, negative, or neutral — using VADER and visualize it using Chart.js.

- ☁️ **Word Cloud Generation**  
  Visualize high-frequency words in your text using intuitive word clouds.

- 📄 **PDF Upload Support**  
  Upload and extract text directly from PDF files.

- 🌗 **Light/Dark Mode**  
  Toggle between elegant light and dark themes for comfortable reading.

---

## 🧪 Usage Guide

1. **Summarize Text**  
   Paste text or upload a PDF → choose summarization → select Pegasus or frequency-based → view results.

2. **Analyze Sentiment**  
   Quickly determine the sentiment of your content with VADER.

3. **Generate Word Cloud**  
   Visual representation of top keywords for easy interpretation.

---

## 📦 Requirements

- **Python Version:** 3.10 to 3.11

### 📥 Install Dependencies

```bash
pip install -r requirements.txt
````

---

## 💻 Run Locally

Follow these steps to clone and run the application on your local machine:

### 🔁 Step 1: Clone the Repository

```bash
git clone https://github.com/Akash-Kadali/Cloud-Based-NLP-Model-for-Automated-Document-Summarization.git
cd Cloud-Based-NLP-Model-for-Automated-Document-Summarization
```

### 🛠️ Step 2: Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate         # For Windows
# OR
source venv/bin/activate      # For macOS/Linux
```

### 📥 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### 📦 Step 4: Download NLTK VADER Lexicon (One-Time Setup)

In Python shell:

```python
import nltk
nltk.download('vader_lexicon')
```

### ▶️ Step 5: Start the Application

Navigate to the backend directory if needed, then:

```bash
python app.py
```

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 UI Snapshots

### 🔹 Home Page

![Home](https://raw.githubusercontent.com/Akash-Kadali/Cloud-Based-NLP-Model-for-Automated-Document-Summarization/main/static/2.png)

### 🔹 Text Summarization

![Summarization](https://raw.githubusercontent.com/Akash-Kadali/Cloud-Based-NLP-Model-for-Automated-Document-Summarization/main/static/4.png)

### 🔹 Sentiment Analysis

![Sentiment](https://raw.githubusercontent.com/Akash-Kadali/Cloud-Based-NLP-Model-for-Automated-Document-Summarization/main/static/1.png)

### 🔹 Word Cloud

![Word Cloud](https://raw.githubusercontent.com/Akash-Kadali/Cloud-Based-NLP-Model-for-Automated-Document-Summarization/main/static/3.png)

---

## 🔧 Tech Stack

* **Backend:** Flask
* **NLP:** NLTK, VADER, Transformers, SentencePiece
* **Visualization:** Matplotlib, WordCloud, Chart.js
* **Cloud Inference:** Pegasus model via Modal API

---

## 📄 License

MIT License — free for personal and commercial use. Attribution appreciated.

---

> Designed & Developed by **Sri Akash Kadali**
> Empowering faster reading, smarter decisions ✨
