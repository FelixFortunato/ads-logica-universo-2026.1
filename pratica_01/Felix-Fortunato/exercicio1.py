# Exercício 1: O Registro do Sistema (I/O e Tipagem)

def Registro_de_Usuario():
   nome = input ("Digite seu nome:\n")
   ano_de_nascimento = int(input("Digite seu ano de nascimento:\n"))
   altura = float(input("Digite sua altura:\n"))
   print(f"Olá, {nome}! Você tem {abs(ano_de_nascimento - 2026)} anos e sua altura é {altura:.2f}m. Registro concluido")

Registro_de_Usuario()