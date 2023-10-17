# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if a < b + c and b < a + c and c < a + b: 
    print("Os comprimentos informados podem formar um triangulo.")
else:
    print("Os comprimentos infomados não podem formar um triangulo.")
    