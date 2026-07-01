#Jogo de adivinhação

#No jogo o usuário precisa adinhar o númeor secreto
#Ele pode tentar várias vezes até acertar

numero_secreto = 25
tentativa = 0

while tentativa !=numero_secreto:
    tentativa = int(input("Digite um número de 1 a 30: "))

    if tentativa > numero_secreto:
        print("O número secreto é menor")
    elif tentativa < numero_secreto:
        print("O número secreto é maior")
    else:
        print("Parabéns! Você acertou o número secreto!")   
  
        
   