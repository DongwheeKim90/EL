#import method
from pages.EL_openai_FUNC.openai_func import talkAI_EN, generate_response
#import library
from PIL import Image
import io
import streamlit as st
import pandas as pd
import requests

#page setting
st.set_page_config(layout="wide")
#header
st.title("ELOBOT🤖 : The Lord of the Robots.", anchor=False, help=None)
st.subheader("EL company has a variety of robots.👨🏻‍👩🏻‍👦🏻‍👦🏻", anchor=False, help=None)
st.subheader("The types of ELOBOT are as follows.📋", anchor=False, help=None)
st.markdown("Currently, we created ELOBOT using the API and models :red[gpt-3.5-turbo] and :red[dall-e-3] provided by OPENAI.")
st.markdown("In the future, we plan to release ELOBOT, created with our own technology, through the :blue[development of EL's LLM(large language model) and various models.]")

#-Kinds of ELOBOT
elobot_df = pd.DataFrame({
    "Model Num" : ["EL-ELOBOT-EN-1.0", "EL-PAINTBOT-HWABAEK-1.0"],
    "Model Name" : ["ELOBOT is English teacher", "ELBOT is nice Artist"],
    "Model Function(summary)" : ["This is a bot that answers questions about English words or sentences and corrects errors.", "This bot helps you visualize what's in your head."]
})
st.dataframe(elobot_df, hide_index=True, use_container_width=True, width=700)
#body
tab_1, tab_2 = st.tabs(["ENG Teacher", "Nice Artist"])

# EN : OPENAI_CHAT
with tab_1:
    #divide layout and fix the area rate
    EN_col_1, EN_col_2 = st.columns([1,2.8])
    with EN_col_1:
        st.image("useData/EL_img/ELOBOT_ENG.png", width=350)
    with EN_col_2:
        # Managing History. Initialize session state for storing chat history if it doesn't exist.
        # if messages not in session_state, print out blank.
        if "messages" not in st.session_state:
            # make a empty list and saving message here
            st.session_state["messages"] = []

        # conversation area
        message_area = st.container(height=300)
        # --Display chat history on initial load when input the message
        with message_area:
            for role, message in st.session_state["messages"]:
                # --parameter of chat_meesage is role. role include of user and assistant
                st.chat_message(role).write(message)
        

        # Input area & user ask
        st_userAsk = st.chat_input(placeholder="Please ask to ELOBOT_EN About English", key=None, max_chars=None, disabled=False, on_submit=None, args=None, kwargs=None)
        
        if st_userAsk:
            # Get response from elobot : return answer for ask from openai_fun.py > talkAI_EN
            st_gpt_response = talkAI_EN(st_userAsk)
            
            # Update chat history
            # according st.seesion_STATE include of key(role), value(message)
            st.session_state["messages"].append(('user', st_userAsk))
            st.session_state["messages"].append(('assistant', st_gpt_response))
            
            # Display new messages
            with message_area:
                # Display every messages of user & assistant
                st.chat_message("user").write(st_userAsk)
                st.chat_message("assistant").write(st_gpt_response)
# NA : OPENAI_CHAT                
with tab_2:

    hwabaek_col_1, hwabaek_col_2, hwabaek_col_3, hwabaek_col_4 = st.columns([0.1,0.45,1,0.1]) 

    with hwabaek_col_1:
        st.markdown("#")

    with hwabaek_col_2:
        st.image("useData/EL_img/ELOBOT_HWABAEK.png", width=350)

    with hwabaek_col_3:
        st.markdown("### You can select type of ELOBOT for drawing image.")             
        st.markdown("##### (1)The HWABAEK-ELOBOT")        
        st.markdown("##### The HWABAEK-ELOBOT is drawing what your thinking or imagination. \
                    If you want to get Nice Result? Enter your expression in details by using words or sentences. \
                    Then your imagination will become to materialize and reality.")           
        st.markdown("##### (2)JAVIS-ELOBOT")
        st.markdown("##### The JAVIS-ELOBOT can drawing that New Products with slogan.\
                    For example, If your company prepare to new product design planning or before launch? \
                    JAVIS-ELBOT can helpful to you. JAVIS-ELOBOT can your own secretary.")
        st.markdown("##### Draw your own image and see your imagination and thoughts together!")

    with hwabaek_col_4:
        st.markdown("#")        

    #Describe & Setting area for drawing images.
    kinds_NA_ELOBOT = ["HWABAEK : The HWABAEK-ELOBOT is drawing what your thinkin or imagination.",
                       "JAVIS-ELOBOT : The JAVIS-ELOBOT is drawing that New Products with slogan."]
            
    option = st.selectbox(
        "Please select ELOBOT option for your purpose.",
        (kinds_NA_ELOBOT)
    )
    print(option)
    for v in range(len(kinds_NA_ELOBOT)):

        if option == kinds_NA_ELOBOT[v]:
            drawing_area_col_1,drawing_area_col_2 = st.columns([1.5,1])
            with drawing_area_col_1:
                
                st.title("The HWABAEK-ELOBOT ZONE!!🖼️",  help=None)
                st.subheader(":red[Attention please, If you use sentences or words that include of any dangerous or violent meanings, HWABAEK-ELBOT can't drawing.👿]",  help=None)
                st.subheader("Please use HWABAEK-ELBOT with a mature and rational mind.😍",  help=None)
                prompt = st.text_input("1.Please enter detailed words or sentences for high-quality","Here is text-input area.")
                kinds_of_size = ["1024x1024","1024x1792","1792x1024"]
                imgsize = st.selectbox(
                    "2.Please select size of image",
                    (kinds_of_size)
                )

                HWABAEK_ACTION_BTN = st.button("Drawing Image", use_container_width=True, type="primary")
                HWABAEK_RESULT = None
                if HWABAEK_ACTION_BTN:
                    HWABAEK_RESULT = generate_response(prompt, imgsize)

            with drawing_area_col_2:
                if HWABAEK_RESULT:
                    
                    # URL에서 이미지를 가져오기
                    response = requests.get(HWABAEK_RESULT) 
                    
                    # 이미지 데이터를 바이너리 형식으로 변환
                    img = Image.open(io.BytesIO(response.content))
                    # 이미지를 화면에 표시
                    with st.container(height=450, border=True):
                        st.image(img, use_column_width=True)
                    
                    # 이미지를 바이트 배열로 변환
                    img_byte_arr = io.BytesIO()
                    img.save(img_byte_arr, format='PNG')
                    img_byte_arr = img_byte_arr.getvalue()
                    
                    # 다운로드 버튼 제공
                    st.download_button(
                        label="Download",
                        data=img_byte_arr,
                        file_name="HWABAEK_BOT_IMG.png",
                        mime="image/png",
                        use_container_width=True
                    )
                else:
                    with st.container(height=450, border=True):
                        st.image("useData/EL_img/HWABAEK_GUIDE.png")