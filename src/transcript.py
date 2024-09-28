import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

filename = os.path.dirname(__file__) + "/sample_audio.m4a"

"""
Tengo el siguiente texto:

"Mensaje transcrito"

Quiero que me hagas una síntesis o un resumen detallado de lo que trata el texto que te estoy enviando.

Solo quiero la síntesis del texto, NO quiero más texto, aparte de la sintesis del texto enviado.
"""
