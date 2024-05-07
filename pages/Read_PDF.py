import streamlit as st
import io
import PyPDF2

def read_pdf(uploaded_file):
    # Get the content of the uploaded file as bytes
    pdf_bytes = uploaded_file.read()


    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))

    # Initialize an empty string to store the text
    text = ""

    # Loop through each page in the PDF
    for page_num in range(len(pdf_reader.pages)): #len(reader.pages) 
        # Extract text from the page and append to the text string
        # reader.pages[page_number]
        text += pdf_reader.pages[page_num].extract_text()

    return text

def main():
    st.title("PDF to Text Converter")
    st.write("Upload a PDF file to extract its text.")

    # Allow the user to upload a file
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Read the uploaded PDF file
        text = read_pdf(uploaded_file)
        # Display the extracted text
        st.subheader("Extracted Text:")
        st.write(text)

if __name__ == "__main__":
    main()
