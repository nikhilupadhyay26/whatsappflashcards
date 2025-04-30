import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("API Key:", api_key)

# Create OpenAI client (new SDK syntax)
client = openai.OpenAI(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip().lower()
    sender = request.values.get('From', '')

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.startswith("start"):
        topic = incoming_msg.replace("start", "").replace("flashcards", "").strip()
        if topic == "":
            msg.body("Please mention a topic. For example: 'Start Python flashcards'")
        else:
            flashcards = generate_flashcards(topic)
            msg.body(f"📚 Flashcards for *{topic.title()}*:\n\n{flashcards}")
    else:
        msg.body("👋 Hi! To begin, type: Start [topic] flashcards\nExample: Start Python flashcards")

    return str(resp)

def generate_flashcards(topic):
    prompt = f"Create 3 concise flashcards on the topic '{topic}'. Each flashcard should be in this format:\n\nQ: <question>\nA: <answer>\n\n"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I couldn't generate flashcards right now."

if __name__ == "__main__":
    app.run(debug=True)
