# import os

from fastapi import FastAPI

# from transcript import get_audio_transcript

app = FastAPI()

# filename = os.path.dirname(__file__) + "/audio/voz-docente-005.m4a"
# transcript, final_transcript = get_audio_transcript(filename)

@app.get("/api/audio/debug/{audio_id}")
def get_audio_transcription_debug(audio_id: str):
    return {
        "result": f"Hello {audio_id}",
    }


@app.get("/api/audio/{audio_id}")
def get_audio_transcription(audio_id: str):
    #filename = os.path.dirname(__file__) + f"/audio/{audio_id}.m4a"
    #transcript, final_transcript = get_audio_transcript(filename)

    # return {
    #     "original_transcription": transcript,
    #     "final_transcription": final_transcript,
    # }

    return {
        "message": f"Hello {audio_id}",
    }
