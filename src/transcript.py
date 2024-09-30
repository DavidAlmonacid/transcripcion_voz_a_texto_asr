import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def get_audio_transcript(filename: str) -> str:
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
        return transcript if len(transcript) < 75 else get_synthesis_text(transcript)


def get_synthesis_text(text: str) -> str:
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente virtual que ayuda a los usuarios a resumir o dar una síntesis detallada de lo que trata un texto de una clase universitaria en el idioma Español. El usuario solamente quiere la síntesis del texto, NO quiere más texto adicional aparte de la síntesis del texto. Por favor, ayuda al usuario con esto.",
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
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content.strip()


if __name__ == "__main__":
    transcript_message = get_audio_transcript("/audio/voz-docente.mp3")
    print(transcript_message)
