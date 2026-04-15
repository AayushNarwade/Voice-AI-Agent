import streamlit as st
import os
from audiorecorder import audiorecorder

from modules.stt.stt import transcribe_audio
from modules.llm.llm import process_with_llm
from modules.tools.executor import execute_action


st.set_page_config(page_title="Voice AI Agent", layout="wide")

st.title("🤖 Voice AI Chat Agent")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_audio_hash" not in st.session_state:
    st.session_state.last_audio_hash = None


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


st.divider()
st.subheader("🎤 Give Command")

col1, col2 = st.columns(2)

audio_path = None



with col1:
    audio = audiorecorder("🎙️ Click to Record", "Recording...")

    if len(audio) > 0:
        os.makedirs("data/temp_audio", exist_ok=True)
        audio_path = "data/temp_audio/recorded.wav"
        audio.export(audio_path, format="wav")

        # Unique audio fingerprint
        audio_hash = hash(audio.raw_data)

        if st.session_state.last_audio_hash != audio_hash:

            st.session_state.last_audio_hash = audio_hash

            with st.spinner("Processing..."):

                
                stt_result = transcribe_audio(audio_path)


                if "error" in stt_result:
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": f"❌ {stt_result['error']}"
                    })
                    st.rerun()

                transcription = stt_result["transcription"]

                st.session_state.messages.append({
                    "role": "user",
                    "content": f"🎤 {transcription}"
                })


                llm_result = process_with_llm(transcription)

                if "error" in llm_result:
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": f"❌ {llm_result['error']}"
                    })
                else:
                    assistant_msg = f"""
🧾 **Transcription:**
{transcription}

🧠 **Intent:**
{llm_result['intent']}
"""
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": assistant_msg
                    })

                  
                    tool_result = execute_action(llm_result)

                    if "error" in tool_result:
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": f"❌ {tool_result['error']}"
                        })
                    else:
                        output_msg = "✅ **Execution Completed**\n\n"

                        if "path" in tool_result:
                            output_msg += f"📂 File saved at:\n`{tool_result['path']}`\n\n"

                        if "summary" in tool_result:
                            output_msg += f"📝 **Summary:**\n{tool_result['summary']}\n\n"

                        if "response" in tool_result:
                            output_msg += f"💬 {tool_result['response']}"

                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": output_msg
                        })

            st.rerun()



with col2:
    uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

    if uploaded_file:
        os.makedirs("data/temp_audio", exist_ok=True)
        audio_path = os.path.join("data/temp_audio", uploaded_file.name)

        with open(audio_path, "wb") as f:
            f.write(uploaded_file.read())



if st.button("🚀 Send"):

    if not audio_path:
        st.error("Please upload an audio file")
    else:
        with st.spinner("Processing..."):

           
            stt_result = transcribe_audio(audio_path)

            # ✅ Silent handling
            if "error" in stt_result:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"❌ {stt_result['error']}"
                })
                st.rerun()

            transcription = stt_result["transcription"]

            
            st.session_state.messages.append({
                "role": "user",
                "content": f"🎤 {transcription}"
            })

            
            llm_result = process_with_llm(transcription)

            if "error" in llm_result:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"❌ {llm_result['error']}"
                })
            else:
                assistant_msg = f"""
🧾 **Transcription:**
{transcription}

🧠 **Intent:**
{llm_result['intent']}
"""
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_msg
                })

                
                tool_result = execute_action(llm_result)

                if "error" in tool_result:
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": f"❌ {tool_result['error']}"
                    })
                else:
                    output_msg = "✅ **Execution Completed**\n\n"

                    if "path" in tool_result:
                        output_msg += f"📂 File saved at:\n`{tool_result['path']}`\n\n"

                    if "summary" in tool_result:
                        output_msg += f"📝 **Summary:**\n{tool_result['summary']}\n\n"

                    if "response" in tool_result:
                        output_msg += f"💬 {tool_result['response']}"

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": output_msg
                    })

        st.rerun()