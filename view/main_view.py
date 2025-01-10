import tkinter as tk
import os

def criar_interface(executar_main):
    # Configuração da interface gráfica
    app = tk.Tk()
    app.title("Digite seu texto para a reprodução")
    app.geometry("400x300")

    # Obtenha o caminho absoluto baseado no diretório do script
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_imagem = os.path.join(diretorio_atual, '..', 'image', 'leao.ico')

    # Configurar o ícone usando o caminho da imagem
    try:
        app.iconbitmap(caminho_imagem)
    except Exception as e:
        print(f"Não foi possível carregar o ícone: {e}")

    # Layout do texto
    text_label = tk.Label(app, text="Insira o texto que você quer que seja dito:")
    text_label.pack(pady=(10, 5))

    # Caixa de Texto Responsiva
    text_entry = tk.Text(app, height=10)
    text_entry.pack(expand=True, fill='both', padx=10, pady=5)

    # Botão de processamento
    process_button = tk.Button(app, text="Falar Texto", command=lambda: executar_main(text_entry))
    process_button.pack(pady=(5, 10))

    # Rodar a aplicação
    app.mainloop()