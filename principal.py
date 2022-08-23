#---------------------------------------------------------------------------------------------
#Programa para rotar figuras geométricas regulares en el centro de la pantalla
#---------------------------------------------------------------------------------------------

#Importo las librerias necesarias así como el otro archivo llamado 'apoyo'
from wsgiref.util import application_uri
import pygame
import apoyo
import math

#Inicio pygame
pygame.init()
#Pongo una resolución de pantalla
alto = 600
anch = 600
#Dicha resolución es almacenada en un array
resol = [alto,anch]
#Obtengo el centro de la pantalla
centro = [alto/2,anch/2]
#Llamo al display de pantalla con dicha resolución
screen = pygame.display.set_mode(resol)
pygame.display.update()


#Creo una figura de 7 lados y longitud 100 px cada lado
long = 100
num_lados = 7

#Almaceno los vertices
vertices = apoyo.vertices(centro,num_lados,long,screen,1)
#Creo un array vacio donde almacenaré los vertices girados y el angulo a girar en grados
verticesgirados = []
angulo = 15

#Creo un bucle que recorra todos los puntos
for i in range(len(vertices)):
    #Giro cada punto y lo almaceno en un array
    verticesgirados.append(apoyo.giro(angulo,centro,vertices[i-1]))

#Represento el poligono girado
apoyo.representarpoligono(verticesgirados,screen)







    





#Actualizo la pantalla tras dibujar la figura
pygame.display.flip()
#Creo un bucle infinito para observar si se ha pulsado el botón de salida.
running = True
while running:
    #Si se ha pulsado, salgo del bucle infinito
    running = apoyo.parada()
#Cierro la pantalla
pygame.quit()


