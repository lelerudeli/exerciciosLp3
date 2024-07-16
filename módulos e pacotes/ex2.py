#entrada : peso e altura 
# saída: classificação do individuo, IMC -> e quanto ele precisa perder para chegar no peso ideal

print("Calculadora de IMC")

print("para começar, me fale as informações sobre você:")

def chamaFuncoes():
    peso, altura, imc = calculo_imc()
    classificacao(imc)
    calc_pesoIdeal(imc, peso, altura)

def calculo_imc():
    peso = float(input("peso ->"))
    altura = float(input("altura (em metros) ->"))
    if peso and altura > 0:
        imc = peso/(altura*altura)        
    else: 
        "Alguma coisa deu errado! Digite seus dados novamente."
        calculo_imc()
    return peso, altura, imc

def classificacao(imc):
    if imc <= 18.5:
        print(f"Você está abaixo do Peso ideal. Seu imc é de {imc:.2f}")
    elif imc <= 24.9:
        print(f"Você está com o peso normal. Seu imc é de {imc:.2f}")
    elif imc <= 29.9:
        print(f"Você está com excesso de peso. Seu imc é de {imc:.2f}")
    elif imc <= 34.9:
        print(f"Você está com Obesidade de Classe 1. Seu imc é de {imc:.2f}")
    elif imc <= 39.9:
        print(f"Você está com Obesidade de Classe 2. Seu imc é de {imc:.2f}")
    else:
        print(f"Você está com Obesidade de Classe 3. Seu imc é de {imc:.2f}")
         
def calc_pesoIdeal(imc, peso, altura): 
    peso_ideal_min = 18.5 *(altura*altura)
    peso_ideal_max = 24.9 *(altura*altura)
    if imc <= 18.5:
        peso_ganhar = peso_ideal_min - peso
        print(f"Você precisa ganhar {peso_ganhar:.2f} kg para atingir o peso ideal")
    elif imc >= 24.9: 
        peso_perder = peso_ideal_max - peso
        print(f"Você precisa perder {peso_perder:.2f}kg para atingir o peso ideal")
    else:
        print("")

chamaFuncoes()