# 📱 WhatsApp Flashcards

A Flask-based WhatsApp chatbot that generates flashcards using the OpenAI GPT-3.5 API. Simply message a topic on WhatsApp and get quick, concise flashcards powered by AI!

## 🚀 Features

- 🧠 Generate 3 flashcards per topic
- 🤖 Uses OpenAI's GPT-3.5 Turbo model
- 📞 WhatsApp integration via Twilio
- 🌐 Flask-based server for handling incoming messages

## 🛠️ Technologies Used

- Python 3.8+
- Flask
- Twilio API for WhatsApp messaging
- OpenAI API
- dotenv for environment variable management

## 📦 Setup Instructions

### 1. Clone the repository

### 2. Install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Set up .env file
OPENAI_API_KEY=your_openai_api_key_here

### 4. Run the Flask app
python app.py

### 5. Connect with Twilio
Create a Twilio account and activate the WhatsApp sandbox.
Set your webhook URL (e.g., using ngrok):

In the Twilio console, set the "WHEN A MESSAGE COMES IN" URL to: https://<your-ngrok-subdomain>.ngrok.io/whatsapp

### How to Use

On WhatsApp, message:
Start Python flashcards

You'll receive 3 flashcards like:
📚 Flashcards for Python:

Q: What is a list in Python?
A: A list is a collection data type that is ordered and mutable.

Q: How do you define a function in Python?
A: Use the 'def' keyword followed by the function name and parentheses.

Q: What is a dictionary in Python?
A: A dictionary is an unordered collection of key-value pairs.
