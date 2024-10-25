import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def get_audio(source_file: str):
    try:
        os.makedirs(
            os.path.join(os.path.dirname(__file__), "audio"),
            exist_ok=True,
        )

        destination_file = os.path.join(
            os.path.dirname(__file__),
            "audio",
            source_file,
        )

        with open(destination_file, "wb+") as f:
            res = supabase.storage.from_("audios").download(source_file)
            f.write(res)
            f.close()

    except FileNotFoundError as e:
        print(f"get_audio: FileNotFoundError: {e}")
        return None
