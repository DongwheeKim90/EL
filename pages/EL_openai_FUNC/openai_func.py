#import library
import openai
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)

# API_KEY 설정
# --Inner
#openai.api_key = os.environ.get("mySecretkey_openai")
# --streamlit
myOpenAI_Key = st.secrets["mySecretkey_openai"]

# (1) openai Chatbot : ELBOT_EN
def talkAI_EN(user_message):
    #user input word
    input_value = {
        "role":"user",
        "content":user_message
    }
    
    # OpenAI ChatGPT setting and callAPI
    response = openai.ChatCompletion.create(
        # define model
        model="gpt-3.5-turbo",
        # setting role
        messages=[{
            "role": "system",
            "content": "당신은 영어 전문가이자 영어 번역가입니다. 영어 외 다른 영역에 대한 질문은 답하지마."
            },
            {"role":"user",
            "content":user_message}],
        # various of response
        temperature=0.6,
        # weather streaming of response
        stream=False
    )
    # elobot_el response
    gpt_response = response["choices"][0]["message"]["content"]

    return gpt_response

# (2) openai Chatbot : ELBOT_HWABAEK
def HWABAEK_TRANSLATE_PROMPT(text):
    translate_template = "You are a helpful assistant that translates {input_language} to {output_language}."
    system_message = translate_template.format(input_language="Korean", output_language="English")

    # API 호출로 번역 결과 생성
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": text}
        ],
        temperature=0,
        max_tokens=100
    )
    
    return response.choices[0].message['content'].strip()

def generate_response(prompt, imgtype, imgsize):
    # 번역 결과 생성
    translate_result = HWABAEK_TRANSLATE_PROMPT(prompt)

    # GPT-3.5 응답 생성
    HWABAEK_GPT_PROMPT = [
        {"role": "system", "content": "Imagine the details of the input shape. Please answer briefly."},
        {"role": "user", "content": translate_result}
    ]

    gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=HWABAEK_GPT_PROMPT,
        temperature=0.6,
        max_tokens=150
    )
    gpt_prompt_result = gpt_response.choices[0].message['content'].strip()

    # DALL-E 이미지 생성
    dalle_response = openai.Image.create(
        model="dall-e-3",
        prompt = prompt,
        size = imgsize,
        n = 1,
        style=imgtype
    )

    dalle_img_url = dalle_response['data'][0]['url']

    return dalle_img_url