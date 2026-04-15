# 🎙️ Voice AI Agent

A voice-controlled AI assistant that converts speech into actionable commands using Speech-to-Text (STT), Large Language Models (LLM), and local automation tools.

---

## 🚀 Features

* 🎤 **Voice Input Support**

  * Record audio in real-time
  * Upload pre-recorded audio files (WAV/MP3)

* 🧠 **Intent Detection using LLM**

  * Understands user commands from speech
  * Classifies into actions like:

    * Create file
    * Write code
    * Summarize text
    * General chat

* 🛠️ **Local Task Execution**

  * Creates files
  * Writes Python code
  * Generates summaries
  * Responds conversationally

* 💬 **Chat-Based UI**

  * Clean chatbot interface using Streamlit
  * Displays transcription, intent, and results

* ⚡ **Real-time Processing**

  * Auto-process after recording (no button needed)

* 🧯 **Robust Error Handling**

  * Handles silent audio inputs
  * Prevents invalid command execution

---

## 🧩 Tech Stack

| Component        | Technology                            |
| ---------------- | ------------------------------------- |
| STT              | Groq Whisper API (`whisper-large-v3`) |
| LLM              | Ollama (`mistral`)                    |
| Backend          | Python                                |
| UI               | Streamlit                             |
| Audio Processing | pydub, audiorecorder                  |

---

## 🤖 Model Selection: Why Mistral over LLaMA3?

During development, both **Mistral (via Ollama)** and **LLaMA3** were evaluated for intent detection and structured output generation.

### ⚖️ Key Observations

| Factor                  | Mistral         | LLaMA3                            |
| ----------------------- | --------------- | --------------------------------- |
| Response Speed          | ⚡ Faster        | Slower                            |
| Stability               | ✅ Stable        | ❌ Occasional crashes (500 errors) |
| Resource Usage          | 🟢 Lightweight  | 🔴 Heavy (high RAM/CPU usage)     |
| JSON Output Consistency | ✅ More reliable | ❌ Sometimes inconsistent          |
| Startup Time            | ⚡ Quick         | 🐢 Very slow                      |

---

### 🚨 Issues with LLaMA3

* Faced **runtime crashes (500 errors)** during inference
* High memory consumption (~4–8GB)
* Long initialization time
* Less consistent structured (JSON) outputs

---

### ✅ Why Mistral Was Chosen

* Faster inference → better real-time UX
* More stable for continuous usage
* Better at **structured JSON generation**
* Lightweight → works smoothly on local machines
* Ideal for **assignment constraints (free, local, efficient)**

---

### 🧠 Conclusion

Mistral provided a better balance of **performance, stability, and reliability**, making it more suitable for a real-time voice-based AI agent.

---

## 🏗️ Project Structure

```
voice-ai-agent/
│
├── modules/
│   ├── stt/            # Speech-to-text
│   ├── llm/            # Intent detection
│   ├── tools/          # Execution logic
│
├── prompts/            # LLM prompt templates
├── output/
│   ├── code/           # Generated code
│   ├── summaries/      # Summaries (if used)
│   ├── text/           # Created files
│
├── data/temp_audio/    # Temporary audio storage
├── app.py              # Main Streamlit app
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AayushNarwade/Voice-AI-Agent.git
cd Voice-AI-Agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Install FFmpeg (Required for Audio)

Download from: https://www.gyan.dev/ffmpeg/builds/

Add `ffmpeg/bin` to system PATH.

---

### 6️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🎯 How It Works

```
Audio Input → STT → LLM → Tool Execution → Chat Output
```

1. User gives voice input
2. Whisper converts speech → text
3. LLM detects intent
4. Tools execute the action
5. Output shown in chat UI

---

## 🧪 Example Commands

* 🎤 "Create a Python file with retry function"
* 🎤 "Summarize this paragraph..."
* 🎤 "Create a text file named notes.txt"
* 🎤 "Explain machine learning"

---

## 🧯 Edge Case Handling

* Silent audio → ❌ "Did not understand the input"
* Invalid commands → safely handled
* Prevents unintended file creation

---

## 🧠 Key Design Decisions

* Modular architecture (STT, LLM, Tools)
* Session-based memory for chat UI
* Audio preprocessing for better transcription
* Error-first handling strategy

---

## 🔮 Future Improvements

* Voice output (Text-to-Speech)
* Persistent memory
* Deployment (Streamlit Cloud / Docker)
* Improved intent classification

---

## 👨‍💻 Author

**Aayush Narwade**

* 🎤 Tech Enthusiast
* 💡 Interested in AI, Data Science & Voice Interfaces

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
