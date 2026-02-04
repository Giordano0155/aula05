print("Escolha uma das opções abaixo:\n1-Escolha um número e diga se é par ou ímpar\n2-Escolha dois valores e diga quem é maior entre eles ou se são iguais\n3-Escolha um valor e calcule o dobro")
#num = int(input("Digite a opção desejada: "))
continuar = "s"

while continuar == "s":
    num = int(input("Digite a opção desejada: "))
    match num:
        case 1:
            numero = int(input("Escolha o número desejado: "))
            if numero % 2 == 0:
                print("O número é par.")

            else:
                print("O número é ímpar.")

        case 2:
            numero1 = int(input("Escolha o primeiro número: : "))
            numero2 = int(input("Escolha o segundo número: : "))
            if numero1 > numero2:
                print(f"{numero1} é maior que {numero2}")

            elif numero2 > numero1:
                print(f"{numero2} é maior que {numero1}")

            else:
                print("Os números são iguais.")

        case 3:
            numero = float(input("Digite um valor: "))
            valor = numero * 2
            print(f"O valor escolhido foi {numero} e o dobro é {valor}")

        case _:
            print("Opção inválida. Tente novamente.")

    continuar = input("Deseja continuar? (s/n) ").strip().lower()
    if continuar != "s":
        print("Encerrando o programa.")
    
        break

