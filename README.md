#Streamlit Gemini Chatbot#


This project is a simple AI Chatbot web app built using Streamlit and Google Generative AI (Gemini).
It allows users to chat with a Gemini model in real-time through a clean chat interface.

# Features#
Chat interface using Streamlit
Integration with Google Gemini API
Conversation memory during session (chat history)
Loading spinner while generating responses
Simple and beginner-friendly structure


 #Tech Stack#
Python
Streamlit
Google Generative AI (google-generativeai)


# Installation
Clone the project
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

 Install dependencies
pip install streamlit google-generativeai

# API Key Setup
You need a Google Gemini API key.
Replace this line in the code:
api = 'Api_Key'
With your real key:
api = "YOUR_GOOGLE_API_KEY"







# How It Works
User types a message in the chat input
Message is stored in st.session_state

Gemini model generates a response:

model = genai.GenerativeModel('gemini-3-flash-preview')
Response is displayed in chat UI
Both user & assistant messages are saved for context

 Project Structure
chatbot.py      # Main Streamlit app
README.md       # Project documentation

# Notes
Make sure your API key is valid and active
Internet connection is required
Session history resets when page refreshes


# Future Improvements
Add authentication system
Save chat history to database
Improve UI with Streamlit components
Add voice input/output
