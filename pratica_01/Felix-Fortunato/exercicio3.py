# Exercício 3: Divisão Justa (Divisão Inteira e Módulo)

total_fatias = int(input("Digite o número total de fatias: "))
programadores = int(input("Digite o número de programadores: "))

fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

print("\n--- Resultado ---")
print(f"Os programadores vão comer {fatias_por_pessoa} fatias cada. Vão sobrar {sobra} fatias na caixa")

#Engraçado como as fatias não vão pro senior