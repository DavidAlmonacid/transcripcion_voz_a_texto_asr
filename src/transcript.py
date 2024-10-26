import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def get_audio_transcript(filename: str):
    try:
        with open(filename, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(filename, file.read()),
                model="whisper-large-v3",
                language="es",
                temperature=0.0,
                prompt="Audio de un docente impartiendo una clase universitaria",
            )

            transcript = transcription.text.strip()
            file.close()

            return (transcript, get_synthesis_text(transcript))

    except FileNotFoundError as e:
        print(f"get_audio_transcript: FileNotFoundError: {e}")
        return None

    except Exception as e:
        print(f"get_audio_transcript: Exception: {e}")
        return None


def get_synthesis_text(text: str) -> str:
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente virtual que ayuda a los estudiantes universitarios a resumir un texto de una clase universitaria en el idioma Español latinoamericano. NO intentes resolver lo que contiene el texto, sino resumir en un texto corto, simple y claro, el texto que te provea el usuario. El usuario solamente quiere el resumen del texto, NO quiere más texto adicional aparte del resumen del texto. Intenta tomar el contexto del texto original (el que te provea el usuario), e intenta mejorar la calidad de la respuesta del resumen. Por favor, ayuda al usuario con esto.",
            },
            {
                "role": "user",
                "content": "Un concepto clave durante la actividad de codificación (y uno de los aspectos del que más se habla en la XP) es la programación por parejas. XP recomienda que dos personas trabajen juntas en una estación de trabajo con el objeto de crear código para una historia. Esto da un mecanismo para la solución de problemas en tiempo real (es frecuente que dos cabezas piensen más que una) y para el aseguramiento de la calidad también en tiempo real (el código se revisa conforme se crea). También mantiene a los desarrolladores centrados en el problema de que se trate. En la práctica, cada persona adopta un papel un poco diferente. Por ejemplo, una de ellas tal vez piense en los detalles del código de una porción particular del diseño, mientras la otra se asegura de que se siguen los estándares de codificación (parte necesaria de XP) o de que el código para la historia satisfará la prueba unitaria desarrollada a fin de validar el código confrontándolo con la historia.",
            },
            {
                "role": "assistant",
                "content": "La programación por parejas en XP consiste en que dos personas trabajen juntas en una estación para crear código, lo que facilita la resolución de problemas y asegura la calidad en tiempo real. Cada miembro tiene un rol diferente, como enfocarse en los detalles del código o verificar que se sigan los estándares y que el código pase las pruebas unitarias",
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content.strip()
