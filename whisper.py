from dotenv import load_dotenv
import os
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key=api_key

audio_file = open('audios/sia.mp3', 'rb')
transcription = openai.Audio.transcribe(
  model="whisper-1",
  file=audio_file
)

transcription_text = transcription.text
print(transcription.text)

output_file_path = "results/sia_transcription.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(transcription_text)
