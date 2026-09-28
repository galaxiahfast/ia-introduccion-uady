# Sistemas RAG

RAG significa generación aumentada por recuperación. Su propósito es producir una respuesta basada en documentos seleccionados, en lugar de depender únicamente del conocimiento aprendido por un modelo de lenguaje. El proceso general consiste en preparar documentos, dividirlos, crear embeddings, indexarlos, recuperar los fragmentos relacionados con una pregunta y generar una respuesta con esa evidencia.

La ingestión ocurre antes de responder preguntas. Primero se extrae el texto de archivos PDF, Markdown o texto plano. Después se divide en fragmentos llamados chunks. Un documento completo puede ser demasiado grande y contener muchos temas. Los chunks permiten recuperar solamente la sección relacionada con la consulta.

El tamaño del chunk afecta la calidad. Un fragmento muy pequeño puede perder contexto. Uno demasiado grande puede mezclar información relevante con contenido que no sirve. El solapamiento repite algunas palabras entre fragmentos consecutivos para evitar cortar una explicación justo en el límite. En este proyecto se usan 300 palabras por fragmento y 60 palabras de solapamiento.

Un embedding es un vector numérico que representa el significado aproximado de un texto. Los textos con temas parecidos tienden a quedar cerca en el espacio vectorial. El documento y la pregunta deben procesarse con el mismo modelo o con instrucciones compatibles. Para recuperación, el texto del documento se marca como contenido y la pregunta se marca como consulta.

ChromaDB guarda los vectores, el texto original y metadatos. Los metadatos pueden incluir el nombre del archivo y la posición del chunk. Cuando llega una pregunta, la API calcula su embedding y solicita los vecinos más cercanos. La base devuelve distancias que se pueden transformar en un puntaje de similitud para presentarlo al usuario.

La generación ocurre después de recuperar. El prompt contiene la pregunta, los chunks numerados y una instrucción para responder únicamente con esa evidencia. El modelo debe incluir citas como [1] y [2]. Esas citas corresponden al orden de los fragmentos mostrados en la interfaz, de modo que la respuesta se pueda revisar.

La abstención evita inventar. Si el mejor puntaje no alcanza un umbral mínimo, la API responde que no tiene evidencia suficiente y no llama al modelo para completar con conocimiento externo. Incluso si el puntaje supera el umbral, el prompt permite que el modelo indique que los fragmentos no responden la pregunta. Una pregunta sobre una receta de paella debe producir abstención porque el corpus trata sobre inteligencia artificial.

FastAPI concentra la lógica del sistema. El endpoint `/health` informa si el servicio está activo, si existe clave y cuántos chunks contiene el índice. `/ingest` recibe archivos, extrae texto, divide, pide embeddings y guarda en Chroma. `/query` recibe una pregunta, recupera evidencia y genera la respuesta. La documentación interactiva está disponible en `/docs`.

Streamlit funciona como cliente de la API. Permite indexar el corpus incluido, cargar archivos y escribir preguntas. La interfaz no se conecta directamente a ChromaDB ni a Google AI. Esta separación facilita probar la API y permite que otra interfaz pueda utilizarla en el futuro.

La persistencia significa que el índice continúa en disco cuando la API se cierra. Reiniciar el servidor no obliga a calcular todos los embeddings otra vez. La carpeta local de Chroma no se sube al repositorio porque puede reconstruirse desde el corpus y puede ocupar espacio. Tampoco se sube la clave. El archivo `.env.example` muestra las variables necesarias sin contener secretos.

