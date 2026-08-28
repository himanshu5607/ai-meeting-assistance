import streamlit as st
from dotenv import load_dotenv

from main import run_pipeline
from core.rag_engine import ask_question

load_dotenv()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Meeting Assistant",
    page_icon="🤖",
    layout="wide",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f7f7f7;
        margin-bottom: 15px;
    }

    .chat-user {
        background-color: #e8f0fe;
        padding: 12px;
        border-radius: 10px;
        margin: 8px 0;
    }

    .chat-assistant {
        background-color: #f1f3f4;
        padding: 12px;
        border-radius: 10px;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">🤖 AI Meeting Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Transcribe • Summarize • Extract Insights • Chat with your Meeting'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    language = st.selectbox(
        "Select Language",
        ["english", "hinglish"]
    )

    st.divider()

    st.info(
        "You can provide a YouTube URL or a local audio/video file path."
    )

    if st.button("🗑️ Clear Results"):
        for key in [
            "result",
            "chat_history",
            "rag_chain"
        ]:
            if key in st.session_state:
                del st.session_state[key]

        st.rerun()


# -----------------------------
# Input Section
# -----------------------------
st.subheader("🎥 Meeting / Video Input")

input_type = st.radio(
    "Choose input type",
    ["YouTube URL", "Local File"],
    horizontal=True
)

source = ""

if input_type == "YouTube URL":

    source = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=..."
    )

else:

    uploaded_file = st.file_uploader(
        "Upload audio/video file",
        type=[
            "mp3",
            "wav",
            "m4a",
            "mp4",
            "mov",
            "avi",
            "mkv"
        ]
    )

    if uploaded_file:

        import os

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        source = file_path

        st.success(
            f"Uploaded: {uploaded_file.name}"
        )


# -----------------------------
# Process Button
# -----------------------------
if st.button(
    "🚀 Process Meeting",
    type="primary",
    use_container_width=True
):

    if not source:
        st.warning(
            "Please enter a YouTube URL or upload a file."
        )

    else:

        with st.status(
            "Processing your meeting...",
            expanded=True
        ) as status:

            try:

                st.write("🎵 Processing audio/video...")
                st.write("🎙️ Transcribing...")
                st.write("🧠 Generating title...")
                st.write("📝 Creating summary...")
                st.write("✅ Extracting action items...")
                st.write("🔑 Extracting key decisions...")
                st.write("❓ Extracting open questions...")
                st.write("🔍 Building RAG system...")

                result = run_pipeline(
                    source,
                    language
                )

                st.session_state.result = result
                st.session_state.rag_chain = result["rag_chain"]
                st.session_state.chat_history = []

                status.update(
                    label="✅ Processing completed!",
                    state="complete",
                    expanded=False
                )

            except Exception as e:

                status.update(
                    label="❌ Processing failed",
                    state="error"
                )

                st.error(
                    f"Error: {str(e)}"
                )


# -----------------------------
# Display Results
# -----------------------------
if "result" in st.session_state:

    result = st.session_state.result

    st.divider()

    # Title
    st.header("📌 " + str(result["title"]))

    # -------------------------
    # Summary
    # -------------------------
    st.subheader("📝 Summary")

    st.markdown(
        f'<div class="result-box">{result["summary"]}</div>',
        unsafe_allow_html=True
    )

    # -------------------------
    # Three columns
    # -------------------------
    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("✅ Action Items")

        st.markdown(
            f'<div class="result-box">'
            f'{result["action_items"]}'
            f'</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.subheader("🔑 Key Decisions")

        st.markdown(
            f'<div class="result-box">'
            f'{result["key_decisions"]}'
            f'</div>',
            unsafe_allow_html=True
        )

    with col3:

        st.subheader("❓ Open Questions")

        st.markdown(
            f'<div class="result-box">'
            f'{result["open_questions"]}'
            f'</div>',
            unsafe_allow_html=True
        )

    # -------------------------
    # Transcript
    # -------------------------
    st.divider()

    st.subheader("📜 Full Transcript")

    with st.expander("Show Transcript"):

        st.text_area(
            "Transcript",
            result["transcript"],
            height=500,
            label_visibility="collapsed"
        )

        st.download_button(
            label="⬇️ Download Transcript",
            data=result["transcript"],
            file_name="transcript.txt",
            mime="text/plain"
        )

    # -------------------------
    # Chat
    # -------------------------
    st.divider()

    st.header("💬 Chat with your Meeting")

    st.caption(
        "Ask questions about the transcript using RAG."
    )

    # Initialize history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display previous messages
    for message in st.session_state.chat_history:

        if message["role"] == "user":

            st.markdown(
                f'<div class="chat-user">'
                f'👤 <b>You:</b> {message["content"]}'
                f'</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f'<div class="chat-assistant">'
                f'🤖 <b>Assistant:</b> {message["content"]}'
                f'</div>',
                unsafe_allow_html=True
            )

    # Chat input
    question = st.chat_input(
        "Ask something about the meeting..."
    )

    if question:

        # Display user message
        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })

        try:

            with st.spinner("🤔 Thinking..."):

                answer = ask_question(
                    st.session_state.rag_chain,
                    question
                )

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": answer
            })

            st.rerun()

        except Exception as e:

            st.error(
                f"Error while answering: {str(e)}"
            )