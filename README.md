# Mintic_reto_python

En este reto se da solución a varios ejercicios utilizando el lenguaje de programación Python. a continuación se  presenta el enunciado de cada  reto.

reto_3

ONLY MUSIC.

PROMUSIC se ha enterado de su capacidad auditiva, su contexto melómano y sus habilidades en desarrollo de software. Por estas tres características, que son muy difíciles de encontrar, lo han contactado para que genere alguna idea innovadora que permita realizar el lanzamiento de ONLY MUSIC.
La dinámica de ONLY MUSIC consiste en hacer sonar una serie de cuerdas, una cuerda a la vez, y cada cuerda asociada a una letra distinta del alfabeto; lamentablemente, el sonido algunas veces no suena con calidad perfecta, así que el sonido de la cuerda puede llegar representado por la letra del alfabeto en minúscula o en mayúscula. La idea es que luego de escuchar la sucesión de sonidos, se pueda determinar,  cuál cuerda sonó y cuántas veces sonó la misma cuerda de manera consecutiva.

Un ejemplo sencillo de ésta dinámica se puede hacer con la canción “SON PARA UN SONERO”, que inicia con la secuencia: E,E,e,E,E,d,EE,D,c,C. En este caso, los sonidos generados serán E (con cinco repeticiones), D (con una repetición), E (con dos repeticiones), D (con una repetición), y C (con dos repeticiones).
Realizando el análisis completo usted decide construir un programa que resuelve la propuesta realizada.
Inicialmente el programa recibe la sucesión de cuerdas que está escuchando, que puede estar en minúscula o en mayúscula, y cada sonido separado por coma.
La salida estará representada por una sucesión de cuerdas, representadas en mayúscula, sin tener en cuenta los sonidos repetidos, y debajo de cada cuerda, la cantidad de veces que sonó esta de manera consecutiva.
Entrada
La entrada consta de una sucesión de caracteres separados por coma que corresponden a las cuerdas asociadas a los sonidos determinados.
Salida
La salida consta de dos líneas: la primera es la sucesión de sonidos de cuerdas sin repeticiones, en mayúscula y separadas por espacio; la segunda es la cantidad de veces que se repitió cada sonido de cuerda de manera consecutiva, separado también por espacio.
 
 
Entrada	
C,E,a,b,g,c,e,c,B,C,g,b,d,f,B,D,g,e,c,a

Salida
C E A B G C E C B C G B D F B D G E C A
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 11

Entrada	
e,E,c,E,b,d,f,F,c,e,a,c,a,c,e

Salida
E C E B D F C E A C A C E
2 1 1 1 1 2 1 1 1 1 1 1 1

Entrada	
E,E,e,E,E,d,E,E,D,c,C,E,E,B,E,E,a,E,A,E,g,E,G,E,f,E

Salida	
E D E D C E B E A E A E G E G E F E
5 1 2 1 2 2 1 2 1 1 1 1 1 1 1 1 1 1
 
Entrada	Salida
c,c,A,c,G,g,g,b,a,c	

Salida
C A C G B A C
2 1 1 3 1 1 1
 
Entrada	Salida
b,B,b,B,B,f,C,G,B,G,C,g,a,A,D,C

Salida
B F C G B G C G A D C
5 1 1 1 1 1 1 1 2 1 1
 
 
Reto 4

Gi, Ale y Nico están coleccionando las láminas del Mundial 2024 de Pannini Paganini y encontraron una tienda OnLine donde vende algunas láminas, cada lámina es vendida a un cierto precio. Como ellos tienen una lista con los códigos de las láminas que les hacen falta, quieren saber los códigos de las láminas que pueden comprar y el precio a pagar por dicha compra. Realizar un programa que dado un diccionario (en formato JSON) que tiene las parejas código:precio de todas las láminas que tiene la tienda, y que dada la lista de códigos de láminas que les faltan a Gi, Ale y Nico (separados por espacios), imprima el precio de las láminas que pueden comprar y los códigos 
de las láminas que pueden comprar: