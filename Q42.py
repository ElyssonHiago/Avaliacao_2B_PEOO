Audiencia = {"4": 0, "5": 0, "7": 0, "12": 0}

ContadorDeCanais = 0

while ContadorDeCanais < 10:
    canal = input("Digite o número do canal: ")
    
    if canal.lower() == 'sair':
        break
    
    if canal not in Audiencia:
        print("Canal inválido! Tente novamente.")
        continue
    
    try:
        AudienciaDoCanal = int(input(f"Quantas pessoas estavam assistindo ao canal {canal}: "))
        
        Audiencia[canal] += AudienciaDoCanal
        
        ContadorDeCanais += 1
    except ValueError:
        print("Digite um número válido de pessoas.")
        
Audiencia_total = sum(Audiencia.values())

for canal, pessoas in Audiencia.items():
    if Audiencia_total > 0:
        porcentagem = (pessoas / Audiencia_total) * 100
    else:
        porcentagem = 0
    print(f"Canal {canal}: {porcentagem:.2f}% da audiência total.")

print("Programa encerrado.")