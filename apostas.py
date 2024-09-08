import random
import time

print("---- APOSTAS ----")

opcao = [
    "1 - Jogo de adivinhar 2 numeros entre 1 e 7. ", #0
    "2 - Roleta de 25 números. ", #1
    "3 - aposte na cor. " #2
]

saldo = 100

def adivinhar_numero():
    global saldo

    while True:
        try:
            valor_aposta = float(input(f"R${saldo:.2f} - Quanto você quer apostar? "))
        except ValueError:
            print("Digite um valor monetário válido, por favor.")
            continue

        if (valor_aposta > saldo):
            print(f"Saldo insuficiente para este valor! Saldo atual: R${saldo:.2f}")
            continue
        else:
            print(f"Valor apostado: R${valor_aposta}. Saldo atual: R${saldo:.2f}")
            saldo -= valor_aposta

        num1 = random.randint(1, 7)
        num2 = random.randint(1, 7)

        try:
            resposta1 = int(input(f"{num1} - Diga sua 1ª resposta: ")) # mostra a resposta para testes
            resposta2 = int(input(f"{num2} - Diga sua 2ª resposta: ")) # mostra a resposta para testes
        except ValueError:
            print("Digite um número válido, por favor.")

        if (resposta1 == num1 and resposta2 == num2):
            resultado = valor_aposta * 2
            saldo += resultado
            print(f"\nParabéns! Você acertou 2 números e ganhou: R${resultado:.2f} Saldo atual: R${saldo:.2f}")

        elif (resposta1 == num1 and resposta2 != num2) or (resposta1 != num1 and resposta2 == num2):
            resultado = valor_aposta * 1.5
            saldo += resultado
            print(f"Você acertou 1 número e ganhou: R${resultado:.2f}!  Saldo atual: R${saldo:.2f}")

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

        if (escolha_numero >= 1 and escolha_numero <= 25):
            while (numeros_gerados < 25):
                numeros_gerados += 1
                resposta = random.randint(1, 25)
                time.sleep(0.3)
                print(f"\033[34m[{resposta}]\033[m")

                if (resposta == escolha_numero):
                    valor_ganho = valor_aposta * 0.7
                    saldo += valor_ganho
                    print(f"\033[32mVocê ganhou {valor_ganho:.2f}R$!\033[m ")

            else:
                saldo -= valor_aposta

        else:
            print("O número deve ser entre 1 e 25.")

        print(f"Saldo atual: {saldo:.2f}")

        escolha = input("Deseja jogar novamente? (s/n:) ")
        if (escolha.lower() != 's'):
            break    

for opcao in opcao:
    print(opcao)

print(f"\n\033[32mSaldo:\033[m {saldo:.2f}")

while True:

    escolha_opcao = str(input("\nSelecione uma das seguintes opções: "))
    if(escolha_opcao == '1'):
        adivinhar_numero()
    elif(escolha_opcao =='2'):
        roleta()
    else:
        print("\033[31mOpção inválida!\033[m")

    print(f"Saldo: \033[32m{saldo}\033[m")
    escolha = input("Deseja escolher outro jogo? (s/n:) ")
    if (escolha.lower() != 's'):
        break
