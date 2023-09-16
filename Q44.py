LucroTotalDaEmpresa = 0
AcoesLucroMaior1000 = 0
AcoesLucroMenor200 = 0

ContadorDeAcoes = 0

while ContadorDeAcoes < 10:
    tipo_acao = input("Digite o tipo de ação (letra): ")
    
    if not tipo_acao:
        break
    
    try:
        preco_compra = float(input("Digite o preço de compra da ação: R$ "))
        preco_venda = float(input("Digite o preço de venda da ação: R$ "))
        
        lucro_acao = preco_venda - preco_compra
        LucroTotalDaEmpresa += lucro_acao
        
        print(f"Lucro da ação {tipo_acao}: R$ {lucro_acao:.2f}")
        
        if lucro_acao > 1000:
            AcoesLucroMaior1000 += 1
        if lucro_acao < 200:
            AcoesLucroMenor200 += 1
        
        ContadorDeAcoes += 1
    except ValueError:
        print("Entrada inválida. Tente novamente.")

print(f"Número de ações com lucro maior do que R$ 1.000,00: {AcoesLucroMaior1000}")
print(f"Número de ções com lucro menor do que R$ 200,00: {AcoesLucroMenor200}")
print(f"Lucro total da empresa: R$ {LucroTotalDaEmpresa:.2f}")