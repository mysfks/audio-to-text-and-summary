# Audio Transcription and Summarization

This project is designed to transcribe audio files into text, correct the text for common errors, and then summarize the text. It is implemented using Python and the OpenAI API.

## Features

- **Audio Transcription**: Converts audio files to text using the `whisper-1` model.
- **Text Correction**: Corrects common spelling and grammar errors.
- **Text Summarization**: Summarizes the corrected text using the OpenAI API.

## Requirements

- Python 3.x
- `openai` Python library
- `python-dotenv` Python library
- `nltk` Python library
- `spellchecker` Python library
- OpenAI API key

## Installation

1. **Install Dependencies**:
   ```bash
   pip install openai python-dotenv nltk spellchecker


2. **Create a .env File**:
    ```bash
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

3. **Download NLTK Data**:
    ```bash
    import nltk

    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    ```

## Usage
1. **Transcribe the Audio File:**
Use the audios/sia.mp3 file to transcribe the audio into text. The resulting text will be saved to results/sia_transcription.txt.

2. **Correct the Text:**
Add your text correction rules to the correct_common_errors function. The corrected text will be saved to correct_results/corrected_sia_transcription.txt.

3. **Summarize the Text:**
Use the OpenAI API to summarize the corrected text. The summary will be saved to summaries/sia_summary.txt.

## File Structure
    audios/ - Directory for audio files
    results/ - Directory for transcription results
    correct_results/ - Directory for corrected text results
    summaries/ - Directory for summaries
