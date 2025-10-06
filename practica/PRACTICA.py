# Ejercicio 1
# Hay diferentes formas de representar los datos, y cada forma
# tiene su propia forma de recorrerlos para procesarlos

# Resuelva los siguientes casos, donde la variable 'notas' contiene
# las notas de los 3 parciales para 3 materias de un mismo estudiante

# Recuerde:
# - Escriba su propio código, la copia se califica con 1.0 (para ambos)
# - Analice primero, planee/diseñe una solución, luego escriba el código
# - Utilice comentarios para explicar las partes importantes
# - No utilice números mágicos, si es el caso utilice constantes
# - Realice sus propias pruebas para verificar que todo funciona
# - Debe entregar antes de medianoche
#####################################################################

# Caso 1: Lista de Listas
from pprint import pprint
notas = [
    ["Calculo", 3.5, 2.5, 1.5],
    ["Quimica", 2.5, 3.0, 5.0],
    ["Deporte", 2.4, 2.0, 2.2],
    ["Logica", 1.5, 4.0, 4.5]
]

# 1.1 Calcula la nota final de cada materia (30%, 30% y 40%)
# y agregue el valor a los datos
def c1_final():
    global notas
    for i in  range(len(notas)):
        nota1=notas[i][1]*0.3
        nota2=notas[i][2]*0.3
        nota3=notas[i][3]*0.4
        nota_final = nota1+nota2+nota3 #sumamos las notas para obtener el promedio final
        notas[i].append(nota_final) #agremos al arreglo la nota  final

# 1.2 Calcule el promedio de las notas del Estudiante
def c1_promedio():
    pass
    global notas
    suma_notas  = 0
    for i in range(len(notas)):
        suma_notas += notas[i][4]
    print("el promedio  de las notas del estudiante es:", suma_notas/len(notas))

    
# Llamar funciones
print("------------------------punto 1------------------")
c1_final()
c1_promedio()

#------------------------------------------------------------------------------------------------

# Caso 2: Diccionario de Listas
#####################################################################

notas = {
    "Calculo": [3.5, 2.5, 1.5],
    "Quimica": [2.5, 3.0, 5.0],
    "Deporte": [2.4, 2.0, 2.2],
    "Logica": [1.5, 4.0, 4.5]
}

# 2.1 Calcula la nota final de cada materia (30%, 30% y 40%),
# y agregue el valor a los datos
def c21_final():
    global notas
    for key,value in  notas.items() :
        nota1= value[0]*0.3
        nota2 =value[1]*0.3
        nota3=value[2]*0.4
        nota_final= nota1+nota2+nota3
        notas[key].append(nota_final)


# 2.2 Calcule el promedio de las notas del Estudiante
def c22_promedio():
    global notas
    suma_notas=0
    for key,value in notas.items():
        suma_notas  += value[3]
    print("el promedio de las  notas del estudiante es:",suma_notas/len(notas))


# Llamar funciones, y mostrar Resultados
print("------------------------punto 2------------------")
c21_final()
c22_promedio()

#---------------------------------------------------------------------------------------------

# Caso 3: Diccionario de Diccionarios
#####################################################################

notas = {
    "Calculo": {"pp": 3.5, "sp": 2.5, "tp": 1.5},
    "Quimica": {"pp": 2.5, "sp": 3.0, "tp": 5.0},
    "Deporte": {"pp": 2.4, "sp": 2.0, "tp": 2.2},
    "Logica":  {"pp": 1.5, "sp": 4.0, "tp": 4.5}
}

# 3.1 Calcula la nota final de cada materia (30%, 30% y 40%)
# y agregue el valor a los datos
def c31_final():
    global notas
    #print(notas["Calculo"]) / con esto llamamos al diccionario de calculo
    #print(notas["Quimica"]["sp"]) / con esto llamados a la nota del segundo parcial de quimica
    for key,value in notas.items():
        nota1=value["pp"]*0.3
        nota2=value["sp"]*0.3
        nota3=value["tp"]*0.4
        nota_final=nota1+nota2+nota3
        notas[key]["nota_final"]= nota_final

# 3.2 Calcule el promedio de las notas del Estudiante
def c32_promedio():
    global notas
    suma_notas = 0
    for key,value in notas.items():
        suma_notas+= value["nota_final"]
    print("el promedio de las notas del estudiante es: ",suma_notas/len(notas))



# Llamar funciones, y mostrar Resultados
print("------------------------punto 3------------------")
c31_final()
c32_promedio()


#---------------------------------------------------------------------------------------------

# Caso 4: lista  de Diccionarios
#####################################################################

notas = [
   {
   "nombre": "Calculo",
   "pp": 3.5,
   "sp": 2.5,
   "tp": 1.5},
   {
   "nombre": "Quimica",
   "pp": 2.5,
   "sp": 3.0,
   "tp": 5.0},
   {
   "nombre": "Deporte",
   "pp": 2.4,
   "sp": 2.0,
   "tp": 2.2},
   {
   "nombre": "Logica",
   "pp": 1.5,
   "sp": 4.0,
   "tp": 4.5}

]


# 4.1 Calcula la nota final de cada materia (30%, 30% y 40%)
# y agregue el valor a los datos

def c41_final():
    global notas
    #print(notas[0]["tp"]) llamamos al tercer parcial del curso Calculo
    for  i in  range(len(notas)):
        nota1=notas[i]["pp"]*0.3
        nota2=notas[i]["sp"]*0.3
        nota3=notas[i]["tp"]*0.4
        nota_final=nota1+nota2+nota3
        notas[i]["nota_final"] = nota_final


# 4.2 Calcule el promedio de las notas del Estudiante

def c42_promedio():
    global notas
    suma_notas =  0
    for i  in range(len(notas)):
        suma_notas+= notas[i]["nota_final"]
    print("el promedio de las notas del estudiante es:",suma_notas/len(notas))

# Llamar funciones, y mostrar Resultados

print("------------------------punto 4------------------")
c41_final()
c42_promedio()