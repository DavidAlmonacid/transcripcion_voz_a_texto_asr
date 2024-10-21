from fastapi import FastAPI
import os

from transcript import get_audio_transcript

app = FastAPI()

# filename = os.path.dirname(__file__) + "/audio/voz-docente-005.m4a"
# transcript, final_transcript = get_audio_transcript(filename)

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/audio/{audio_id}")
def read_root(audio_id: str):
    filename = os.path.dirname(__file__) + f"/audio/{audio_id}.m4a"
    transcript, final_transcript = get_audio_transcript(filename)
    
    return {
        "original_transcription": transcript,
        "final_transcription": final_transcript,
    }
