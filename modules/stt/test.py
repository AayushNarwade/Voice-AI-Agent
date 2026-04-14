from stt import transcribe_audio
file_path = "D:/Study/voice-ai-agent/data/temp_audio/Sample.mp3"

result = transcribe_audio(file_path)

print("OUTPUT:")
print(result)