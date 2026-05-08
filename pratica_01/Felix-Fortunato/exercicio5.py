# Exercício 5: Desafio do Download (Mistura de Conceitos)

tamanho_do_arquivo = float(input("Digite o tamanho do seu arquivo (MB): "))
velocidade_mbps = float(input("Digite a velocidade da sua internet (Mbps): "))

tempo_segundos = tamanho_do_arquivo / (velocidade_mbps / 8)

minutos = int(tempo_segundos // 60)
segundos = int(tempo_segundos % 60)


print(f"Seu download levará {minutos} minutos e {segundos} segundos")