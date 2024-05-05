'''
Funcionamiento:
La función esta_explorado es una herramienta simple pero efectiva para manipular segmentos dentro de una lista. 
Comienza verificando si los índices proporcionados son válidos, lo cual es crucial para evitar errores como 
índices fuera de rango. Luego, procede a guardar una copia del primer elemento del segmento y desplazar los 
elementos hacia la izquierda, abriendo espacio para colocar el elemento máximo en la posición final del segmento. 
Finalmente, devuelve un valor booleano que indica si el segmento ha sido explorado correctamente o no.

Lo bueno:
Cabe resaltar cómo la función se preocupa por la integridad de la lista, verificando la validez de los índices antes 
de realizar cualquier manipulación. Además, realiza todas las operaciones directamente en la lista de 
entrada, lo que hace que el código sea más eficiente y fácil de entender.

Lo malo:
Una de las preocupaciones que tengo con esta función es su potencial para causar efectos secundarios no deseados 
debido a su modificación directa de la lista de entrada. En situaciones donde la lista original debe permanecer 
intacta, esto podría ser problemático. Además, aunque el enfoque de desplazar elementos funciona, podría no ser la 
solución más eficiente para listas grandes o segmentos extensos.
'''

def esta_explorado(t, inicio, fin):
    """
    Verifica si un segmento en una tabla t ha sido explorado correctamente,
    siguiendo ciertos pasos específicos.

    Parámetros:
        t (list): La tabla de componentes.
        inicio (int): El índice de inicio del segmento.
        fin (int): El índice de fin del segmento.

    Retorna:
        bool: True si el segmento ha sido explorado correctamente, False de lo contrario.


"""

    # Verificar si los índices son válidos
    if inicio < 0 or fin >= len(t) or inicio > fin:
        return False
    
    # Realizar una copia de seguridad del máximo del segmento
    m = t[inicio]
    
    # Desplazar los elementos una celda hacia la izquierda
    for i in range(inicio, fin):
        t[i] = t[i + 1]
    
    # Colocar el elemento más grande en la posición 'fin'
    t[fin] = m
    
    return True

# Ejemplo de uso
t = [10, 8, 15, 18, 12, 7, 18, 14, 9, 18, 21, 3]
inicio = 5
fin = 9

explorado = esta_explorado(t, inicio, fin)
print("El segmento ha sido explorado correctamente:", explorado)
print("Tabla actualizada:", t)


