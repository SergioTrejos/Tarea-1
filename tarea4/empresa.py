archivo = open("c:/Users/Sergio/Documents/2k23/Estructuras/Tarea3/datos_empresa.txt", "r")
lineas = archivo.readlines()
archivo.close()

def validar_entrada(entrada):
    listas = entrada.split(",")
    if len(listas) == 5 and isinstance (str,listas[0]) and isinstance (str,listas[1]) and isinstance (str,listas[3]):
        try:
            int(listas[2])
            int(listas[4])
            return True
        except:
            return False
    else:
        return False
    
def leer_archivo(archivo):
    Lista_Empleados = []
    lineas = archivo.split(",")
    for linea in lineas:
        datos = linea.split(",")
        nombre = datos[0]
        correo = datos[1]
        edad = int(datos[2])
        departamento = datos[3]
        salario = float(datos[4])
        empleado = Empleado(nombre,correo,edad,departamento,salario) 
        Lista_Empleados.append(empleado)


class Empleado:
    def __init__(self,nombre,correo,edad,departamento,salario):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.departamento = departamento
        self.salario = salario





for empleado in Lista_Empleados:
    print("Nombre: ", empleado.nombre)
    print("Correo: ", empleado.correo)
    print("Edad: ", empleado.edad)
    print("Departamento: ", empleado.departamento)
    print("Salario: ", empleado.salario)
    print()
