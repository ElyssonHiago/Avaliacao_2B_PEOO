Repeticoes = 0

while Repeticoes < 1000:
    print("Menu de opções:")
    print("1º Média aritmética")
    print("2º Média ponderada")
    print("3º Sair")
    
    opcao = input("Digite a opção escolhida: ")
    
    if opcao == '1':
        try:
            nota1 = float(input("Digite a 1ª nota: "))
            nota2 = float(input("Digite a 2ª nota: "))
            
            media_aritmetica = (nota1 + nota2) / 2
            print(f"A média aritmética é: {media_aritmetica:.2f}")
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir números válidos.")
    elif opcao == '2':
        try:
            nota1 = float(input("Digite a 1ª nota: "))
            nota2 = float(input("Digite a 2ª nota: "))
            nota3 = float(input("Digite a 3ª nota: "))
            
            peso1 = float(input("Digite o peso da 1ª nota: "))
            peso2 = float(input("Digite o peso da 2ª nota: "))
            peso3 = float(input("Digite o peso da 3ª nota: "))
            
            soma_pesos = peso1 + peso2 + peso3
            media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / soma_pesos
            
            print(f"A média ponderada é: {media_ponderada:.2f}")
        except ValueError:
            print("Entrada inválida! Confira se foi inserido números válidos.")
    elif opcao == '3':
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
    
    Repeticoes += 1