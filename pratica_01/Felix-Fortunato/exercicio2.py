# Exercício 2: Calculadora de Freelancer (Matemática)

valor_hora = float(input("Digite o valor cobrado por hora: "))
horas = float(input("Digite a quantidade de horas estimadas: "))

valor_bruto = horas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print("\n--- Resultado ---")
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Impostos (15%): R$ {impostos:.2f}")
print(f"Valor líquido: R$ {valor_liquido:.2f}")