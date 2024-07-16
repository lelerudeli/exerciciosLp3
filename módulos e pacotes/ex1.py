# entrada: comprimento, altura e largura 
# calcular volume em L 
# potência do termostato
# qtd em L de filtragem por hora


# Volume é dado por (comprimento * altura * largura) / 1000
# A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
# A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

print("Aquário!!")

print("para começar, me fale as informações do seu aquário:\n")

comprimento = float(input("comprimento ->"))
altura = float(input("altura ->"))
largura = float(input("largura ->"))


def opcoes():
    print("agora que você já me deu as informações, o que deseja fazer?")
    print("1. Calcular o Volume")
    print("2. Calcular a Potência do Termostato")
    print("3. Calcular a quantidade de filtragem mínima")

    opc = int(input(""))
    match opc:
        case 1:
            vol = volume(comprimento, altura, largura)
            print(f"O volume do seu aquário é de {vol} litros")
        case 2:
            vol = volume(comprimento, altura, largura)
            pot(vol)
        case 3:
            vol = volume(comprimento, altura, largura)
            filtragem(vol)
        case _:
            print("Escolha um número de 1 a 3")

def volume(comprimento, altura, largura):
    vol = (comprimento*altura*largura)/1000
    return vol

def pot(vol):
    if vol <=0:
          print("tem algo de errado com o seu volume, digite 2 para calcular novamente")
          opcoes()
    else:
         temp_desejada = float(input("você que a temperatura chegue a quantos graus? (só o número)\n"))
         temp_ambiente = float(input("e qual é a tempreatura ambiente de agora?\n"))

         pot = vol*0.05*(temp_desejada - temp_ambiente)

         print(f"A potencia do seu termostato é de {pot:.2f}")

def filtragem(vol):
    if vol <=0:
          print("é preciso o valor do volume primeiro, digite a opção para calculá-lo!")
          opcoes()
    else:
         filtragem = vol*3
         print(f"É preciso filtrar o filtro {filtragem:.2f} por hora")

opcoes()   


