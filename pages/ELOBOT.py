#import method
from pages.EL_openai_FUNC.openai_func import talkAI_EN, generate_response, sparta_advertiseAI
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
    "Model Num" : ["EL-ELOBOT-EN-1.0", "EL-PAINTBOT-HWABAEK-1.0", "EL-SLOGANBOT-DAVIS-1.0"],
    "Model Name" : ["ELOBOT-EN is English teacher", "HWABAEK is nice Artist", "DAVIS is a versatile advertising and marketing strategist."],
    "Model Function(summary)" : ["This is a bot that answers questions about English words or sentences and corrects errors.", "This bot helps you visualize what's in your head.", "This bot delivers innovative slogans and designs for new products or items."]
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
        # conversation area
        message_area = st.container(height=300)
        with message_area:
            enbot_area_1, enbot_area_2, enbot_area_3 = st.columns([3,9,1])
            with enbot_area_2:
                st.image("useData/EL_img/ELOBOT_ENG_BEFORE.png", width=480)

        # Managing History. Initialize session state for storing chat history if it doesn't exist.
        # if messages not in session_state, print out blank.
        if "messages" not in st.session_state:
            # make a empty list and saving message here
            st.session_state["messages"] = []
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
                    JAVIS-ELOBOT can helpful to you. JAVIS-ELOBOT can your own secretary.")
        st.markdown("##### Draw your own image and see your imagination and thoughts together!")

    with hwabaek_col_4:
        st.markdown("#")

    #Describe & Setting area for drawing images.
    kinds_ELOBOT = ["HWABAEK-ELOBOT : The HWABAEK-ELOBOT is drawing what your thinking or imagination.",
                       "DAVIS-ELOBOT : The JAVIS-ELOBOT is drawing that New Products with slogan."]
    st.divider()
    option = st.selectbox(
        "Please select ELOBOT option for your purpose.",
        (kinds_ELOBOT)
    )
    if option == kinds_ELOBOT[0]:
        drawing_area_col_1,drawing_area_col_2 = st.columns([1.5,1])
        with drawing_area_col_1:
            
            st.title("The HWABAEK-ELOBOT ZONE!!🖼️",  help=None)
            st.subheader(":red[Attention⚠️!!] If using sentences or words that include of any dangerous, violent meanings, HWABAEK-ELOBOT can't drawing. Please use HWABAEK-ELOBOT with a mature and rational mind.😍",  help=None)
            st.markdown("##### :red[※If you contact Error('content_policy_violation'), Don't hesitate and Press F5(refresh)]",  help=None)                
            imgprompt = st.text_input("1.Please enter detailed words or sentences for high-quality","Here is text-input area.")
            kinds_of_size = ["1024x1024","1024x1792","1792x1024"]
            imgsize = st.selectbox(
                "2.Please select size of image",
                (kinds_of_size)
            )
            kinds_of_quality = ["standard", "hd"]
            imgquality = st.selectbox("3.Please select quality of image", (kinds_of_quality))

            HWABAEK_ACTION_BTN = st.button("Drawing Image", use_container_width=True, type="primary")
            HWABAEK_RESULT = None

        with drawing_area_col_2:
        
            if HWABAEK_ACTION_BTN:
                # 이미지를 화면에 표시
                with st.container(height=485, border=True):                    
                    with st.spinner("Drawing the image. please wait👨‍🍳"):
                        HWABAEK_RESULT = generate_response(imgprompt, imgsize, imgquality)
                        # URL에서 이미지를 가져오기
                        response = requests.get(HWABAEK_RESULT) 
                        # 이미지 데이터를 바이너리 형식으로 변환
                        img = Image.open(io.BytesIO(response.content))
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
            elif HWABAEK_RESULT == '''NONE''':
                with st.container(height=550, border=True):
                    st.image("useData/EL_img/ELOBOT_HWABAEK_BAN.png")   

            else:
                with st.container(height=550, border=True):
                    st.image("useData/EL_img/HWABAEK_GUIDE.png")
    
    if option == kinds_ELOBOT[1]:
        st.subheader("Do you have any ideas for a new product or service?🙂 We can offer you :red[Triple-S]!!")
        st.subheader("Remember, you have the right to work comfortably and efficiently.")
        st.subheader("Save your :blue[Money]💰, Save your :blue[Time]🕒, Save your :blue[Energy]💪")
        st.subheader(":red[DAVIS-ELOBOT] will improve the quality of the work environment. So just sit back and comfortably type away😎")        
        adpd_col_1, adpd_col_2 = st.columns([0.4,0.6])
        with adpd_col_1:
            st.image("useData/EL_img/ELOBOT_PD_AD.png")
            myItems = st.text_input("(1) Please input your what kind of item.","Please specify the exact kind of item.")
            myItems_feature = st.text_input("(2) Please input your what feature or function of item.","Please enter the detailed features or functions of the item.")
            myItems_market = st.text_input("(3) Please input your target market.","Please specify the target market, e.g., the United States, Europe, etc.")
            myItems_Client = st.text_input("(4) Please input your target client.","Specify the target client, e.g., men in their 30s, middle-class, etc.")
            myItems_add = st.text_input("(5) Please input what you want to add words or sentences about item.","Please provide any additional phrases or keywords for DAVIS to consider.")
            myItems_button = st.button("Submit", use_container_width=True, type="primary")
        with adpd_col_2:
            slogan_img_area = st.container(border=True, height=1020)
            with slogan_img_area:
                if myItems_button:
                    with st.spinner("Your order is being processed👨‍🍳"):
                        # 주문 내용을 생성
                        myItems_order = f"{myItems} 은 {myItems_feature} 기능 및 특징을 가지고 있어. {myItems}를 판매할 지역은 {myItems_market} 이고 판매 대상은 {myItems_Client}이야. 앞에서 말한 것들과 {myItems_add}를 참고 해서 슬로건 문구와 이미지를 만들어줘. "
                        action_order = sparta_advertiseAI(myItems_order)

                        slogan_result = action_order[0]
                        pdimg_result = action_order[1]

                        # 슬로건 컨테이너
                        slogan_area = st.container(border=True, height=475)
                        # 이미지 컨테이너
                        pdimg_area = st.container(border=True, height=475)

                        # 슬로건 컨테이너에 결과 표시
                        with slogan_area:
                            st.write(slogan_result)
                        
                        # 이미지 컨테이너에 이미지 표시 및 다운로드 버튼 추가
                        with pdimg_area:
                            # URL에서 이미지를 가져오기
                            sloganimg_response = requests.get(pdimg_result)
                            # 이미지 데이터를 바이너리 형식으로 변환
                            img = Image.open(io.BytesIO(sloganimg_response.content))
                            
                            # 이미지를 한 번만 표시
                            st.image(img, use_column_width=True)

                            # 이미지를 바이트 배열로 변환
                            img_byte_arr = io.BytesIO()
                            img.save(img_byte_arr, format='PNG')
                            img_byte_arr = img_byte_arr.getvalue()

                        # 다운로드 버튼을 이미지 아래에 배치
                        st.download_button(
                            label="Download",
                            data=img_byte_arr,
                            file_name="SLOGAN_IMG.png",
                            mime="image/png",
                            use_container_width=True
                        )
                else:
                    davis_col_1, davis_col_2, davis_col_3 = st.columns([0.5,9,0.5])
                    with davis_col_2:
                        st.image("useData/EL_img/ELOBOT_DAVIS_HOPE.png", width=700)