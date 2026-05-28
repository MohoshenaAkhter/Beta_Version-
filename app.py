# app.py
from flask import Flask, render_template, request, jsonify
from ai_engine import get_emotion_and_scene
from data_handler import save_scene, load_scenes
from stats import get_emotion_chart_base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_input = data.get("text", "").strip()
    if not user_input:
        return jsonify({"error": "Empty input"}), 400
    try:
        result = get_emotion_and_scene(user_input)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/save", methods=["POST"])
def save():
    data = request.get_json()
    result = {
        "emotion": data["emotion"],
        "scene": data["scene"],
        "camera_style": data["camera_style"],
        "lighting": data["lighting"],
        "colors": data["colors"]
    }
    save_scene(data["input"], result)
    return jsonify({"status": "saved"})

@app.route("/history")
def history():
    entries = load_scenes().to_dict(orient="records")
    chart = get_emotion_chart_base64()
    return render_template("history.html", entries=entries, chart=chart)

if __name__ == "__main__":
    app.run(debug=True)