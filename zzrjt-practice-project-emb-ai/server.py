# server.py

from flask import Flask, request, render_template
from SentimentAnalysis.analyzer import sentiment_analyzer

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/sentimentAnalyzeText", methods=["GET"])
def sentiment_analyze_text():
    # Must match the query parameter in mywebscript.js
    text = request.args.get("TextToAnalyze")

    if not text or not text.strip():
        return "Please enter the text to be analyzed.", 400

    result = sentiment_analyzer(text)   # {'label': ..., 'score': ...}
    label = result["label"]
    score = result["score"]

    # The JS expects plain text to display in #system_response
    return f"Sentiment: {label} (score = {score})"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
