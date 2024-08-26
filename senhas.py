import secrets
import string
from pathlib import Path

CAMINHO = Path(__file__).parent/"senha_salva.txt"

digitos = (string.ascii_letters + string.digits + string.punctuation)

try:
  tamanho_senha = int(input('Digite o tamanho da sua senha '))
  senha = ''.join(secrets.choice(digitos) for _ in range (tamanho_senha))
  print(f'Sua senha é : {senha}')
  with open(CAMINHO,'w') as arquivo:
      arquivo.write(f'Senha:  {senha}\n')
      arquivo.write(f'Sua senha tem {tamanho_senha} caracteres')

except ValueError or TypeError: 
  print ('ERRO: Digite um valor inteiro possivel')
    





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