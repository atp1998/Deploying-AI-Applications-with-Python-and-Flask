function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value;

    if (!text.trim()) {
        document.getElementById("system_response").innerHTML =
            "Please enter some text first.";
        return;
    }

    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                document.getElementById("system_response").innerHTML = this.responseText;
            } else {
                document.getElementById("system_response").innerHTML =
                    "Error: " + this.status + " " + this.statusText;
            }
        }
    };

    // 👇 Route + query parameter name must match server.py
    xhr.open(
        "GET",
        "/sentimentAnalyzeText?TextToAnalyze=" + encodeURIComponent(text),
        true
    );
    xhr.send();
}
