Repeticoes = 0

while Repeticoes < 1000:
    print("Menu de opções:")
    print("1º Novo salário")
    print("2º Férias")
    print("3º Décimo terceiro")
    print("4º Sair")
    
    opcao = input("Digite a opção escolhida: ")
    
    if opcao == '1':
        try:
            salario = float(input("Digite o salário do funcionário: R$ "))
            
            if salario <= 210:
                aumento = salario * 0.15
            elif 210 < salario <= 600:
                aumento = salario * 0.10
            else:
                aumento = salario * 0.05
            
            novo_salario = salario + aumento
            
            print(f"Novo salário do funcionário: R$ {novo_salario:.2f}")
        except ValueError:
            print("Entrada inválida! Verifique se foi inserido um valor válido.")
    elif opcao == '2':
        try:
            salario = float(input("Digite o salário do funcionário: R$ "))
            valor_ferias = salario + (salario / 3)
            
            print(f"Valor das férias do funcionário: R$ {valor_ferias:.2f}")
        except ValueError:
            print("Entrada inválida! Verifique se foi inserido um valor válido.")
    elif opcao == '3':
        try:
            salario = float(input("Digite o salário do funcionário: R$ "))
            meses_trabalho = int(input("Digite o número de meses de trabalho (até 12): "))
            
            if meses_trabalho > 12:
                print("Número de meses de trabalho inválido! Deve ser no máximo 12.")
            else:
                decimo_terceiro = (salario * meses_trabalho) / 12
                print(f"Décimo terceiro do funcionário: R$ {decimo_terceiro:.2f}")
        except ValueError:
            print("Entrada inválida! Verifique se foi inserido valores válidos.")
    elif opcao == '4':
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida! Escolha uma opção válida.")
    
    Repeticoes += 1