from view.main_view import criar_interface
from models.engine import configurar_engine, falar, engine
from models.language_detection import detectar_idioma
from tkinter import messagebox
import asyncio

async def processar_texto(text_entry):
    texto_original = text_entry.get("1.0", "end").strip()

    if not texto_original:
        messagebox.showwarning("Atenção", "Por favor, insira algum texto para ser processado.")
        return

    try:
        idioma_detectado = await detectar_idioma(texto_original)

        voices = engine.getProperty('voices')
        if idioma_detectado == 'en':
            voice_id = voices[1].id
        else:
            voice_id = voices[0].id

        configurar_engine(voice_id)
        falar(texto_original)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def executar_main(text_entry):
    asyncio.run(processar_texto(text_entry))

if __name__ == "__main__":
    criar_interface(executar_main)