import os
from os.path import abspath, dirname, join

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

            synthesis = (
                transcript if len(transcript) <= 90 else get_synthesis_text(transcript)
            )

            return (transcript, synthesis)

    except FileNotFoundError as e:
        print(f"get_audio_transcript: FileNotFoundError: {e}")
        return None

    except Exception as e:
        print(f"get_audio_transcript: Exception: {e}")
        return None

    finally:
        audio_dir = join(dirname(__file__), "audio")
        audio_dir = abspath(audio_dir)  # Convertir a ruta absoluta

        for filename in os.listdir(audio_dir):
            file_path = join(audio_dir, filename)
            file_path = abspath(file_path)  # Convertir a ruta absoluta

            if not file_path.startswith(audio_dir):
                print(f"Skipping potentially unsafe path: {file_path}")
                continue

            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")


def get_synthesis_text(text: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
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
                "content": "Ya abrí la aplicación XAMPP, estoy en el panel de control, ya activé los servicios de Apache, ya activé el servicio de MySQL, aunque este no es necesario para lo que estamos haciendo, MySQL no es necesario porque yo no voy a trabajar con bases de datos.",
            },
            {
                "role": "assistant",
                "content": "El docente está explicando la configuración inicial de XAMPP, donde se activan los servicios de Apache y MySQL, aunque este último no es necesario para la actividad que se está realizando.",
            },
            {
                "role": "user",
                "content": "A los de tecnología les toca así, el sistema funciona en un momento y en un momento pum, cinco, seis de la tarde, un sábado, un domingo, y si no funciona, ¿qué hacen? Pues te van a llamar. Ya le mandamos el carro, tranquilo, ya va para allá el carro, va con él, entonces lo recogemos, va por el bicho, ya está bajo, se cayó el sistema, toca montarlo ya. llevese eso aquí en la cabeza nosotros no somos públicos que de 8 a 5 y chao 8 entramos aquí nos sacan si a las 5 o 6 todo está bien nos vamos pero usted tiene que llevarse eso en la cabeza si no va a perder el año acuérdense que cuando usted empieza a armar la oferta de vida lo que le evaluan a uno es que ya van a ser ingresados es la continuidad de tiempo y la cantidad mínima de una empresa son dos años. Si usted ve una hoja de vida y le muestra a la persona dos meses aquí, tres meses aquí, cuatro meses aquí, no, pero este man que.",
            },
            {
                "role": "assistant",
                "content": "El docente está hablando sobre la responsabilidad de los profesionales de tecnología, quienes deben estar disponibles para solucionar problemas en cualquier momento, incluso los fines de semana. Además, menciona la importancia de la continuidad laboral para ser considerado por una empresa.",
            },
            {
                "role": "user",
                "content": "Primero, vamos a abrir el simulador de red Cisco Packet Tracer. Una vez dentro, seleccionamos un switch desde el panel de dispositivos y lo arrastramos al área de trabajo. Ahora, necesitamos agregar dos computadoras para la simulación. Recuerden que cada dispositivo en una red necesita una dirección IP, así que antes de conectar los cables, configuraremos las IPs.",
            },
            {
                "role": "assistant",
                "content": "El docente está explicando cómo configurar una red en Cisco Packet Tracer, donde se selecciona un switch y dos computadoras para la simulación. Antes de conectar los cables, se deben configurar las direcciones IP de los dispositivos.",
            },
            {
                "role": "user",
                "content": "En la primera computadora, abrimos la pestaña Desktop, luego hacemos clic en IP Configuration. Asignaremos la dirección IP 192.168.1.2 con la máscara de subred 255.255.255.0. En la segunda computadora haremos lo mismo, pero usaremos la IP 192.168.1.3.",
            },
            {
                "role": "assistant",
                "content": "Para configurar las direcciones IP en las computadoras, se debe acceder a la pestaña Desktop y luego a IP Configuration. La primera computadora tendrá la IP.",
            },
            {
                "role": "user",
                "content": "En esta sesión hablaremos del concepto de separación de poderes en un estado democrático. Este principio, que Montesquieu popularizó, establece que el poder del estado debe dividirse en tres ramas: legislativa, ejecutiva y judicial, para evitar la concentración de poder en una sola entidad. Por ejemplo, en muchos países, el Congreso o Parlamento es quien elabora las leyes (poder legislativo), el Presidente o Primer Ministro las ejecuta (poder ejecutivo) y los jueces interpretan y aplican esas leyes (poder judicial). Este sistema busca mantener un equilibrio entre las ramas y garantizar los derechos fundamentales de los ciudadanos.",
            },
            {
                "role": "assistant",
                "content": "El docente está explicando el concepto de separación de poderes en un estado democrático, donde el poder se divide en tres ramas: legislativa, ejecutiva y judicial. Cada rama tiene funciones específicas para evitar la concentración de poder y garantizar los derechos de los ciudadanos.",
            },
            {
                "role": "user",
                "content": "Hoy vamos a trabajar en el análisis de mercado para evaluar la viabilidad de sus ideas de negocio. Recuerden que un análisis de mercado nos ayuda a entender a nuestros posibles clientes, a identificar a los competidores y a encontrar un espacio en el mercado donde podamos diferenciarnos. Por ejemplo, si quiero emprender con una cafetería, debo investigar: ¿quiénes son los clientes? ¿Prefieren un café rápido o buscan una experiencia más relajada? También debo observar a los competidores: ¿qué están haciendo? ¿Qué puedo ofrecer que sea diferente? Si mis competidores usan granos de café convencionales, tal vez yo pueda ofrecer opciones orgánicas o especiales. Para la actividad de hoy, definan quién sería su cliente ideal y escriban tres formas en las que su negocio puede destacarse. Luego lo discutiremos en grupo.",
            },
            {
                "role": "assistant",
                "content": "El docente está explicando la importancia del análisis de mercado para evaluar la viabilidad de un negocio. Este análisis ayuda a comprender a los clientes, identificar a los competidores y encontrar un espacio diferenciado en el mercado. Por ejemplo, si se quiere emprender una cafetería, se debe investigar las preferencias de los clientes y las estrategias de los competidores para ofrecer algo único.",
            },
            # Añadir de aqui para abajo
            # Añadir de aqui para arrriba
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
