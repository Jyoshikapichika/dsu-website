from flask import Flask, request, jsonify
import openai

app = Flask(_name_)

# 🔑 Add your OpenAI API key
openai.api_key = "AIzaSyBLATBB0IGEkYanVJy9gbJyTrPEsFnWxSc"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Call OpenAI GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",   # You can use gpt-4 if available
        messages=[{"role": "system", "content": "You are a helpful chatbot."},
                  {"role": "user", "content": user_message}]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if _name_ == "_main_":
    app.run(debug=True)
