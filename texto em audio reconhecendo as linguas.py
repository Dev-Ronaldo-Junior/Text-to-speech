import pyttsx3
from googletrans import Translator
import asyncio

# Inicializa o motor de texto para fala
engine = pyttsx3.init()

def configurar_engine(voice_id):
    # Define a voz (opcional)
    engine.setProperty('voice', voice_id)  # Altera a voz com base no ID fornecido
    engine.setProperty('rate', 190)  # Velocidade
    engine.setProperty('volume', 1)  # Volume (1.0 é o valor máximo)

def falar(texto):
    # Converte texto em fala
    engine.say(texto)
    # Aguarda até que a fala termine
    engine.runAndWait()

async def detectar_idioma(texto):
    # Cria uma instância do tradutor
    translator = Translator()
    # Detecta o idioma do texto
    resultado = await translator.detect(texto)
    return resultado.lang

async def main():
    while True:
        try:
            # Texto que você deseja que seja falado
            texto_original = input("Insira o texto que você quer que seja dito: ")
            
            # Detecta o idioma do texto
            idioma_detectado = await detectar_idioma(texto_original)
            print(f"Idioma detectado: {idioma_detectado}")

            # Obtém as vozes disponíveis
            voices = engine.getProperty('voices')

            # Define a voz com base no idioma detectado
            if idioma_detectado == 'en':  # Se o texto estiver em inglês
                voice_id = voices[1].id  # Usar a segunda voz
            else:  # Para outros idiomas (incluindo português)
                voice_id = voices[0].id  # Usar a primeira voz

            # Configura o motor com a voz escolhida
            configurar_engine(voice_id)

            # Fala o texto
            falar(texto_original)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        # Pergunta se o usuário quer tentar novamente
        resposta = input("Quer tentar de novo? (sim/não): ").strip().lower()
        if resposta != "sim":
            print("Tudo bem, obrigado pela atenção.")
            break

# Executa a função principal
if __name__ == "__main__":
    asyncio.run(main())