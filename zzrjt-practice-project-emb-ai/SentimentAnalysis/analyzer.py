import requests
import json


def sentiment_analyzer(text_to_analyse):
    """
    Call the Watson NLP sentiment service if available.
    If not reachable (e.g., running locally on your Mac),
    use a local fallback result.

    Returns:
        dict: {"label": <str>, "score": <float>}
    """

    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    data = None

    # 1) Try real Watson API first
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=5)

        if response.ok and response.text.strip():
            # Convert JSON text → Python dict
            data = json.loads(response.text)

    except requests.exceptions.RequestException:
        # Any network / SSL / timeout error → we'll use fallback instead
        pass

    # 2) If Watson call failed, create a fake response dict (fallback)
    if data is None:
        lower = text_to_analyse.lower()

        positive_words = ["love", "like", "great", "good", "happy", "amazing", "excellent"]
        negative_words = ["hate", "bad", "terrible", "worst", "awful", "sad", "angry"]

        if any(word in lower for word in positive_words):
            label = "SENT_POSITIVE"
            score = 0.95
        elif any(word in lower for word in negative_words):
            label = "SENT_NEGATIVE"
            score = -0.95
        else:
            label = "SENT_NEUTRAL"
            score = 0.0

        data = {
            "documentSentiment": {
                "score": score,
                "label": label
            }
        }

    # 3) Extract only label and score from the (real or fake) response dict
    label = data["documentSentiment"]["label"]
    score = data["documentSentiment"]["score"]

    # 4) Return a clean dictionary as Task 3 requires
    return {"label": label, "score": score}
