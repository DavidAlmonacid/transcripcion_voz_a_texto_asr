from fastapi import FastAPI
import os

from transcript import get_audio_transcript

app = FastAPI()

filename = os.path.dirname(__file__) + "/audio/voz-docente.m4a"
transcript = get_audio_transcript(filename)


@app.get("/")
def read_root():
    return {"Audio transcription": transcript}
