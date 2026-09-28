# Proyecto final - Asistente RAG de Inteligencia Artificial

Este proyecto permite consultar seis apuntes del curso. La interfaz está hecha con Streamlit y se comunica con una API de FastAPI. La API usa Google AI para crear embeddings y respuestas, y guarda los vectores en ChromaDB.

## Preparación

Se necesita Python 3.12 y una clave gratuita de [Google AI Studio](https://aistudio.google.com/apikey). No es necesario activar facturación para probar la cuota gratuita.

```powershell
cd proyecto-final
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Abrir `.env` y colocar la clave:

```text
GOOGLE_API_KEY=tu_clave
```

El archivo `.env` está ignorado por Git.

## Ejecución

En una terminal:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

En otra terminal:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run ui\streamlit_app.py
```

También se pueden abrir `iniciar_api.bat` e `iniciar_ui.bat`. La aplicación queda en `http://localhost:8501` y la documentación de la API en `http://localhost:8000/docs`.

## Prueba rápida

1. Entrar a la pestaña **Documentos**.
2. Presionar **Indexar corpus incluido**.
3. Preguntar: `¿Qué diferencia hay entre BFS y DFS?`
4. Probar fuera del tema: `¿Cuál es la receta de la paella?`

La primera pregunta debe responder con citas. La segunda debe indicar que no existe evidencia suficiente.

## Cómo funciona

- Los seis archivos de `data` suman varios miles de palabras.
- Cada documento se divide en chunks de 300 palabras con 60 de solapamiento.
- `gemini-embedding-2` crea los vectores de documentos y preguntas.
- ChromaDB guarda el índice en la carpeta local `chroma`.
- Se recuperan tres chunks de forma predeterminada.
- Si el mejor score es menor que 0.35, el sistema se abstiene.
- `gemini-3.5-flash-lite` redacta en español usando solamente la evidencia.

La carpeta `chroma` se conserva al reiniciar la API, pero no se sube a Git porque se puede reconstruir.

## Estructura

```text
proyecto-final/
├── app/              # API y lógica RAG
├── ui/               # interfaz Streamlit
├── data/             # seis apuntes del curso
├── evidencias/       # capturas de la ejecución
├── REPORTE.md
├── requirements.txt
└── .env.example
```

