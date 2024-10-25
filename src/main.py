from os.path import dirname, join

from fastapi import FastAPI

from get_audio import get_audio
from transcript import get_audio_transcript

app = FastAPI()


@app.get("/api/audio/{audio_id}")
def get_audio_transcription(audio_id: str):
    source_file = f"{audio_id}.m4a"

    if source_file != f"{audio_id.split('.m4a')[0]}.m4a":
        return {
            "message": "Invalid audio id",
        }

    get_audio(source_file)

    filename = join(dirname(__file__), "audio", source_file)

    try:
        transcript, synthesis = get_audio_transcript(filename)

        print(
            {
                "transcript": transcript,
                "synthesis": synthesis,
            }
        )

    except TypeError as e:
        return {
            "message": f"get_audio_transcription: TypeError: {e}",
        }

    return {
        "message": synthesis,
    }
