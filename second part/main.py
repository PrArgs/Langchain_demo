import streamlit as st
import langchain_helper as lch
import textwrap
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="YouTube Assistant", layout="centered")
st.title("🎥 YouTube Assistant")

with st.sidebar:
    with st.form(key='query_form'):
        youtube_url = st.text_area(
            label="🔗 Enter YouTube video URL",
            max_chars=100
        )
        query = st.text_area(
            label="❓ Ask a question about the video",
            max_chars=100,
            key="query"
        )
        submit_button = st.form_submit_button(label='Submit')

if submit_button and query and youtube_url:
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        st.error("🔑 Please set your OpenAI API key in your environment variables.")
        st.stop()

    with st.spinner("Processing the video and generating a response..."):
        db = lch.create_db_from_youtube_video_url(youtube_url)

        if db is None:
            st.error("🚫 Failed to load transcript. Make sure the video has a valid transcript.")
        else:
            response, docs = lch.get_response_from_query(db, query)
            st.subheader("💬 Answer:")
            st.text(textwrap.fill(response, width=85))

            with st.expander("📝 Relevant Transcript Snippets"):
                for i, doc in enumerate(docs, 1):
                    st.markdown(f"**Chunk {i}:** {doc.page_content}")
