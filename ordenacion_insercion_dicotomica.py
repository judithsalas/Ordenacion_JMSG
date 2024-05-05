'''
Pseudocódigo:

Hipótesis:
- Los elementos de la tabla son comparables.

Precondición:
- La tabla no está vacía.

Entrada:
- Una tabla de elementos comparables.

Salida:
- No hay una salida explícita. La tabla se modifica para que sus elementos estén ordenados en orden creciente.

Efecto:
- La tabla de entrada se modifica de manera que sus elementos estén ordenados en orden creciente.

Postcondición:
- Después de la ejecución del algoritmo, los elementos de la tabla están ordenados en orden creciente.
'''
def ordenacion_insercion_dicotomica(t):
    # Recorremos la lista desde el segundo elemento hasta el último
    for i in range(1, len(t)):
        clave = t[i]  # Elemento actual que se insertará en su posición correcta
        inicio = 0    # Índice de inicio de la búsqueda en la sublista ordenada
        fin = i - 1   # Índice de fin de la búsqueda en la sublista ordenada
        
        # Búsqueda binaria para encontrar la posición de inserción de la clave
        while inicio <= fin:
            # Calculamos el índice medio de la sublista
            mitad = (inicio + fin) // 2
            # Si la clave es mayor que el elemento en el índice medio, ajustamos los límites
            if t[mitad] < clave:
                inicio = mitad + 1
            # Si la clave es menor o igual que el elemento en el índice medio, ajustamos los límites
            else:
                fin = mitad - 1
        
        # Desplazamos los elementos para hacer espacio para la inserción
        for j in range(i, inicio, -1):
            t[j] = t[j - 1]
        
        # Insertamos la clave en su posición correcta
        t[inicio] = clave

# Ejemplo de uso
lista_ejemplo = [10, 5, 8, 3, 6, 1]
ordenacion_insercion_dicotomica(lista_ejemplo)
print("Lista ordenada por inserción dicotómica:", lista_ejemplo)

