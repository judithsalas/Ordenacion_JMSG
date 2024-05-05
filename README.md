# Ejercicios de ordenación

## Algoritmo de Ordenacón por Inserción Dicotómica

Este código implementa el algoritmo de ordenación por inserción dicotómica. Este algoritmo ordena una lista de elementos en orden creciente directamente en la misma lista, sin necesidad de utilizar memoria adicional. Funciona dividiendo la lista en una parte ordenada y otra desordenada, y en cada iteración inserta el próximo elemento en la parte ordenada utilizando búsqueda binaria para encontrar su posición correcta.

El resumen del proceso es:

Se recorre la lista desde el segundo elemento hasta el último.
Para cada elemento, se busca su posición de inserción en la parte ordenada utilizando búsqueda binaria.
Se desplazan los elementos mayores que el elemento actual una posición a la derecha para hacer espacio.
Se inserta el elemento en su posición correcta en la parte ordenada de la lista.
Finalmente, se muestra un ejemplo de uso del algoritmo con una lista de ejemplo, demostrando cómo se ordena la lista utilizando la función ordenacion_insercion_dicotomica.

## Algoritmo de Ordenación Toplógica
Este código implementa un algoritmo para ordenar tareas teniendo en cuenta restricciones de predecesores. El algoritmo utiliza una búsqueda en profundidad (DFS) para explorar las dependencias entre las tareas y determinar el orden correcto en el que deben realizarse.

El resumen del proceso es:

Se crea un diccionario para almacenar las tareas y sus predecesores.
Se inicializa el diccionario con listas vacías para cada tarea.
Se llenan las listas de predecesores con las restricciones de predecesores proporcionadas.
Se define una función auxiliar de búsqueda en profundidad (DFS) para explorar las dependencias entre las tareas.
Se crea una lista para almacenar el orden de las tareas.
Se recorren todas las tareas y se aplica la búsqueda en profundidad para determinar el orden de ejecución correcto.
Se devuelve el orden de las tareas, que se presenta en orden inverso ya que la lista se llena en orden inverso durante la búsqueda en profundidad.
El ejemplo de uso permite al usuario ingresar el número total de tareas y las restricciones de predecesores entre las tareas. Luego, el algoritmo calcula y muestra el orden en el que deben realizarse las tareas teniendo en cuenta las restricciones de predecesores proporcionadas.

## Completar las especificaciones

La función esta_explorado es una herramienta simple pero efectiva para manipular segmentos dentro de una lista. 
Comienza verificando si los índices proporcionados son válidos, lo cual es crucial para evitar errores como 
índices fuera de rango. Luego, procede a guardar una copia del primer elemento del segmento y desplazar los 
elementos hacia la izquierda, abriendo espacio para colocar el elemento máximo en la posición final del segmento. 
Finalmente, devuelve un valor booleano que indica si el segmento ha sido explorado correctamente o no.






