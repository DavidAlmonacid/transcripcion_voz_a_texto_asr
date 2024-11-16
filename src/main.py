from os.path import dirname, join
from os.path import exists as file_exists

from fastapi import FastAPI

from get_audio import get_audio
from transcript import get_audio_transcript

app = FastAPI()


@app.get("/api/audio/{audio_id}")
def get_audio_transcription(audio_id: str):
    formatted_audio_id = audio_id[0:-4].split(".m4a")[0]

    if audio_id != f"{formatted_audio_id}.m4a":
        return {
            "message": "Invalid audio id",
        }

    get_audio(audio_id)

    filename = join(dirname(__file__), "audio", audio_id)
   
    # Para hacer pruebas locales
    # filename = join(dirname(__file__), "audio", "voz-docente-2.m4a")

    if not file_exists(filename):
        return {
            "message": "The audio file does not exist",
        }

    try:
        transcript, synthesis = get_audio_transcript(filename)

        print(
            {
                "transcript": transcript,
                "synthesis": synthesis,
            }
        )

    except Exception:
        return {
            "message": "Error getting the audio transcript",
        }

    return {
        # "transcript": transcript,
        "message": synthesis,
    }
