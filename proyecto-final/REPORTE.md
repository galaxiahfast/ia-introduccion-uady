# Reporte corto

## Dominio y corpus

El sistema responde preguntas sobre temas vistos en Introducción a la Inteligencia Artificial. El corpus contiene seis apuntes propios en Markdown: agentes inteligentes, búsqueda de rutas, perceptrón multicapa, visión computacional, clustering K-medias y sistemas RAG. En conjunto tienen más de 3,500 palabras. Los embeddings se calculan con `gemini-embedding-2` y se guardan en una colección persistente de ChromaDB.

## Partición

El texto se divide en fragmentos de 300 palabras con un solapamiento de 60. Elegí ese tamaño porque conserva una explicación casi completa y el solapamiento evita perder información cuando una idea queda entre dos fragmentos.

## Abstención

La distancia de Chroma se convierte en score de similitud. Si el mejor resultado tiene un score menor que 0.35, la API responde que no cuenta con evidencia suficiente. El prompt también le indica al modelo que se abstenga cuando los fragmentos no contesten la pregunta. La prueba fuera del corpus pregunta por una receta de paella.

## Responsabilidad de cada herramienta

Google AI genera los embeddings de los documentos y de la pregunta. ChromaDB conserva esos vectores y recupera los chunks cercanos. Después, Gemini recibe la evidencia numerada y escribe una respuesta corta en español con citas. FastAPI coordina estos pasos y Streamlit muestra el resultado, las fuentes y los scores.

