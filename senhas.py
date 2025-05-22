import secrets
import string
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

CAMINHO = Path(__file__).parent / "senha_salva.txt"

digitos = (string.ascii_letters + string.digits + string.punctuation)

def gerar_e_salvar_senha():
    try:
        tamanho_senha_str = entrada_tam.get()
        tamanho_senha = int(tamanho_senha_str)

        if tamanho_senha <= 0:
            messagebox.showerror("Erro", "Por favor, digite um número inteiro positivo para o tamanho da senha.")
            return

        senha = ''.join(secrets.choice(digitos) for _ in range(tamanho_senha))
        label_senha_gerada.config(text=f"Sua senha é: {senha}")
        with open(CAMINHO, 'w') as arquivo:
            arquivo.write(f'Senha:  {senha}\n')
            arquivo.write(f'Sua senha tem {tamanho_senha} caracteres')

        messagebox.showinfo("Sucesso", f"Senha gerada e salva em '{CAMINHO.name}'!")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número inteiro válido para o tamanho da senha.")
    except Exception as e:
        messagebox.showerror("Erro inesperado", f"Ocorreu um erro: {e}")


janela = tk.Tk()
janela.title('Gerador de Senhas')
janela.geometry('400x350')

label_tam = tk.Label(janela, text='Tamanho da senha:')
label_tam.pack(pady=10)

entrada_tam = tk.Entry(janela, width=30)
entrada_tam.pack(pady=10)

botao = tk.Button(janela, text="Gerar Senha", command=gerar_e_salvar_senha)
botao.pack(pady=20)

label_senha_gerada = tk.Label(janela, text="Sua senha aparecerá aqui", wraplength=350, font=('Arial', 12, 'bold'))
label_senha_gerada.pack(pady=10)

janela.mainloop()



'''
Resultados e conclusão com esse código:
    Estudos das bibliotecas string e screts para uso no projeto, realizei a leitura da documentação
para ver os possiveis casos. Aprendi a usar o _ junto ao for e assim conseguindo concatenar a string dos 
aleatorios dentro de uma so string vazia como na linha 6. Portando, esse projeto é básico mas serviu para 
eu comecar a desenvolver projetos sozinho e buscar soluçoes para possiveis problemas existentes.
Principais aprendizados:
  - Aprendizado das bibliotecas Secrets e string
  - Criando e escrevendo em arquivo na pratica
  - Usando try/except para tratar erro de entrada de dados 
  - Aprendendo a mexer com caminho de arquivos

ASS: Matheus Figueira Merlos

'''