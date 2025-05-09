
import streamlit as st
import requests

st.title("clone GPT")

if 'message' not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message['role']):
        st.write(message['content'])

if prompt:= st.chat_input("Ask anything....."):
    with st.chat_message('user'):
        st.write(prompt)
    st.session_state.message.append({'role':'user','content':prompt})

if prompt:
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyBDujciL6JlQ4XhzCzLD95c5omGxMiMkKw"

    data= {'contents':[{'parts':[{'text':prompt}]}]}
    response = requests.post(url,json=data)
    response = (response.json())
    response=response['candidates'][0]['content']['parts'][0]['text']
try:
    with st.chat_message('Assistant'):
        st.write(response)
    st.session_state.message.append({'role':'Assistant','content':response})
except:
    pass


