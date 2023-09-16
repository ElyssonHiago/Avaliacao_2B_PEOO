SomaIdades = 0
ContadorIdades = 0


while ContadorIdades < 10:
    try:
        Idade = int(input(f'Digite a {ContadorIdades + 1}ª idade: '))
        SomaIdades += Idade
        ContadorIdades += 1
    except ValueError:
        print("Digite alguma idade válida.")

MediaIdades = SomaIdades / 10

print(f'A média das idades digitadas é: {MediaIdades}')