import requests
import json
import re
import csv
from elevenlabs import generate, play
from elevenlabs import set_api_key

set_api_key("<Your API key")


def clean_filename(filename: str) -> str:
    return re.sub(r'[\\/:"*?<>|]+', "", filename)


# Replace name of the csv file with your filename
with open("sentences_list.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    sentences = next(reader)

for i, sentence in enumerate(sentences):
    sentence = sentence.strip()
#You can replace voice here
    voice = "Elli"
    audio = generate(
        text=f"{sentence}",
        voice=voice
    )

    safe_filename = clean_filename(sentence)
    with open(f"{safe_filename}.mp3", "wb") as f:
        f.write(audio)
    print(f"Created audio file for sentence: {sentence}")
