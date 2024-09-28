import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

filename = os.path.dirname(__file__) + "/sample_audio.m4a"
