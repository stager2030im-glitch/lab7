"""EJERCICIO 02 — Preparar un catálogo

ENUNCIADO
Cada producto tiene nombre, precio y categoria. Los nombres son únicos.
Devuelve un diccionario con:
- disponibles: lista de nombres con precio <= 20, en el orden original.
- precios: diccionario nombre -> precio de todos los productos.
- categorias: set de todas las categorías.
Usa una comprensión para cada estructura. No uses ciclos explícitos.
No modifiques la entrada. Para [] devuelve las tres estructuras vacías.

Con los datos entregados se espera:
{"disponibles": ["cafe", "te"],
 "precios": {"cafe": 10, "torta": 25, "te": 8},
 "categorias": {"bebida", "postre"}}
El orden de los elementos del set puede cambiar.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 02".
"""

def preparar_catalogo(productos):
    return {
        "disponibles": [p["nombre"] for p in productos if p["precio"] <= 20],
        "precios": {p["nombre"]: p["precio"] for p in productos},
        "categorias": {p["categoria"] for p in productos},
    }
    
productos = [
    {"nombre": "cafe", "precio": 10, "categoria": "bebida"},
    {"nombre": "torta", "precio": 25, "categoria": "postre"},
    {"nombre": "te", "precio": 8, "categoria": "bebida"},
]
print(preparar_catalogo(productos))

productos2 = [
    {"nombre": "pan", "precio": 20, "categoria": "panaderia"},
    {"nombre": "jugo", "precio": 21, "categoria": "bebida"},
    {"nombre": "galleta", "precio": 5, "categoria": "panaderia"},
    {"nombre": "helado", "precio": 15, "categoria": "postre"},
]
print(preparar_catalogo(productos2))

print(preparar_catalogo([]))

