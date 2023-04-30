# ElevenLabs-API-CSV-to-audio-files
This script takes a list of sentences from a CSV file and generates audio files for each sentence using the ElevenLabs Text-to-Speech API. The generated audio files are saved in MP3 format with sanitized filenames based on the input text.

Features:

Reads sentences from a CSV file
Generates audio using the ElevenLabs Text-to-Speech API
Saves audio files in MP3 format
Sanitizes filenames to remove unsupported characters


Usage:

Set your ElevenLabs API key in the script by replacing "your_api_key" in the set_api_key function call.
Add your desired sentences to a CSV file, with each sentence separated by a comma.
Update the input CSV file path in the script if needed.
Run the script, and it will generate MP3 files for each sentence in the CSV file.

Dependencies:

Python 3.x
requests
elevenlabs
Note: This script uses the ElevenLabs Text-to-Speech API, which requires an API key. Make sure to obtain an API key before using the script.
