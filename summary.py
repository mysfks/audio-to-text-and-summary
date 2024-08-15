import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model='gpt-4-turbo',  
        messages=[
            {"role": "system", "content": "Aşağıdaki metinin her bir kelimesi paragraflar halinde özetler misin?"},
            {"role": "user", "content": text}
        ],
        max_tokens=4096, 
        temperature=0.5,  
    )
    summary = response.choices[0].message['content'].strip()
    return summary

def write_text_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

input_file_path = 'correct_results/corrected_sia_transcription.txt'
output_file_path = 'summaries/sia_summary.txt'

transcription_text = read_text_file(input_file_path)
summary = summarize_text(transcription_text)
write_text_file(output_file_path, summary)