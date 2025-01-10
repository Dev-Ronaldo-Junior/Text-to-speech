import pyttsx3

# Inicializa o motor de texto para fala
engine = pyttsx3.init()

def configurar_engine(voice_id):
    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1)

def falar(texto):
    engine.say(texto)
    engine.runAndWait()