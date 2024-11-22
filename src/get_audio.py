import os
from os.path import dirname, join

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def get_audio(source_file: str):
    try:
        response_audio = supabase.storage.from_("audios").download(source_file)
    except Exception as e:
        print(f"get_audio: Error downloading the audio: {e}")
        return None

    try:
        os.makedirs(join(dirname(__file__), "audio"), exist_ok=True)

        destination_file = join(dirname(__file__), "audio", source_file)

        with open(destination_file, "wb+") as f:
            f.write(response_audio)
            f.close()

    except FileNotFoundError as e:
        print(f"get_audio: FileNotFoundError: {e}")
        return None
