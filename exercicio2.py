#Simulando um caixa eletrônico

#O usuário tem um Saldo de R$ 500,00 no 
# inicio e pode sacar até zerar a conta

saldo = 500

while saldo > 0:
    saque = float(input("Digite o valor do saque(ou digite 0 para sair): "))
   
    if saque == 0:
        break

    if saque > saldo:
         print("Saldo insuficiente! Saque não efetuado.")
    else:
        saldo = saldo - saque
        print (f"Saque efetuado com sucesso! Saldo atual: R${saldo:.2f}")

print("Operação finalizada!")
