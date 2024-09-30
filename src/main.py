from fastapi import FastAPI

from transcript import get_audio_transcript

app = FastAPI()

# filename = os.path.dirname(__file__) + "/audio/voz-docente.mp3"
transcript = get_audio_transcript("/audio/voz-docente.mp3")


@app.get("/")
def read_root():
    return {"Audio transcription": transcript}
