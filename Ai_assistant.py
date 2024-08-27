import openai
import streamlit as st

# Replace with your OpenAI API key
openai.api_key = "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"

# Function to generate a response from the LLM using the ChatCompletion API
def Reply(question):
    conversation_history = [{"role": "system", "content": "You are a helpful assistant."}, 
                            {"role": "user", "content": question}]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Switch to gpt-4 if you have access
        messages=conversation_history,
        max_tokens=200,
        temperature=0.8
    )
    
    answer = response['choices'][0]['message']['content'].strip()
    return answer

# Streamlit interface
st.title("Chatbot Interface")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = Reply(user_input)
        st.write(f"Chatbot: {response}")
    else:
        st.write("Please enter a question or message.")
