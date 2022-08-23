#Importo las librerias necesarias
from array import array
from inspect import _void
import math
from re import A
import pygame

#Creo un función llamada parada
def parada():
    #Comprueba si se ha obtenido un evento
    for event in pygame.event.get():
        #Si ese evento es la pulsación del botón de escape entra
        if event.type == pygame.QUIT:
            #Esto hace que deje el bucle infinito
            return False
    #De no ser introducido, sigue el bucle
    return True

#Función para obtener la posición de los vertices de un polígono regular
def vertices(origen: tuple or array,num_lados: int,long: float,screen: pygame.surface,representar: bool = 0) -> array:
    #Convierto el lado en apotema
    long = Ladoaapotema(long,num_lados)
    puntos = []
    for i in range(num_lados):
        #Obtengo el angulo en el que se encuentra el primer punto
        ang = math.radians((360/num_lados)*i)
        #Obtengo el angulo en el que se encuentra el segundo punto
        angsig = math.radians((360/num_lados)*(i+1)) 
        #Con trigonometría paso de un angulo y una distancia, a un punto llamado A
        puntoA = [long*math.cos(ang)+(origen[0]),long*math.sin(ang)+(origen[1])]
        #Dibujo la línea entre ambos puntos
        puntos.append(puntoA)
    if(representar):
        representarpoligono(puntos,screen)
    return puntos

#Función para girar un punto, un angulo concreto desde otro punto.
def giro(angulo: float,origen: tuple ,punto: tuple) -> array:
    #Paso el punto de origen y que se va a girar a una lista
    origen = list(origen)
    punto = list(punto)
    Ppunto = punto
    #Para realizar un giro, es necesario que se indique el angulo a girar, el origen y el punto a girar.
    #Creo un array vacio donde almacenaré los puntos girados
    giro = []
    #Transformo los angulos de hexadecimal a radianes
    angulo = math.radians(angulo)
    #Realizo una translación para poder girar los puntos
    Ppunto[0] = punto[0] - origen[0]
    Ppunto[1] = punto[1] - origen[1]
    #Empleo la matriz de giro 
    cos = math.cos(angulo)
    sen = math.sin(angulo)
    #Construyo la matríz de giro
    matrizG = [[cos, sen],[-1*sen,cos]]
    #Obtengo los puntos ya girados y los vuelvo a trasladar a donde estaban
    giro.append((Ppunto[0]*matrizG[0][0]+Ppunto[1]*matrizG[0][1])+origen[0])
    giro.append((Ppunto[0]*matrizG[1][0]+Ppunto[1]*matrizG[1][1])+origen[1])
    #Devuelvo los puntos ya girados
    return giro


#Función para conocer la distancia entre 2 puntos
def distancia(origen: tuple ,final: tuple) -> float:
    #Paso el punto de origen y que se va a girar a una lista
    origen = list(origen)
    final = list(final)
    #Obtengo la distancia, es pitágoras
    return math.sqrt(math.pow(origen[0]-final[0],2)+math.pow(origen[1]-final[1],2))


#Función para obtener un vector desde 2 puntos
def creavector(inicio: tuple,final: tuple) -> tuple:
    #Devuelvo una tupla, en la que se encuentra el vector
    return (final[0]-inicio[0],final[1]-inicio[1])


#Función para obtener el modulo de un vector
def modulovector(vector: tuple) -> float:
    #Devuelve el módulo del vector
    return math.sqrt((math.pow(vector[0],2)+math.pow(vector[1],2)))

#Función para representar el vector
def representarvector(puntoap: tuple ,vector: tuple) -> tuple:
    #Un vector puede ser representado conociendo dicho vector y su punto de aplicación
    #Mejora, que se dibuje directamente y añadiendo el sentido
    return [puntoap[0]+vector[0],puntoap[1]+vector[1]]

#Función producto escalar
def productoEscalar(vector1: tuple ,vector2: tuple) -> tuple:
    #Teniendo 2 vectores, devuelve el producto escalar de ambos
    return (vector1[0]*vector2[0]+vector1[1]*vector2[1])

#Función para obtener el angulo entre 2 vectores
def anguloVectores(vector1: tuple,vector2: tuple) -> float:
    #Realiza el módulo de los vectores
    modv1 = modulovector(vector1)
    modv2 = modulovector(vector2)
    #Realiza el producto escalar de los vectores
    podES = productoEscalar(vector1,vector2)
    #Devuelve el angulo que forman ambos vectores en grados sexagesimales
    return math.degrees(math.acos((podES/(modv1*modv2))))


#Función para dibujar los ejes en la pantalla
def ejes(thick: int = 2) -> _void:
    #Posible mejora. Dibujar flechas que indiquen el sentido positivo en ambos ejes así como el nombre
    #Obtengo la resolución de la pantalla
    resol = pygame.display.get_window_size()
    #Llamo a la pantalla 
    screen = pygame.display.set_mode(resol)
    #Dibuja el eje X
    pygame.draw.line(screen,colores[1],(0,resol[0]/2),(resol[0],resol[0]/2),thick)
    #Dibuja el eje Y
    pygame.draw.line(screen,colores[1],(resol[1]/2,0),(resol[1]/2,resol[1]),thick)
    #Actualiza la pantalla
    #pygame.display.flip()
    
#Función para pasar del apotema al lado
def Apotemaalado(apotema: float,numlados: int) -> float:
    #Obtenemos el angulo, en radianes, que se obtiene de dividir 360 entre el num de lados
    angulo = math.radians(360/numlados)
    #Obtenemos el cuadrado del apotema
    ap2 = apotema * apotema
    #Obtenemos el cuadradao del lado
    lado2 = 2*ap2 - 2*ap2*math.cos(angulo)
    #Realizamos la raiz cuadrada para obtener el lado 
    lado = math.sqrt(lado2)
    #Devolvemos el lado
    return lado

#Función para pasar del lado al apotema
def Ladoaapotema(lado: float, numlados: int) -> float:
    #Obtenemos el angulo, en radianes, que se obtiene de dividir 360 entre el num de lados
    angulo = math.radians(360/numlados)
    #Obtenemos el cuadrado del lado
    lado2 = lado*lado
    #Obtenemos el apotema
    apotema = math.sqrt(lado2/(2-(2*math.cos(angulo))))
    #Devolvemos el apotema
    return apotema

#Función para representar un poligono
def representarpoligono(vertices: array,screen: pygame.surface) -> _void:
    #Realizo un bucle, en el que dibujo una línea de punto a punto
    for i in range(len(vertices)):
        pygame.draw.line(screen,colores[1],vertices[i-1],vertices[i])


#Función para pintar el centro con un punto
def centro(screen: pygame.surface,width: int = 1) -> _void:
    #Obtengo la resolución de la pantalla
    resol = pygame.display.get_window_size()
    #Creo un vector centro
    centro = []
    #Obtengo el centro en X y en Y
    centro.append(resol[0]/2)
    centro.append(resol[1]/2)
    #Dibujo el punto en la pantalla
    pygame.draw.line(screen,colores[1],centro,centro,width)





#Defino los colores a emplear
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

#Son guardados en un array para ser usados más facilmente en el programa principal
colores = [BLACK,WHITE]
