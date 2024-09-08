import random

print("--------------------------- APOSTAS ---------------------------")

opcao = [
    "1 - Jogo de adivinhar 2 numeros entre 1 e 7. ", #0
    "2 - Roleta de 25 números. ", #1
]

saldo = 100

def opcoes_de_aposta():
    global opcao
    for opcoes in opcao:
        print(opcoes)

    print(f"\n\033[32mSaldo:\033[m {saldo:.2f}")

opcoes_de_aposta()

def adivinhar_numero():
    global saldo

    while True: 
        valor_aposta = float(input(f"R${saldo:.2f} - Quanto você quer apostar? ")) 

        if (valor_aposta > saldo):
            print(f"Saldo insuficiente para este valor! Saldo atual: R${saldo:.2f}")
            valor_aposta = float(input(f"R${saldo:.2f} - Quanto você quer apostar? ")) 
        else:
            print(f"Valor apostado: R${valor_aposta}. Saldo atual: R${saldo:.2f}")
        
        saldo -= valor_aposta

        num1 = random.randint(1, 7)
        num2 = random.randint(1, 7)

        resposta1 = float(input(f"{num1} - Diga sua 1° resposta: ")) # mostra a resposta para testes
        resposta2 = float(input(f"{num2} - Diga sua 2° resposta: ")) # mostra a resposta para testes

        if (resposta1 == num1 and resposta2 == num2):
            resultado = valor_aposta * 2
            saldo += resultado
            print(f"\nParabéns! Você acetrou 2 números e ganhou: R${resultado:.2f} Saldo atual: R${saldo:.2f}")

        elif (resposta1 == num1 and resposta2 != num2):
            resultado = valor_aposta * 1.5
            saldo += resultado
            print(f"Você acetrou 1 número e ganhou: R${resultado:.2f}! Saldo atual: R${saldo:.2f}")

        elif (resposta1 != num1 and resposta2 == num2):
            resultado = valor_aposta * 1.5
            saldo += resultado
            print(f"Você acetrou 1 número e ganhou: R${resultado:.2f}!  Saldo atual: R${saldo:.2f}")

        else:
            print(f"Você não acertou nenhum número! Saldo atual: R${saldo:.2f}")
            break

        escolha = input("Deseja jogar novamente? (s/n:) ")
        if (escolha.lower() != 's'):
            break

def roleta():
    global saldo

    while True:
        valor_aposta = float(input(f"R${saldo:.2f} - Digite o valor que quer apostar: "))
        escolha_numero = float(input(f"Escolha um número entre 1 e 25: "))
        numeros_gerados = 0

        if (escolha_numero > 1 and escolha_numero < 25):
            while (numeros_gerados < 25):
                numeros_gerados += 1
                resposta = random.randint(1, 25)
                print(f"\033[34m[{resposta}]\033[m")

                if (resposta == escolha_numero):
                    valor_ganho = valor_aposta * 0.2
                    saldo += valor_ganho + valor_aposta
                    print(f"Você ganhou {valor_ganho}R$! ")

            else:
                saldo -= valor_aposta

        else:
            print("O número deve ser entre 1 e 25.")

        print(f"Saldo atual: {saldo:.2f}")

        escolha = input("Deseja jogar novamente? (s/n:) ")
        if (escolha.lower() != 's'):
            break    

while True:

    escolha_opcao = str(input("\nSelecione uma das seguintes opções: "))
    if(escolha_opcao == '1'):
        adivinhar_numero()
    elif(escolha_opcao =='2'):
        roleta()
    else:
        print("\033[31mOpção inválida!\033[m")

    escolha = input("Deseja escolher outro jogo? (s/n:) ")
    print(" ")
    if (escolha.lower() != 's'):
        break
    else:
        opcoes_de_aposta()
