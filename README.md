# Giro-punto
Giro de un punto realizado en python y pygame


Para la realización de un giro se emplea la matriz de giro. En este caso, se realiza el giro de varios puntos, concretamente una serie de puntos que forman un polígono.

La matriz de giro, en 2 dimensiones se puede expresar como:

![1](https://user-images.githubusercontent.com/68278278/186279823-a313944b-a6cd-42dc-aff2-9c6e493f9a28.png)

Siendo:
  * x' = Coordenada x del punto ya girado
  * y' = Coordenada y del punto ya girado
  * cos(theta) = Función coseno del angulo 'theta' a girar
  * sin(theta) = Función seno del angulo 'theta' a girar
  * x = Coordenada x del punto a girar
  * y = Coordenada y del punto a girar
  
Se exponen ejemplo del poligono a girar y girado. Es un polígono de 7 lados regular, cuya longitud entre vertices es de 100 px
  
El poligono a girar es el siguiente:
  ![imagen](https://user-images.githubusercontent.com/68278278/186280389-7e24235b-d98a-4752-abd1-e27a1c85e5c5.png)
  
Siendo sus vertices:
[[415.23824354812433, 300.0], [371.8498696363685, 390.0968867902419], [274.3570784181862, 412.34898018587336], [196.17393017138318, 350.0], [196.17393017138318, 250.0], [274.35707841818623, 187.65101981412664], [371.8498696363685, 209.9031132097581]]

El poligono ya girado es el siguiente:

![imagen](https://user-images.githubusercontent.com/68278278/186280595-dc0a935b-ef09-4500-9c97-360f27846c5a.png)

Cuyos vertices son:
[[346.0828544915108, 194.37697553103743], [411.3115956193229, 270.17414784558275], [392.72043490303145, 368.4307951689116], [304.30889555257045, 415.1576579962178], [212.65266996557284, 375.1684555642437], [186.77076545532077, 278.57587293533686], [246.152784012671, 198.11609495866998]]

Ambos poligonos, el 'original' y el girado se verían así:
![imagen](https://user-images.githubusercontent.com/68278278/186280794-20ccda50-0bac-42a3-963c-149f0dec4340.png)
![imagen](https://user-images.githubusercontent.com/68278278/186280795-b688e0cc-d026-4316-bf83-0ba7f93d5e78.png)
