import streamlit as st
import requests

# Gemini API endpoint 및 API 키 설정
GEMINI_API_URL = "https://api.gemini.com/v1/answer"
API_KEY = "AIzaSyDIYgGSW1JnXWtqmPjSA7YR9-A4xz7-YYg"

# Streamlit 앱 제목 설정
st.title("Gemini API Question Answering")

# 사용자 입력란 (질문)
user_question = st.text_input("Ask a question:")

def get_gemini_response(question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "question": question
    }
    response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json().get("answer", "No answer available")
    else:
        return f"Error: {response.status_code}"

# 버튼 클릭 시 응답 가져오기
if st.button("Get Answer"):
    if user_question:
        answer = get_gemini_response(user_question)
        st.write(f"**Answer:** {answer}")
    else:
        st.warning("Please enter a question.")