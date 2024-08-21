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
txt_btn = st.button("Download to .txt file",use_container_width=True,type="primary")

if txt_btn:
    down_spin = st.spinner("Please wait a minute.")
    file_nm = str(st.session_state.upload_area_pdf.name).replace(".pdf","")
    with open(f"{file_nm}.txt","w", encoding="utf-8") as dwn_file:
        dwn_file.write(st.session_state['output_text'])