# Ejercicio 1 - Mundo de Wumpus

Para este ejercicio cambié la posición del Wumpus y de los pozos del mapa
original. Dejé el mapa de 4x4 y el agente sigue iniciando en `[1,1]` mirando
hacia el este.

Las posiciones que usé fueron:

- Wumpus: `[4,3]`
- Pozos: `[2,2]`, `[4,1]` y `[3,4]`
- Oro: `[1,4]`

## Mapa

```text
4 | ORO |     | POZO |        |
3 |     |     |      | WUMPUS |
2 |     | POZO|      |        |
1 |  A  |     |      | POZO   |
     1     2      3       4
```

El oro se puede alcanzar usando el camino `[1,1]`, `[1,2]`, `[1,3]` y
`[1,4]`. Este mismo camino sirve para regresar, por lo que el mapa es válido.

## Resultados

Después de probar los agentes obtuve lo siguiente:

| Agente | Resultado | Puntaje |
|---|---|---:|
| Reflejo simple | No consiguió el oro | -200 |
| Basado en modelo | No consiguió el oro | -200 |
| Basado en metas | No consiguió el oro | -200 |
| Basado en utilidad | Salió con el oro | 985 |
| Aprendizaje | Salió sin el oro | -1 |

El agente de reflejo simple se quedó girando cuando encontró una brisa porque
solo toma en cuenta lo que percibe en ese momento. El agente de utilidad sí pudo
encontrar el camino seguro, tomar el oro y regresar.

Si un pozo se coloca cerca del inicio, el agente basado en modelo detecta brisa
muy pronto y se vuelve más cuidadoso. Si el pozo se aleja, puede recorrer más
casillas y conocer mejor el mapa antes de encontrar peligro.

## Cómo ejecutar

Desde la carpeta `codigo`:

```powershell
python -m pip install -r requirements.txt
python 02_simple_reflex_agent.py --config config/mi_cueva_4x4.yaml
python 03_model_based_agent.py --config config/mi_cueva_4x4.yaml
python 04_goal_based_agent.py --config config/mi_cueva_4x4.yaml
python 05_utility_based_agent.py --config config/mi_cueva_4x4.yaml
```

Las capturas de las pruebas están en la carpeta `evidencias`.

