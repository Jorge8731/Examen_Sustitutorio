"""1. Crear un programa de evaluación de pago de impuestos.

Reglas:

- Crear una clase Persona con dos atributos nombre, edad y ciudad. Los atributos se
introducirán por teclado y habrá otro método para imprimir los datos. Construir
correctamente el constructor de la clase Persona.

- El valor del nombre no podrá ser editado o usado fuera de la clase, para esto usar la
definición de encapsulamiento para esta variable.

- Declarar una segunda clase llamada Empleado que hereda de la clase Persona y
agrega el método sueldo, el cuál pedirá el sueldo del empleado.

- Crear el método impuesto() el cual obtendrá el impuesto que debe pagar empleado
el cuál será el 9% de su sueldo.

- Debe evaluar dentro de esta función también si tiene que pagar impuestos o no
(sueldo superior a 5500 soles).

- En una función manejoDiccionario() crear un diccionario con los key de nombres,
edad, sueldo e impuesto donde el valor de cada key será el que ha obteniendo en
los anteriores métodos.

- En un método generarArchivoEmpleado() crear en un archivo (crearlo sino existe
mediante la misma función) donde escribirá el nombre, sueldo y el impuesto de cada
empleado que se registra.(Separado cada empleado por comas y en una línea
diferente)

- Crear una función para abrir el archivo y mostrar por consola todos los empleados
que se han ido registrando con su nombre, sueldo e impuesto a pagar para luego
imprimir por consola usando la función manejoDiccionario() el diccionario que se ha
creado.

- Crear un función para encontrar a un empleado por su nombre dentro del archivo
que se ha generado con los registro de los empleado, en caso de encontrarlo
imprimir el mensaje: “El empleado Nombre tiene una remuneración de Sueldo y un
impuesto de Impuesto”."""


class Persona:
    def __init__(self):
        self.__nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
        self.ciudad = input("Ingrese la ciudad: ")

    def imprimir_datos(self):
        print("Nombre: {}".format(self.__nombre))
        print("Edad: {}".format(self.edad))
        print("Ciudad: {}".format(self.ciudad))


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def impuesto_pagar(self):
        impuesto = self.sueldo * 0.09
        if self.sueldo > 5500:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no debe pagar impuestos.")
        return impuesto


def manejoDiccionario(empleados):
    diccionario = {}
    for empleado in empleados:
        diccionario[empleado._Persona__nombre] = {
            "edad": empleado.edad,
            "sueldo": empleado.sueldo,
            "impuesto": empleado.impuesto_pagar()
        }
    return diccionario


def generarArchivoEmpleado(empleados):
    try:
        file = open("my_files/empleados.txt", "a+")
        for empleado in empleados:
            file.write(f"{empleado._Persona__nombre},{empleado.sueldo},{empleado.impuesto_pagar()}\n")  # Corregir aquí
    except FileNotFoundError:
        file = open("my_files/empleados.txt", "w")
        for empleado in empleados:
            file.write(f"{empleado._Persona__nombre},{empleado.sueldo},{empleado.impuesto_pagar()}\n")

        file.close()


def mostrarEmpleados():
    try:
        file = open("my_files/empleados.txt", "r")
        for linea in file:
            nombre, sueldo, impuesto = linea.strip().split(",")
            print(f"Nombre: {nombre}, Sueldo: {sueldo}, Impuesto: {impuesto}")
    except FileNotFoundError:
        print("El archivo de empleados no existe.")

        file.close()


def encontrarEmpleado(nombre):
    try:
        file = open("my_files/empleados.txt", "r")
        for linea in file:
            nombre_empleado, sueldo, impuesto = linea.strip().split(",")
            if nombre_empleado == nombre:
                print(f"El empleado {nombre} tiene una remuneración de {sueldo} y un impuesto de {impuesto}")
                return
        print("Empleado no encontrado.")
    except FileNotFoundError:
        print("El archivo de empleados no existe.")

        file.close()


empleados = [Empleado() for _ in range(3)]

generarArchivoEmpleado(empleados)

mostrarEmpleados()

print("\nDiccionario de empleados:")
print(manejoDiccionario(empleados))

encontrarEmpleado("Jorge")
