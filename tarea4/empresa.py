import os
script_dir = os.path.dirname(os.path.abspath(__file__))


archivo = open(script_dir + "\\datos_empresa.txt", "r")
lineas = archivo.readlines()
archivo.close()

class Empleado:
    def __init__(self,nombre,correo,edad,departamento,salario):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.departamento = departamento
        self.salario = salario

def validar_entrada(entrada):
    listas = entrada.split(",")
    if len(listas) == 5 and isinstance (listas[0],str) and isinstance (listas[1],str) and isinstance (listas[3],str):
        try:
            int(listas[2])
            int(listas[4])
            return True
        except:
            return False
    else:
        return False

def leer_archivo(archivo_nombre):
    archivo_temp = open(archivo_nombre, "r")
    lineas_temp = archivo_temp.readlines()
    archivo_temp.close()
    Lista_Empleados_temp = []
    for linea in lineas_temp:
        if validar_entrada(linea):
            datos = linea.split(",")
            nombre = datos[0]
            correo = datos[1]
            edad = int(datos[2])
            departamento = datos[3]
            salario = float(datos[4])
            empleado = Empleado(nombre,correo,edad,departamento,salario) 
            Lista_Empleados_temp.append(empleado)
    return Lista_Empleados_temp

def buscar_dep(empleados, nombre_departamento):
    empleado_dep = []
    for empleado in empleados:
        if empleado.departamento == nombre_departamento:
            empleado_dep.append(empleado)
    return empleado_dep


def buscar_salario(empleados, salario_min, salario_max):
    empleado_salario = []
    for empleado in empleados:
        if empleado.salario >= salario_min and empleado.salario <= salario_max:
            empleado_salario.append(empleado)
    return empleado_salario


Lista_Empleados = leer_archivo(script_dir + "\\datos_empresa.txt")
Lista_Departamento = buscar_dep(Lista_Empleados,"IT")
Lista_Salario = buscar_salario(Lista_Empleados,100,500)

print("Lista de Empleados: ")
for empleado in Lista_Empleados:
    print("Nombre: ", empleado.nombre)
    print("Correo: ", empleado.correo)
    print("Edad: ", empleado.edad)
    print("Departamento: ", empleado.departamento)
    print("Salario: ", empleado.salario)
    print()

print("Lista de Empleados en el departamento IT: ")
for empleado in Lista_Departamento:
    print("Nombre: ", empleado.nombre)
    print("Correo: ", empleado.correo)
    print("Edad: ", empleado.edad)
    print("Departamento: ", empleado.departamento)
    print("Salario: ", empleado.salario)
    print()

print("Lista de Empleados con un Salario entre 100 y 500: ")
for empleado in Lista_Salario:
    print("Nombre: ", empleado.nombre)
    print("Correo: ", empleado.correo)
    print("Edad: ", empleado.edad)
    print("Departamento: ", empleado.departamento)
    print("Salario: ", empleado.salario)
    print()