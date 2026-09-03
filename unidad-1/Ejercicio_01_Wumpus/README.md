# Ejercicio 1: cambio de ubicación del Wumpus y los pits

## Propuesta

Diseñé una cueva 4x4 diferente al mapa clásico. El agente conserva su salida en
`[1, 1]` y comienza mirando al este. Coloqué el Wumpus en `[4, 3]`, los pozos en
`[2, 2]`, `[4, 1]` y `[3, 4]`, y el oro en `[1, 4]`.

El mapa usado está en `codigo/config/mi_cueva_4x4.yaml`. El resto de `codigo/`
contiene el simulador y los agentes necesarios para repetir las pruebas.

## Diagrama de la cueva

Las filas se leen de arriba hacia abajo, pero las coordenadas usan `(x, y)` y
empiezan en la esquina inferior izquierda.

```text
          x=1   x=2   x=3   x=4
y=4       ORO    .    PIT    .
y=3        .     .     .   WUMPUS
y=2        .    PIT    .     .
y=1      AGENTE  .     .    PIT
```

Existe un camino seguro de ida y vuelta: `[1,1] -> [1,2] -> [1,3] -> [1,4]`.
Ningún objeto se solapa y todas las coordenadas están dentro de la cuadrícula.

## Cómo lo resolví

Primero moví todos los peligros respecto al mapa clásico y después comprobé a
mano que el oro tuviera una ruta segura. Dejé un pozo en `[2,2]` para producir
brisa cerca del recorrido y obligar a los agentes a decidir si siguen explorando
o se vuelven conservadores. El Wumpus quedó lejos de la salida para no bloquear
el único camino seguro.

Después cargué el YAML con el visor y ejecuté los cinco agentes. Los resultados
que obtuve con Python 3.12 y la semilla predeterminada fueron:

| Agente | Resultado | Pasos | Puntaje |
|---|---|---:|---:|
| Reflejo simple | Se detuvo sin oro | 200 | -200 |
| Basado en modelo | Se detuvo sin oro | 200 | -200 |
| Basado en metas | Se detuvo sin oro | 200 | -200 |
| Basado en utilidad | Salió con el oro | 15 | 985 |
| Aprendizaje (1500 episodios) | Salió sin oro en la demostración | 1 | -1 |

El agente basado en utilidad fue el único que completó la tarea en esta prueba.
Recorrió la primera fila para reunir información, regresó a la salida, subió por
la primera columna, tomó el oro y volvió a `[1,1]`. Su puntaje fue positivo, lo
que también demuestra que el mapa sí permite recuperar el oro.

## Análisis solicitado

El agente de reflejo simple falla porque solo responde a la percepción actual.
Al avanzar a `[2,1]` percibe brisa por el pozo de `[2,2]`; como no conserva un
modelo de lo ya visitado, gira repetidamente hasta alcanzar el límite de pasos.

Los agentes basado en modelo y basado en metas no mueren, pero se vuelven muy
conservadores ante la brisa. En esta distribución no consiguen deducir y
planificar el recorrido completo hacia el oro, por lo que terminan girando. El
agente de utilidad sí compara el costo y el riesgo de sus alternativas y elige
la ruta segura por la primera columna.

Si el pozo de `[2,2]` se acercara todavía más a la salida, por ejemplo a `[2,1]`
o `[1,2]`, habría brisa desde el inicio y el agente basado en modelo tendría
menos casillas confirmadas como seguras; incluso podría quedarse sin una acción
de avance aceptable. Si se aleja el pozo de la salida, el agente puede explorar
más casillas sin brisa, ampliar su conjunto de posiciones seguras y tomar mejores
decisiones antes de encontrarse con una zona peligrosa.

## Ejecución

En PowerShell:

```powershell
cd codigo
python -m pip install -r requirements.txt
python 01_wumpus_world.py --config config/mi_cueva_4x4.yaml
python 02_simple_reflex_agent.py --config config/mi_cueva_4x4.yaml
python 03_model_based_agent.py --config config/mi_cueva_4x4.yaml
python 04_goal_based_agent.py --config config/mi_cueva_4x4.yaml
python 05_utility_based_agent.py --config config/mi_cueva_4x4.yaml
python 06_learning_agent.py --episodes 1500 --config config/mi_cueva_4x4.yaml
```

Las capturas y un resumen textual de las ejecuciones están en `evidencias/`.

