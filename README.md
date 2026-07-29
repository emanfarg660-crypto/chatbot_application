# Gemini AI Chatbot

## Overview

This project is a web-based AI chatbot built with **Python**, **Streamlit**, and the **Google Gemini API**. It provides a simple conversational interface that allows users to interact with Google's Gemini language model while maintaining the conversation history throughout the session.

---

## Features

- Interactive chat interface
- Integration with Google Gemini API
- Conversation history using Streamlit Session State
- Secure API key management with Streamlit Secrets
- Lightweight and easy to deploy

---

## Project Structure

```
.
├── app.py
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
└── README.md
```

---

## Technologies

- Python
- Streamlit
- Google Generative AI SDK

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/gemini-chatbot.git
```

Navigate to the project directory:

```bash
cd gemini-chatbot
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create the following file:

```
.streamlit/secrets.toml
```

Add your API key:

```toml
GOOGLE_API_KEY = "YOUR_API_KEY"
```

Generate an API key from Google AI Studio.

---

## Running the Application

```bash
streamlit run app.py
```

---

## Application Workflow

```
User Input
      │
      ▼
Streamlit Chat Interface
      │
      ▼
Generate_Text()
      │
      ▼
Google Gemini API
      │
      ▼
Generated Response
      │
      ▼
Display Response
      │
      ▼
Store Conversation in Session State
```

---

## Implementation

The application follows the following sequence:

1. Load the API key from Streamlit Secrets.
2. Configure the Google Generative AI client.
3. Receive user input through the Streamlit chat interface.
4. Send the prompt to the Gemini model.
5. Receive the generated response.
6. Display the response in the chat window.
7. Store both user and assistant messages in the session state to preserve the conversation.

---

## Requirements

```
streamlit
google-generativeai
```

---

## Future Improvements

- Streaming responses
- Multiple Gemini model selection
- File upload support
- Conversation export
- Markdown and code syntax highlighting
- Chat history persistence
- Authentication and user accounts



Eman Ibrahim Farag

Mechatronics Engineer | Artificial Intelligence and Machine Learning
