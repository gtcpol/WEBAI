import os
from groq import Groq
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
AI_KEY = "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" 

if not AI_KEY:
    raise ValueError(
        "Masukan GROQ API KEY ke environment masing2 atau pake hardcoded version."
    )

client = Groq(
    api_key=AI_KEY,
)


def ai_call(pesan_user):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": pesan_user,
                }
            ],
            model="llama-3.1-8b-instant",
        )

        ai_output = chat_completion.choices[0].message.content
        return ai_output
    except Exception:
        return "Maaf, AI tidak tersedia saat ini. Silakan coba lagi nanti."


@app.route('/')
def main():
    return render_template('chat.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        # Ambil data dari form
        pesan_user = request.form['chat']
        ai_output = ai_call(pesan_user)
        return render_template(
            "chat.html", pesan_user=pesan_user, ai_output=ai_output
        )
    return render_template('chat.html', pesan_user= None, ai_output=None)
if __name__ == "__main__":
    app.run(debug=True)
