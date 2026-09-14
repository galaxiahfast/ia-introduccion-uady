# Ejercicio 2 - Rutas A* en México

Agregué una búsqueda A* al mapa de ciudades de México. Cada ciudad se maneja
por su `id`, porque algunos nombres se repiten. Si un nombre es ambiguo, el
programa pide escribir también el estado, por ejemplo `Puebla, Puebla`.

## Probar en la terminal

```powershell
python find_route.py --from-city Tijuana --to Cancún
python find_route.py --from-city Guadalajara --to Mérida
```

## Probar en el mapa

Abrir `mexico_map.html`, seleccionar un origen y un destino y presionar
**Buscar ruta**. La ruta aparece en color verde y debajo se muestra el costo.

La heurística es la distancia haversine desde cada ciudad hasta el destino.
Esta distancia no puede ser mayor que el recorrido por las aristas, por eso es
admisible. El archivo original del grafo no fue modificado.

En `resultados.txt` están las dos pruebas realizadas.

La ruta larga de Tijuana a Cancún tuvo **125 saltos**, un costo de **4528.20
km** y expandió **949 nodos**. En el programa el estado es el `id` numérico de
cada ciudad. Elegí ese dato porque el nombre y hasta la combinación nombre con
estado pueden repetirse.

