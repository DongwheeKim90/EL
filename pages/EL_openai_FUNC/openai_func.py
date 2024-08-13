import openai
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# API_KEY 설정
# --Inner
os.environ["OPENAI_API_KEY"] = os.environ.get("mySecretkey_openai")
# --streamlit
#myOpenAI_Key = st.secrets["mySecretkey_openai"]

# ChatOpenAI 인스턴스 생성
client = ChatOpenAI(temperature=0.6, openai_api_key=os.environ.get("mySecretkey_openai"))

# (1) openai Chatbot : ELBOT_EN
def talkAI_EN(user_message):
    messages = [
        SystemMessage(content="당신은 영어 전문가이자 영어 번역가입니다. 영어 외 다른 영역에 대한 질문은 답하지마."),
        HumanMessage(content=user_message)
    ]
    
    response = client(messages=messages)
    
    gpt_response = response.content  # AIMessage 객체에서 직접 content를 가져옴
    return gpt_response

# (2) openai Chatbot : ELBOT_HWABAEK
def HWABAEK_TRANSLATE_PROMPT(text):
    messages = [
        SystemMessage(content="You are a helpful assistant that translates Korean to English."),
        HumanMessage(content=text)
    ]
    
    response = client(messages=messages)
    
    return response.content.strip()  # AIMessage 객체에서 직접 content를 가져옴

def generate_response(prompt, imgsize):
    # 번역 결과 생성
    translate_result = HWABAEK_TRANSLATE_PROMPT(prompt)

    # GPT-3.5 응답 생성
    messages = [
        SystemMessage(content="Imagine the details of the input shape. Please answer briefly."),
        HumanMessage(content=translate_result)
    ]
    
    response = client(messages=messages)
    
    gpt_prompt_result = response.content.strip()  # AIMessage 객체에서 직접 content를 가져옴

    # DALL-E 이미지 생성
    dalle_response = openai.images.generate(
        model="dall-e-3",
        prompt=gpt_prompt_result,
        size=imgsize,
        n=1
    )
    dalle_img_url = dalle_response.data[0].url

    return dalle_img_url

#--test
#print(generate_response("웃고있는 아기 공룡", "1024x1024"))