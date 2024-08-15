import openai
import nltk
from spellchecker import SpellChecker
import re
from nltk.corpus import wordnet
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def read_text_file(file_path):  
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def correct_common_errors(text):
    common_mistakes = {
        "İtügen": "İTÜ Gemi"
    }
    
    words = text.split()
    corrected_words = [common_mistakes.get(word, word) for word in words]
    corrected_text = " ".join(corrected_words)
    return corrected_text

def improve_text_with_gpt(text, api_key):
    openai.api_key = api_key
    
    prompt = f"Aşağıdaki metni kısaltmadan hatalar varsa bu hataları düzelt:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sen yardımcı bir asistansın."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4096,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    improved_text = response['choices'][0]['message']['content'].strip()
    return improved_text

def write_text_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

input_file_path = 'results/sia_transcription.txt'
output_file_path = 'correct_results/corrected_sia_transcription.txt'

transcription_text = read_text_file(input_file_path)
transcription_text = correct_common_errors(transcription_text)

api_key = api_key
improved_text = improve_text_with_gpt(transcription_text, api_key)

write_text_file(output_file_path, improved_text)