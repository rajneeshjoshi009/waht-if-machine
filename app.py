import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
import os  # Import os module

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Set up Google AI API key securely
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def what_if_chatbot(user_input):
    if not user_input.lower().startswith("what if"):
        return "I can only answer 'What If' questions. Try something fun, like 'What if cats ruled the world?' 😼"

    try:
        # Define a humorous chatbot personality
        personality = (
            "You are a funny, sarcastic, and witty AI that loves answering hypothetical 'What If' questions in a humorous way. "
            "Make your responses entertaining, use jokes, and add a playful tone. Keep the answer engaging and fun!"
        )

        # Use Google's Gemini Pro model
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"{personality}\nUser: {user_input}\nAI:")
        
        return response.text.strip()
    
    except Exception as e:
        return f"Oops! My circuits got tangled! Error: {str(e)} 🤖💥"

# Root route to prevent 404 error
@app.route('/')
def home():
    return "🚀 What-If API is running! Use the /what-if endpoint to send your queries."

@app.route('/what-if', methods=['POST'])
def handle_what_if():
    data = request.get_json()
    user_input = data.get('user_input', '')
    response = what_if_chatbot(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
