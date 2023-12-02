# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI


chat_model = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input('시 제목을 입력해주세요')


if st.button('시 써줘'):
    
    with st.spinner("시를 써주는 중입니다..."):
        result = chat_model.predict(content + "에 대한 시를 써줘")

        st.write('시 제목: ', content)
        st.write('시 내용: ', result)