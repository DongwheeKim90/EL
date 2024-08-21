import streamlit as st
from pages.TextSnatcher_FUNC.snatcher_method import get_pdf_contents

st.title("PTS : PDF TextSnatcher")
#업로드존
st.subheader("Upload PDF file")
upload_zone = st.container(border=True, height= 180)
with upload_zone:
    upload_area_pdf = st.file_uploader(
    "Only choose your PDF file",
    type="pdf",
    accept_multiple_files=False,
    key="upload_area_pdf",  # 세션 상태 키 지정
    on_change=get_pdf_contents,  # 파일이 업로드될 때 콜백 함수 호출
    label_visibility="hidden"
)
    if st.session_state.upload_area_pdf == None:
        st.text("No PDF file uploaded.")

#요약존
st.subheader("File summary and Extracted content")
contents_zone = st. container(border=True, height=400)
with contents_zone:
    if st.session_state.upload_area_pdf == None:
        contents_zone_col_1, contents_zone_col_2, contents_zone_col_3 = st.columns([0.2,0.4,0.3])
        with contents_zone_col_2:
            st.image("useData/EL_img/upload_pdf.png", width=369)
    else:
        st.write(f"- Total {st.session_state['page_num']} pages.")
        st.write("- Result of extracted")
        st.write(f"{st.session_state['output_text']}")
        
        file_nm = str(st.session_state.upload_area_pdf.name).replace(".pdf", "")
        text_content = st.session_state['output_text']
        # 다운로드 버튼을 생성하여 사용자에게 파일을 제공

# 다운로드 버튼을 contents_zone 아래로 이동
if st.session_state.upload_area_pdf is not None:
    st.download_button(
        label="Download your text file",
        data=text_content,
        file_name=f"{file_nm}.txt",
        mime="text/plain",
    )