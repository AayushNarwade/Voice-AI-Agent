import os
from groq import Groq
from dotenv import load_dotenv
from pydub import AudioSegment

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# -------------------------------
# Helper: Convert & Standardize Audio
# -------------------------------
def preprocess_audio(file_path):
    """
    Converts audio to WAV, mono, 16kHz
    Returns processed file path
    """

    try:
        audio = AudioSegment.from_file(file_path)

        # Standardize audio
        audio = audio.set_frame_rate(16000).set_channels(1)

        processed_path = "data/temp_audio/processed.wav"
        os.makedirs(os.path.dirname(processed_path), exist_ok=True)

        audio.export(processed_path, format="wav")

        return processed_path

    except Exception as e:
        return {"error": f"Audio preprocessing failed: {str(e)}"}


# -------------------------------
# Main STT Function
# -------------------------------
def transcribe_audio(file_path):

    # Step 1: Validate input
    if not file_path:
        return {"error": "No audio file provided"}

    try:
        # Step 2: Preprocess audio
        processed_path = preprocess_audio(file_path)

        if isinstance(processed_path, dict) and "error" in processed_path:
            return processed_path

        # Step 3: Send to Groq Whisper API
        with open(processed_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3"
            )

        transcription = response.text
        clean_text = transcription.strip()

        # -------------------------------
        # Step 4: Strong Validation (FIX)
        # -------------------------------
        meaningless_tokens = [".", "...", ",", "?", "!", "-", "_"]

        if (
            not clean_text
            or clean_text in meaningless_tokens
            or len(clean_text) < 2
        ):
            return {"error": "Did not understand the input"}

        # Step 5: Return clean text
        return {
            "transcription": clean_text
        }

    except Exception as e:
        return {"error": f"STT failed: {str(e)}"}