"""
MP4_AUDIO_A TEXTO
"""

#!/usr/bin/env python
# coding: utf-8

# In[6]:


from moviepy.editor import VideoFileClip
import speech_recognition as sr

# Paso 1: Extraer el audio del video y guardarlo como archivo WAV
def extraer_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"  # Ruta y nombre del archivo de audio temporal
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')  # Especifica codec para formato WAV
    video.close()
    return audio_path

# Paso 3: Transcribir el audio a texto
def transcribir_audio(audio_path):
    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()
    # Cargar el archivo de audio
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    # Intentar reconocer el audio utilizando el reconocedor de Google
    try:
        text = recognizer.recognize_google(audio_data, language="es-ES")  # Asumiendo español como idioma
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition no pudo entender el audio"
    except sr.RequestError as e:
        return f"No se pudo solicitar resultados desde Google Speech Recognition service; {e}"

# Ruta al video MP4
video_path = "C:\\Users\\HP\\Videos\\Movavi Screen Recorder\\VIDEO 1 ELEGIR EL TEMA.mp4"

# Ejecutar las funciones
audio_path = extraer_audio(video_path)
texto_transcrito = transcribir_audio(audio_path)
print(texto_transcrito)



# In[ ]:






if __name__ == "__main__":
    pass
