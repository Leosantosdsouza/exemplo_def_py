#Definição para fazer o calculo da velocidade media.
def calculovelocidademedia(distancia, tempo):

    valocidade_media = distancia/tempo

    print(" A velocidade média é {} KM/h".format(valocidade_media))


#Lembrando que inputs sempre são foras da definição.
distancia = float(input(" Coloque a distancia percorrida "))
tempo = float(input(" Coloque o tempo de viagem "))



#chama a definição pelos valores definido pelo input.
calculovelocidademedia(distancia,tempo)

#definindo valores para a definição.
calculovelocidademedia(15,2)