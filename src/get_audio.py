import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

res = supabase.storage.from_("audios").download()

# def get_audio(destination_file: str, source_file: str):
#     with open(destination_file, "wb+") as f:
#         res = supabase.storage.from_("bucket_name").download(source_file)
#         f.write(res)
#         f.close()


# get_audio("/audio/voz-docente.mp3", "voz-docente.mp3")
