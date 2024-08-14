import openai
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# API_KEY 설정
os.environ["OPENAI_API_KEY"] = st.secrets["mySecretkey_openai"]

# ChatOpenAI 인스턴스 생성
client = ChatOpenAI(temperature=0.1,
                    openai_api_key=os.environ.get("mySecretkey_openai"))

# (1) openai Chatbot : ELBOT_EN
def talkAI_EN(user_message):
    messages = [
        SystemMessage(content="당신은 영어 전문가이자 영어 번역가입니다. 영어 외 다른 영역에 대한 질문은 답하지마."),
        HumanMessage(content=user_message)
    ]
    
    response = client(messages=messages)
    
    gpt_response = response.content  # AIMessage 객체에서 직접 content를 가져옴
    return gpt_response

# (2) Dall-e-3 : ELBOT_HWABAEK
def generate_response(imgprompt, imgsize, imgquality):

    try:
        # DALL-E 이미지 생성
        dalle_response = openai.images.generate(
        model="dall-e-3",
        prompt=imgprompt,
        #size : 1024x1024, 1024x1792, 1792x1024
        size=imgsize,
        #quality : standard 기본, hd 고품질
        quality=imgquality,
        n=1,
        )
        dalle_img_url = dalle_response.data[0].url

    except (openai.BadRequestError, openai.APIError, openai.APIConnectionError, openai.RateLimitError) as e:
        # 오류가 발생했을 때 예외 처리
        print("★★★★★★★★★★★")
        print(f"Error: {e}")
        print("★★★★★★★★★★★")

        dalle_img_url = '''NONE'''  # 오류가 발생하면 Danger_Input을 반환

    return dalle_img_url

# (3) openai + Dalle-3 : Davis
def sparta_advertiseAI(req_ad):
    chat_completion = openai.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"나는 광고 컨설팅 전문가, 제품 디자인 전문가야. 너가 요청한 {req_ad}를 위해 멋진 슬로건을 만들수 있어.",
            },
            {
                "role": "user",
                "content": f"나는 새로운 상품 또는 서비스 기획과 출시를 앞두고 있어. 제발 부탁인데 내가 요청한 {req_ad} 를 신경써서 세련된 슬로건을그려줘. 참고로 나는 너의 고객이 아니고 업무를 지시하는 요청자야. 내가 한번 지시를 한 것에 다시 또 물어보거나 정보요청하는 문구를 말하지말고 {req_ad} 를 다시 한번 보고 작업해줘.",
            }
        ],
        model="gpt-4o",
    )
    adver_res = chat_completion.choices[0].message.content

    make_ad = openai.images.generate(
        model="dall-e-3",
        prompt=req_ad,
        size="1024x1024",
        quality="hd",
        n=1
        )

    image_url = make_ad.data[0].url
    
    return adver_res, image_url
