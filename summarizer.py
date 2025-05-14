import nltk
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.probability import FreqDist
import os

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('vader_lexicon')

# ✅ Summarization (Pegasus + fallback)
def summarize_text(text, use_pegasus=False, num_sentences=2):
    if use_pegasus:
        try:
            url = "https://akash-kadali--pegasus-api-fastapi-app.modal.run/summarize"
            response = requests.post(url, json={"text": text})
            if response.status_code == 200:
                return response.json().get("summary", "No summary returned.")
            return "Pegasus API error."
        except Exception as e:
            return f"Pegasus API call failed: {e}"
    
    # ✅ Frequency-based fallback
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    freq_dist = FreqDist(words)
    max_freq = max(freq_dist.values(), default=1)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_dist[word] / max_freq

    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return TreebankWordDetokenizer().detokenize(ranked_sentences)

# ✅ Sentiment Analysis
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

# ✅ Word Cloud
def generate_wordcloud(text, filename):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    filepath = os.path.join('static', 'images', filename)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()
    return filepath

# ✅ Word Frequency Bar Chart
def plot_word_frequency(text, filename, top_n=10):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    freq_dist = FreqDist(words)
    common_words = freq_dist.most_common(top_n)

    words, counts = zip(*common_words)
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color='skyblue')
    plt.xticks(rotation=45)
    plt.title("Top Word Frequencies")
    plt.tight_layout()

    filepath = os.path.join('static', 'images', filename)
    plt.savefig(filepath)
    plt.close()
    return filepath
