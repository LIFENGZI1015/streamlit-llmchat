import streamlit as st
import pytesseract
from PIL import Image

def file_uploader():
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx", "jpeg"])

    if uploaded_file is not None:
        file_type = uploaded_file.type
        file_name = uploaded_file.name

        # Check if file is an image (jpeg/jpg)
        if file_type.startswith('image'):
            img = Image.open(uploaded_file)
            st.image(img, caption=file_name, use_column_width=True)

        # For other file formats like txt, pdf, docs
        else:
            file_content = uploaded_file.read()
            st.write(file_content.decode('utf-8'))

        return uploaded_file

def prompt_function():

    uploaded_file = file_uploader()

    if uploaded_file is not None:
        prompt = st.text_input("Ask a question about the uploaded file")

        if st.button("Get Answer"):
            # Perform some processing on the uploaded file and the prompt

            # For example, if the file is an image, use OCR to extract text
            if uploaded_file.type.startswith('image'):
                img = Image.open(uploaded_file)
                text = pytesseract.image_to_string(img)
                st.write(f"OCR Text: {text}")

            # If the file is a text file, you can perform text analysis
            elif uploaded_file.type == 'text/plain':
                # Perform your analysis on the text

                st.write(f"Answer: Some analysis result based on the prompt")
                
# Run the prompt_function
prompt_function()




import streamlit as st
import pandas as pd
import docx2txt  # You may need to install this package for DOCX files: pip install docx2txt

def main():
    st.title("File Upload and Question Prompting App")

    # File upload section
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "jpeg", "docx"])

    # If a file is uploaded
    if uploaded_file is not None:
        # Display file details
        st.write("File Details:")
        file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)

        # Read the file based on its type
        file_contents = None
        if uploaded_file.type == "text/plain":  # TXT file
            file_contents = uploaded_file.read()
        elif uploaded_file.type == "application/pdf":  # PDF file
            file_contents = read_pdf(uploaded_file)
        elif uploaded_file.type == "image/jpeg":  # JPEG file
            file_contents = read_image(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":  # DOCX file
            file_contents = read_docx(uploaded_file)

        # Prompt the user with questions
        prompt_questions(file_contents)

def read_pdf(uploaded_file):
    # You can use a PDF parsing library here based on your requirements
    # For example, PyMuPDF or PyPDF2
    # For simplicity, let's assume we're reading the first page as text
    return "PDF content goes here"

def read_image(uploaded_file):
    # You can use an image processing library here based on your requirements
    # For example, PIL or OpenCV
    # For simplicity, let's assume we're displaying the image
    return st.image(uploaded_file)

def read_docx(uploaded_file):
    # Use docx2txt to extract text from DOCX files
    return docx2txt.process(uploaded_file)

def prompt_questions(file_contents):
    # Replace this with your actual questions based on the file contents
    question1 = st.text_input("Question 1:", "Type your answer here")
    question2 = st.text_input("Question 2:", "Type your answer here")

    # You can process and analyze the answers further as needed

if __name__ == "__main__":
    main()