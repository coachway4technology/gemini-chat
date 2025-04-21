from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()
messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input.strip():
            messages.append({"sender": "user", "text": user_input})
            response = chat.send_message(user_input)
            messages.append({"sender": "gemini", "text": response.text})
    return render_template("chat.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
