'''
Hipótesis:
- Las tareas están representadas por números enteros.
- Existen relaciones de predecesor entre las tareas.

Precondición:
- El usuario proporciona un número válido de tareas.
- El usuario ingresa restricciones de predecesores válidas.

Entrada:
- Un número total de tareas.
- Restricciones de predecesores en formato 'tarea_anterior tarea_actual'.

Salida:
- Una lista que representa el orden de las tareas, teniendo en cuenta las restricciones de predecesores.

Efecto:
- El algoritmo proporciona el orden en el que deben completarse las tareas, considerando las restricciones de 
predecesores.

'''

def ordenar_tareas_con_restricciones(numero_tareas, restricciones):
    # Creamos un diccionario para almacenar las tareas y sus predecesores
    predecesores = {}
    
    # Inicializamos el diccionario con listas vacías para cada tarea
    for tarea in range(1, numero_tareas + 1):
        predecesores[tarea] = []
    
    # Llenamos el diccionario con las restricciones de predecesores
    for tarea_anterior, tarea_actual in restricciones:
        if tarea_actual not in predecesores:
            predecesores[tarea_actual] = []
        predecesores[tarea_actual].append(tarea_anterior)
    
    # Función auxiliar para recorrer las tareas en profundidad (DFS)
    def dfs(tarea, visitadas):
        if tarea not in visitadas:
            visitadas.add(tarea)
            for predecesor in predecesores.get(tarea, []):
                dfs(predecesor, visitadas)
            orden.append(tarea)
    
    # Lista para almacenar el orden de las tareas
    orden = []
    
    # Recorremos cada tarea y aplicamos DFS
    visitadas = set()
    for tarea in range(1, numero_tareas + 1):
        dfs(tarea, visitadas)
    
    # Devolvemos el orden inverso, ya que la lista se llena en orden inverso
    return orden[::-1]

# Ejemplo de uso
numero_total_tareas = int(input("Ingrese el número total de tareas: "))

# Entrada de usuario para las restricciones de predecesores
restricciones = []
print("Ingrese las restricciones de predecesores en formato 'tarea_anterior tarea_actual'.")
print("Ingrese '0 0' para terminar.")
while True:
    entrada = input("Restricción: ")
    if entrada == '0 0':
        break
    tarea_anterior, tarea_actual = map(int, entrada.split())
    restricciones.append((tarea_anterior, tarea_actual))

# Calculamos el orden de las tareas con las restricciones dadas
orden_tareas = ordenar_tareas_con_restricciones(numero_total_tareas, restricciones)
print("Orden de las tareas:", orden_tareas)
