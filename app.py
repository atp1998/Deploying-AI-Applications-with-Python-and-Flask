from flask import Flask, jsonify

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<b> My first Flask application in action! </b>"

@app.route("/")
def api_message():
    data = {
        "message": "Hello from Flask JSON!",
        "status": "success"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
