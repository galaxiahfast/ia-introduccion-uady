# Ejercicio 1 - Búsqueda no informada

Elegí la ruta de **Oradea a Bucharest**. Usé la misma pareja de ciudades en
todos los algoritmos.

## Diagrama

```text
Oradea --151-- Sibiu --99-- Fagaras --211-- Bucharest
                    
                     --80-- Rimnicu Vilcea --97-- Pitesti --101-- Bucharest
```

## Resultados

| Algoritmo | Camino | Profundidad | Costo | Expandidos | Estado |
|---|---|---:|---:|---:|---|
| BFS | Oradea - Sibiu - Fagaras - Bucharest | 3 | 461 km | 5 | success |
| UCS | Oradea - Sibiu - Rimnicu Vilcea - Pitesti - Bucharest | 4 | 429 km | 10 | success |
| DFS | Oradea - Sibiu - Arad - Timisoara - Lugoj - Mehadia - Drobeta - Craiova - Pitesti - Bucharest | 9 | 1024 km | 9 | success |
| DLS límite 2 | No encontró camino | - | - | 3 | cutoff |
| DLS límite 4 | Oradea - Sibiu - Fagaras - Bucharest | 3 | 461 km | 6 | success |
| IDS | Oradea - Sibiu - Fagaras - Bucharest | 3 | 461 km | 8 | success |

## Comentario

BFS encontró el camino con menos carreteras, pero no el de menos kilómetros.
UCS eligió pasar por Rimnicu Vilcea y Pitesti porque ese recorrido cuesta 429
km, aunque tiene una carretera más. DFS dio un camino mucho más largo porque
avanza por una rama hasta el fondo antes de probar otras opciones.

Con DLS, el límite 2 produjo `cutoff` porque la solución más corta necesita 3
carreteras. Con límite 4 ya encontró una solución. IDS coincidió con BFS en la
profundidad 3.

Las salidas completas de la terminal están en `resultados.txt`.

