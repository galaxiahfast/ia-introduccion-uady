# Ejercicio 1 - Greedy y A*

Para comparar los dos algoritmos elegí la ruta de **Oradea a Bucharest**. Como
el destino es Bucharest se usó la tabla de distancia en línea recta de AIMA.

## Diagrama

```text
Oradea h=380
   |
 151
   |
Sibiu h=253 ----99---- Fagaras h=176 ----211---- Bucharest h=0
   |
  80
   |
Rimnicu Vilcea h=193 --97-- Pitesti h=100 --101-- Bucharest
```

## Resultados

| Algoritmo | Camino | Profundidad | Costo | Expandidos |
|---|---|---:|---:|---:|
| Greedy | Oradea - Sibiu - Fagaras - Bucharest | 3 | 461 km | 3 |
| A* | Oradea - Sibiu - Rimnicu Vilcea - Pitesti - Bucharest | 4 | 429 km | 5 |

Greedy escogió Fagaras porque su valor `h=176` era menor que el de Rimnicu
Vilcea, que era `h=193`. El problema es que Greedy solo mira qué ciudad parece
estar más cerca y no toma en cuenta lo que ya costó el recorrido.

A* usa `f=g+h`, por eso encontró el camino de menor costo, que fue de 429 km.
En su camino los valores de `f` fueron 380, 404, 424, 428 y 429. No disminuyen,
lo cual concuerda con una heurística consistente.

Las salidas completas están en `resultados.txt`.

