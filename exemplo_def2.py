def calcularvelocidademedia (distancia,tempo):

    velocidade_media = distancia/tempo
    
#exibi o resultado.
    return velocidade_media

distancia = float(input(" informe a distancia (Em Metros) "))
tempo = float(input(" Informe o tempo (Em Minutos)"))

print(" A velocidade media é {}".format(calcularvelocidademedia(distancia, tempo)))