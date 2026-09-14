import argparse
import heapq
import json
import math
from pathlib import Path


def haversine(a, b):
    """Distancia en línea recta entre dos ciudades."""
    radio = 6371.0
    lat1, lat2 = math.radians(a["lat"]), math.radians(b["lat"])
    dlat = math.radians(b["lat"] - a["lat"])
    dlon = math.radians(b["lon"] - a["lon"])
    x = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * radio * math.asin(math.sqrt(x))


def buscar_ciudad(texto, ciudades):
    """Acepta Nombre o Nombre, Estado y avisa si hay nombres repetidos."""
    partes = [p.strip() for p in texto.split(",", 1)]
    opciones = [c for c in ciudades if c["name"].casefold() == partes[0].casefold()]
    if len(partes) == 2:
        opciones = [c for c in opciones if c["state"].casefold() == partes[1].casefold()]

    if not opciones:
        raise ValueError(f"No se encontró la ciudad: {texto}")
    if len(opciones) > 1:
        nombres = "; ".join(f'{c["name"]}, {c["state"]}' for c in opciones)
        raise ValueError(f"El nombre es ambiguo. Usa uno de estos: {nombres}")
    return opciones[0]["id"]


def a_estrella(inicio, meta, ciudades, vecinos):
    frontera = [(haversine(ciudades[inicio], ciudades[meta]), 0, inicio)]
    costo = {inicio: 0.0}
    anterior = {inicio: None}
    visitados = set()
    expandidos = 0

    while frontera:
        _, _, actual = heapq.heappop(frontera)
        if actual in visitados:
            continue
        if actual == meta:
            break
        visitados.add(actual)
        expandidos += 1

        for siguiente, km in vecinos[actual]:
            nuevo_costo = costo[actual] + km
            if siguiente not in costo or nuevo_costo < costo[siguiente]:
                costo[siguiente] = nuevo_costo
                anterior[siguiente] = actual
                f = nuevo_costo + haversine(ciudades[siguiente], ciudades[meta])
                heapq.heappush(frontera, (f, siguiente, siguiente))

    camino = []
    actual = meta
    while actual is not None:
        camino.append(actual)
        actual = anterior[actual]
    camino.reverse()
    return camino, costo[meta], expandidos


def main():
    parser = argparse.ArgumentParser(description="Ruta A* entre ciudades de México")
    parser.add_argument("--from-city", required=True)
    parser.add_argument("--to", required=True)
    args = parser.parse_args()

    archivo = Path(__file__).with_name("mexico_cities_graph.json")
    datos = json.loads(archivo.read_text(encoding="utf-8"))
    ciudades = datos["nodes"]
    vecinos = [[] for _ in ciudades]
    for arista in datos["edges"]:
        a, b, km = arista["source"], arista["target"], arista["km"]
        vecinos[a].append((b, km))
        vecinos[b].append((a, km))

    try:
        inicio = buscar_ciudad(args.from_city, ciudades)
        meta = buscar_ciudad(args.to, ciudades)
    except ValueError as error:
        parser.error(str(error))

    camino, costo, expandidos = a_estrella(inicio, meta, ciudades, vecinos)
    nombres = [ciudades[i]["name"] for i in camino]
    print("Status: success")
    print("Path:", " -> ".join(nombres))
    print("Depth:", len(camino) - 1, "hops")
    print("Cost:", f"{costo:.2f} km")
    print("Expanded:", expandidos, "nodes")
    print("Heuristic: haversine distance to destination")


if __name__ == "__main__":
    main()

