#Exemplo: Calculas imposto de produtos utilizando uma função
#Não precisaria repetir o mesmo cálculo toda vez
#Criar uma função calcular_imposto() e usá-la quando precisar



# def saudacao(nome):
    #print(f"OLá! {nome}! Bem-vindo ao curso de Python.")

#saudacao("Maria")

#RETORNO DE VALORES

def somar(a, b):
    return a + b

#Chamando a função e armazenando o resultado
resultado = somar(5, 3)
print(f"A soma é {resultado}")

#FUNÇÃO COM VARIOS PARAMETROS
def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

#CHAMANDO A FUNÇÃO
resultado = calcular_media(8, 9, 7)
print(f"A média é {resultado:.2f}")
