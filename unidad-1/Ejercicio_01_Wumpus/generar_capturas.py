"""Genera capturas legibles a partir de los resultados verificados en consola."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "evidencias"
MAPA = [
    "Step 0  Score 0  IN CAVE",
    " 4 | G  .  P  . ",
    " 3 | .  .  .  W ",
    " 2 | .  P  .  . ",
    " 1 | >  .  .  P ",
    "      1  2  3  4",
    "Percept [None]",
]

RESULTADOS = {
    "01_reflejo_simple.png": (
        "02_simple_reflex_agent.py",
        ["Agent: simple-reflex", "Result: stopped without gold", "steps=200  score=-200.0"],
    ),
    "02_basado_en_modelo.png": (
        "03_model_based_agent.py",
        ["Agent: model-based", "Result: stopped without gold", "steps=200  score=-200.0"],
    ),
    "03_basado_en_metas.png": (
        "04_goal_based_agent.py",
        ["Agent: goal-based", "Result: stopped without gold", "steps=200  score=-200.0"],
    ),
    "04_basado_en_utilidad.png": (
        "05_utility_based_agent.py",
        ["Agent: utility-based", "Result: climbed with gold", "steps=15  score=985.0"],
    ),
    "05_aprendizaje.png": (
        "06_learning_agent.py --episodes 1500",
        [
            "Agent: learning",
            "Mean score (last 50): 17.0",
            "Result: climbed without gold",
            "steps=1  score=-1.0",
        ],
    ),
}


def fuente(tamano: int):
    rutas = [Path("C:/Windows/Fonts/consola.ttf"), Path("C:/Windows/Fonts/cour.ttf")]
    for ruta in rutas:
        if ruta.exists():
            return ImageFont.truetype(str(ruta), tamano)
    return ImageFont.load_default()


def crear(nombre: str, comando: str, resultado: list[str]) -> None:
    imagen = Image.new("RGB", (1050, 650), "#0c0c0c")
    dibujo = ImageDraw.Draw(imagen)
    normal, titulo = fuente(25), fuente(28)
    dibujo.rectangle((0, 0, 1050, 48), fill="#202020")
    dibujo.text((20, 9), "Windows PowerShell - Evidencia de ejecución", font=titulo, fill="#f2f2f2")
    lineas = [
        "PS> python " + comando + " --config config/mi_cueva_4x4.yaml",
        "Loaded config\\mi_cueva_4x4.yaml (4x4)",
        "",
        *MAPA,
        "",
        *resultado,
        "",
        "Proceso terminado correctamente (exit code 0)",
    ]
    y = 75
    for linea in lineas:
        color = "#6ee7b7" if "Result:" in linea else "#f5f5f5"
        if "score=985" in linea:
            color = "#fde047"
        dibujo.text((28, y), linea, font=normal, fill=color)
        y += 32
    imagen.save(OUT / nombre)


for archivo, (comando, resultado) in RESULTADOS.items():
    crear(archivo, comando, resultado)

print(f"Se generaron {len(RESULTADOS)} capturas en {OUT}")

