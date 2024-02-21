"""2. Realizar el juego “Acierta el número” con los siguientes requerimientos:

Reglas:

- Realizar una función donde se obtendrá un número aleatorio del 1 al 50, luego crear otra
función que pedirá un número el cuál será evaluado para saber si es el número
aleatorio.

- El número ingresado debe ser entero, mayor a 0 y menor a 100.

- Usar try except para comprobar que el valor ingresado si pueda ser convertido a entero
(pistas: usar ValueError)

- Crear una función adivina() para validar si el número ingresado es el que se obtuvo en la
primera función.

- La función adivina llamará a las dos primeras funciones respectivamente.

- En la función validar adivina() se solicitará pedir el número hasta que se adivine cuál es
el número (dar pistas al usuario si es mayor o menor el número), mientras tanto no se
terminará el programa. (importante)

- La función adivina al momento que haya detectado que el usuario haya detectado el
número imprimirá aparte de “Has ganado” imprimirá también el día, el mes, la hora y el
minuto que se haya acertado el número.

- Crear un módulo con todos estas funciones la cuál será llamada en un file main.py
solamente a la función adivina().

- Realizar una función decoradora para utilizarlo en la función principal al momento que
detecte si el número fue adivinado correctamente, imprimir un mensaje de un antes y
después de ser adivinado dentro de la función decorador."""


from adivina import adivina_numero

adivina_decorado = adivina_numero.funcionA(adivina_numero.adivina)

adivina_decorado()
