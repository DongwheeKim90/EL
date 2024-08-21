import pdfplumber
import streamlit as st

def get_pdf_contents():
    # 업로드된 파일 객체를 Streamlit 세션 상태에서 가져옴
    uploaded_file = st.session_state.upload_area_pdf
    
    if uploaded_file is not None:
        # pdfplumber를 사용하여 업로드된 PDF 읽기
        with pdfplumber.open(uploaded_file) as pdf:
            # PDF의 페이지 수를 c추출
            page_num = len(pdf.pages)
            # Streamlit의 세션 상태에 페이지 수를 저장
            st.session_state["page_num"] = page_num  
            
            # 추출된 텍스트를 저장리스트.
            output_text = []
            for page in pdf.pages:
                # 각 페이지에서 텍스트를 추출.
                text = page.extract_text().replace("()"," ").replace("•", "").replace('''""''',"").replace(". ","").replace("Copyright©2023. Acadential. All rights reserved.","").replace("/ , , ,","").replace("Copyright©2023AcadentialAll rights reserved.","")
                # 추출된 텍스트를 리스트에 추가.
                output_text.append(text)
        
        # 모든 페이지의 텍스트를 하나의 문자열로 결합.
        # 각 페이지의 텍스트는 줄바꿈(\n)으로 구분.
        st.session_state["output_text"] = "\n".join(output_text)

    # 세션 상태에 저장된 페이지 수와 텍스트를 반환.
    return st.session_state["page_num"], st.session_state["output_text"]