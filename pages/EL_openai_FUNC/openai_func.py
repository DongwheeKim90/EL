#import library
import openai
import os

# API_KEY 설정
# --Inner
openai.api_key = os.environ.get("mySecretkey_openai")

# (1) openai Chatbot : no settings
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