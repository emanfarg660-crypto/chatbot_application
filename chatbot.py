
import google.generativeai as genai
import streamlit as st

api = 'Api_Key'

#configure google generative ai
if api:
    genai.configure(api_key= api)
else:
    st.error('Your API is Not Found')

#function to generate text using google API
def Generate_Text(text):
    #call generative model from google AI
    model = genai.GenerativeModel('gemini-3-flash-preview')
    #generate response from Gemini
    response = model.generate_content(text)
    return response.text

if 'messages' not in st.session_state:
    st.session_state.messages = []

#display all messages
for message in st.session_state.messages:
    with st.chat_message(message['role']):  #role: user / assistant
        st.markdown(message['content']) #content : user_input / response from model

#input area for user input user 
if user_input := st.chat_input('Please Enter Your Text...'):
    #display user message
    with st.chat_message('user'):
        st.markdown(user_input)

    #append user message in session state
    st.session_state.messages.append({'role' : 'user', 'content': user_input})

    #generate response from google gemini API
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        with st.spinner('Generating Response....'):
            response_text = Generate_Text(user_input)
            message_placeholder.markdown(f'{response_text}')

    #append response and role in session state
    st.session_state.messages.append({'role' : 'assistant', 'content' : response_text})
