SomaDeSalarios = 0
MaiorIdade = float('-inf')
MenorIdade = float('inf')
MulheresComSalarioDeAte200 = 0
MenorSalario = float('inf')
IdadeMenorSalario = None
SexoMenorSalario = None

ContadorIdades = 0

while ContadorIdades < 10:
    try:
        idade = int(input("Digite a idade: "))
        
        if idade == 0:
            break
        
        if idade > MaiorIdade:
            MaiorIdade = idade
        if idade < MenorIdade:
            MenorIdade = idade
        
        sexo = input("Digite qual o gênero (M/F): ").upper()
        salario = float(input("Digite qual o salário: R$ "))
        
        SomaDeSalarios += salario
        
        if sexo == 'F' and salario <= 200:
            MulheresComSalarioDeAte200 += 1
        
        if salario < MenorSalario:
            MenorSalario = salario
            IdadeMenorSalario = idade
            SexoMenorSalario = sexo
        
        ContadorIdades += 1
    except ValueError:
        print("Entrada inválida! Tente novamente.")

if ContadorIdades > 0:
    media_salarios = SomaDeSalarios / ContadorIdades
else:
    media_salarios = 0

print(f"Média dos salários do grupo: R$ {media_salarios:.2f}")
print(f"Maior idade do grupo: {MaiorIdade} anos")
print(f"Menor idade do grupo: {MenorIdade} anos")
print(f"Quantidade de mulheres com salário até R$ 200,00: {MulheresComSalarioDeAte200}")
print(f"Pessoa com menor salário: Idade = {IdadeMenorSalario} anos, Sexo = {SexoMenorSalario}")