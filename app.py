from flask import Flask, render_template, request
from summarizer import summarize_text, analyze_sentiment, generate_wordcloud, plot_word_frequency
from pdf_extractor import extract_text_from_pdf
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text', '')
    action = request.form.get('action')
    pdf_file = request.files.get('pdf_file')

    # Extract text from PDF if uploaded
    if pdf_file:
        text += "\n" + extract_text_from_pdf(pdf_file)

    # Handle empty input
    if not text.strip():
        return render_template('result.html', display="No Result", result="No valid input provided.")

    # Summarization
    if action == 'summarize':
        use_pegasus = 'pegasus' in request.form  # ✅ Fix: read checkbox value properly
        summary = summarize_text(text, use_pegasus=use_pegasus)
        method_used = "Pegasus LLM" if use_pegasus else "Frequency-Based"
        display_text = f"Summarized Text ({method_used})"
        return render_template('result.html', display=display_text, result=summary)

    # Sentiment Analysis + Chart
    elif action == 'sentiment':
        result_dict = analyze_sentiment(text)
        result = get_sentiment_label(result_dict)
        return render_template('sentiment_result.html', display="Sentiment Analysis", result=result, result_dict=result_dict)

    # Word Cloud
    elif action == 'wordcloud':
        filename = "wordcloud.png"
        path = generate_wordcloud(text, filename)
        return render_template('result1.html', display="Word Cloud", image_path=path)

    # Word Frequency Chart (optional, if used)
    elif action == 'frequency':
        filename = "frequency.png"
        path = plot_word_frequency(text, filename)
        return render_template('result1.html', display="Word Frequency", image_path=path)

    # Fallback
    return render_template('result.html', display="No Result", result="Action not recognized.")

# Helper function for sentiment label
def get_sentiment_label(scores):
    compound = scores['compound']
    if compound >= 0.05:
        return f"Positive : {scores}"
    elif compound <= -0.05:
        return f"Negative : {scores}"
    else:
        return f"Neutral : {scores}"

if __name__ == '__main__':
    app.run(debug=True)
