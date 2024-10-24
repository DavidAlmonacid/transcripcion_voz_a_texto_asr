import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def get_audio(source_file: str):
    destination_file = f"audio/{source_file}.m4a"

    with open(destination_file, "wb+") as f:
        res = supabase.storage.from_("audios").get_public_url(source_file)
        f.write(res)
        f.close()


# get_audio("/audio/voz-docente.mp3", "voz-docente.mp3")
