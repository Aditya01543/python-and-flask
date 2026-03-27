from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detection():
    text_to_analyze = request.args.get('text')

    # 🔥 HANDLE BLANK INPUT
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid input! Please try again."

    result = emotion_detector(text_to_analyze)

    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)