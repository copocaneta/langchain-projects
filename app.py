import streamlit as st

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("Chat with mulitiple PDFs :books:")
    st.text_input("Ask a question about these documents")

    with st.sidebar:
        st.subheader("My Documents")
        st.file_uploader("Upload PDFs here and process")
        st.button("Process")

    
if __name__ == "__main__":
    main()
