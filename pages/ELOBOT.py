#import method
from pages.EL_openai_FUNC.openai_func import talkAI_EN
#import library
import streamlit as st
import pandas as pd

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
    "Model Num" : ["EL-ELOBOT-EN-1.0", "EL-PAINTBOT-HWABAECK-1.0"],
    "Model Name" : ["ELOBOT is English teacher", "ELBOT is nice artist"],
    "Model Function(summary)" : ["This is a bot that answers questions about English words or sentences and corrects errors.", "This bot helps you visualize what's in your head."]
})
st.dataframe(elobot_df, hide_index=True, use_container_width=True, width=700)
#body
tab_1, tab_2 = st.tabs(["ENG Teacher", "Nice artist"]) 
# EN : OPENAI_CHAT
with tab_1:
    # Managing History. Initialize session state for storing chat history if it doesn't exist.
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    # conversation area
    message_area = st.container(height=300)

    # Display chat history on initial load
    with message_area:
        for role, message in st.session_state["messages"]:
            st.chat_message(role).write(message)
    
    # Input area & user ask
    st_userAsk = st.chat_input(placeholder="Please ask to ELOBOT_EN About English", key=None, max_chars=None, disabled=False, on_submit=None, args=None, kwargs=None)
    
    if st_userAsk:
        # Get response from elobot
        st_gpt_response = talkAI_EN(st_userAsk)
        
        # Update chat history
        st.session_state["messages"].append(('user', st_userAsk))
        st.session_state["messages"].append(('assistant', st_gpt_response))
        
        # Display new messages
        with message_area:
            # Display only the last two messages
            st.chat_message("user").write(st_userAsk)
            st.chat_message("assistant").write(st_gpt_response)