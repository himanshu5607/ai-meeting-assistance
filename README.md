# 🤖 AI Meeting Assistant

An AI-powered meeting and video assistant that converts YouTube videos or uploaded audio/video files into **transcripts, summaries, action items, key decisions, and open questions**. It also allows users to **chat with the meeting using RAG (Retrieval-Augmented Generation)**.

## 🚀 Features

* 🎥 Process YouTube videos
* 📁 Upload local audio/video files
* 🎙️ Automatic speech-to-text transcription using Whisper
* 🌐 English and Hinglish language support
* 📝 AI-generated meeting summary
* 📌 Automatic title generation
* ✅ Extract action items
* 🔑 Extract key decisions
* ❓ Extract open questions
* 💬 Chat with the meeting using RAG
* 📜 View the complete transcript
* ⬇️ Download transcript
* 🌐 Streamlit web interface

---

## 🏗️ Project Architecture

```text
                    YouTube / Local File
                            │
                            ▼
                    Audio Processing
                            │
                            ▼
                       Whisper
                    Transcription
                            │
                            ▼
                       Transcript
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
           Summary      Information      RAG
                         Extraction       Engine
              │             │              │
              ▼             ▼              ▼
           Summary     ┌─────┴─────┐    AI Chat
                       │     │     │
                       ▼     ▼     ▼
                    Actions Decisions Questions
```

---

## 📂 Project Structure

```text
ai-meeting-assistance/
│
├── app.py                  # Streamlit UI
├── main.py                 # Main AI pipeline
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed)
├── .gitignore
│
├── core/
│   ├── transcriber.py      # Whisper transcription
│   ├── summarizer.py       # Summary and title generation
│   ├── extractor.py        # Extract actions, decisions, questions
│   └── rag_engine.py       # RAG and question answering
│
├── utils/
│   ├── audio_processor.py  # Audio/video processing
│   └── ...
│
├── downloads/              # Downloaded media files
└── uploads/                # Uploaded files
```

---

## 🛠️ Technologies Used

| Technology    | Purpose                                 |
| ------------- | --------------------------------------- |
| Python        | Main programming language               |
| Streamlit     | Web interface                           |
| Whisper       | Speech-to-text transcription            |
| yt-dlp        | YouTube video/audio downloading         |
| Pydub         | Audio processing                        |
| LangChain     | LLM/RAG framework                       |
| ChromaDB      | Vector database                         |
| Mistral / LLM | AI summarization and question answering |
| python-dotenv | Environment variable management         |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/himanshu5607/ai-meeting-assistance.git
cd ai-meeting-assistance
```

### 2. Create a virtual environment

Using `uv`:

```bash
uv venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key
MISTRAL_API_KEY=your_api_key
```

Add `.env` to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
downloads/
uploads/
```

**Never commit your API keys to GitHub.**

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Or:

```bash
python -m streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 🎥 How to Use

### Step 1 — Select Input

Choose either:

```text
YouTube URL
```

or:

```text
Local File
```

### Step 2 — Select Language

Choose:

* English
* Hinglish

### Step 3 — Process

Click:

```text
🚀 Process Meeting
```

The application will:

1. Process the video/audio
2. Extract audio
3. Transcribe the audio
4. Generate a title
5. Generate a summary
6. Extract action items
7. Extract key decisions
8. Extract open questions
9. Build the RAG pipeline

### Step 4 — Explore Results

The application displays:

* 📌 Meeting title
* 📝 Summary
* ✅ Action items
* 🔑 Key decisions
* ❓ Open questions
* 📜 Full transcript

### Step 5 — Chat With the Meeting

Use the chat box to ask questions such as:

```text
What were the main decisions?

Who was assigned the tasks?

What deadlines were discussed?

What problems were mentioned?

What did the team decide about the project?

Summarize the discussion about the database.
```

The RAG system retrieves relevant information from the transcript before generating the answer.

---

## 🧠 AI Pipeline

The main pipeline is implemented in `main.py`.

```python
def run_pipeline(source, language="english"):
    chunks = process_input(source)

    transcript = transcribe_all(
        chunks,
        language
    )

    title = generate_title(transcript)

    summary = summarize(transcript)

    action_items = extract_action_items(transcript)

    decisions = extract_key_decisions(transcript)

    questions = extract_questions(transcript)

    rag_chain = build_rag_chain(transcript)

    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "key_decisions": decisions,
        "open_questions": questions,
        "rag_chain": rag_chain,
    }
```

---

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

### 1. Push the project to GitHub

```bash
git add .
git commit -m "Deploy AI Meeting Assistant"
git push origin main
```

### 2. Connect GitHub to Streamlit

Open Streamlit Community Cloud and create a new application.

Select:

```text
Repository: himanshu5607/ai-meeting-assistance
Branch: main
Main file: app.py
```

### 3. Add Secrets

Add your API keys through Streamlit's Secrets settings instead of committing `.env`.

Example:

```toml
OPENAI_API_KEY = "your-api-key"
MISTRAL_API_KEY = "your-api-key"
```

---

## ⚠️ Deployment Notes

The application performs computationally intensive tasks such as:

* Whisper transcription
* Audio processing
* YouTube downloading
* Embedding/vector processing
* LLM inference

Long videos may require significant processing time and memory.

For production deployment, a separate backend/API architecture can be used.

---

## 🔮 Future Improvements

* 🎤 Real-time meeting transcription
* 👥 Speaker identification
* ⏱️ Timestamped transcript
* 📊 Meeting analytics
* 📧 Email action items automatically
* 📄 Export meeting report as PDF
* 🔎 Search within transcript
* 🧑‍💼 Speaker-wise summaries
* 📅 Calendar integration
* ☁️ Cloud storage for meeting history
* 🔐 User authentication
* ⚡ Background processing for long videos

---

## 📌 Example Use Cases

### Business Meetings

Automatically extract:

```text
Action Items
Decisions
Questions
Summary
```

### Online Lectures

Convert long lectures into:

```text
Transcript
Summary
Important concepts
Questions
```

### YouTube Videos

Paste a YouTube URL and ask questions about the video's content.

### Project Discussions

Identify:

```text
Tasks
Responsibilities
Deadlines
Decisions
Open Issues
```

---

## 👨‍💻 Author

**Himanshu Kumar**

GitHub:
https://github.com/himanshu5607

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
