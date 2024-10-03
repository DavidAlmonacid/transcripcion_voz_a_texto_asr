from fastapi import FastAPI
import os

from transcript import get_audio_transcript

app = FastAPI()

filename = os.path.dirname(__file__) + "/audio/voz-docente-001.m4a"
transcript, final_transcript = get_audio_transcript(filename)


@app.get("/")
def read_root():
    return {
        "original_transcription": transcript,
        "final_transcription": final_transcript,
    }
