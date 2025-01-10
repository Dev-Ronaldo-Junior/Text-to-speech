from googletrans import Translator

async def detectar_idioma(texto):
    translator = Translator()
    resultado = await translator.detect(texto)
    return resultado.lang