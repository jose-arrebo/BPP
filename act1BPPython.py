#########################
###### Actividad 1 ######
#########################
# Crea una funcion que pida por pantalla un número al usuario y que 
# controle mediante excepciones lo siguiente:
#   a. Solo se podrá introducir numeros enteros
#   b. Si el numero es mayor de 10 lanza una excepción con raise la 
#      cual hayas creado previamente mediante ‘class 
#      Miexcepcion(Exception):’

class Miexcepcion(Exception):
    def __init__(self, param1):
        self.param1 = param1

def mayorDiez():
    try:
        num = int(input("Introduce un número entero:"))
        if num > 10:
            raise Miexcepcion("El número introducido es mayor que 10")
        else:
            return f"El entero {num} es menor que 10"

    except ValueError:
        print("El input introducido no es un entero")
        return "El programa ha experimentado un error"
    except Miexcepcion as e:
        print(e.param1)
        return "El programa ha detectado una excepcion"
    except Exception as e:
        print("Ha ocurrido el siguiente error:", e)
        return "El programa ha experimentado un error"


#########################
###### Actividad 2 ######
#########################
#  Abre un fichero .txt y controla mediante excepciones las diferentes 
# casuisticas para que el programa no termine de forma inesperada. 
# Utiliza el finally para cerrar el fichero.

try:
    nombre = input("Indique el nombre del fichero: ")
    modo = input("Indique el modo en el que quiere abrir\
 el archivo: ")
    modos = ["r", "r+", "w", "w+", "a", "a+",
             "rb", "rb+", "wb", "wb+", "ab", "ab+"]
    assert(modo in modos)
    fichero = open(nombre + ".txt", modo)
        
except AssertionError:
    print("El modo seleccionado no es válido")
except FileNotFoundError:
    print("El fichero que desea manipular no existe")
except Exception as e:
    print("Ha ocurrido el siguiente error:", e)

else:
    fichero.close()

finally:
    print("Fin del programa")