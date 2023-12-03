# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import CTransformers


# chat_model = ChatOpenAI()
chat_model = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title('인공지능 시인')

content = st.text_input('시 제목을 입력해주세요')


if st.button('시 써줘'):
    
    with st.spinner("시를 써주는 중입니다..."):
        result = chat_model.predict(content + "에 대한 시를 써줘")

        st.write('시 제목: ', content)
        st.write('시 내용: ', result)