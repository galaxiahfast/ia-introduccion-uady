# Visión computacional y YOLO

La visión computacional busca obtener información a partir de imágenes o video. Entre sus tareas están clasificación, detección de objetos, segmentación y seguimiento. La clasificación asigna una etiqueta a toda la imagen. La detección localiza varios objetos con cajas y clases. La segmentación asigna una categoría a cada píxel, por lo que ofrece una forma más precisa de los objetos.

Una imagen digital puede representarse como una matriz. En escala de grises cada posición contiene una intensidad. En color normalmente se utilizan tres canales. El orden puede ser RGB o BGR según la biblioteca. Las dimensiones de una imagen afectan el costo de procesamiento; por eso los modelos suelen redimensionar la entrada a un tamaño fijo.

La convolución aplica un filtro pequeño sobre distintas regiones de la imagen. El filtro puede aprender bordes, texturas y formas. Las primeras capas de una red convolucional reconocen rasgos simples y las capas posteriores combinan esos rasgos en partes u objetos. Compartir el mismo filtro en toda la imagen reduce el número de parámetros en comparación con una capa completamente conectada.

YOLO significa You Only Look Once. Es una familia de modelos de detección que procesa la imagen y produce predicciones de cajas, clases y confianza. Su principal ventaja es realizar la detección en una sola pasada, lo que permite trabajar con rapidez. Una predicción incluye coordenadas de la caja, clase estimada y un valor de confianza.

El umbral de confianza decide qué detecciones se muestran. Con un umbral muy bajo aparecen más cajas, pero también más falsos positivos. Con un umbral alto se conservan predicciones seguras y se pueden perder objetos difíciles. La supresión no máxima compara cajas que se superponen y elimina duplicados, conservando la de mayor confianza.

La librería Ultralytics ofrece una forma sencilla de usar modelos YOLO ya entrenados. Primero se carga un modelo y luego se ejecuta sobre una ruta, arreglo o imagen. Los modelos entrenados con COCO reconocen clases comunes como persona, silla, taza, automóvil y perro. Esto se llama inferencia con un modelo preentrenado; no es lo mismo que entrenar un detector desde cero.

Para evaluar una evidencia se debe conservar la imagen original y la imagen con resultados. Si se usa una fotografía de una taza, la salida debe mostrar la caja, la etiqueta y la confianza. También conviene registrar qué modelo se usó y el umbral. Una captura del entorno demuestra la ejecución, mientras que el archivo de salida permite revisar la imagen con mejor resolución.

Una detección incorrecta puede deberse a poca luz, objetos pequeños, ángulos poco comunes, oclusión o una clase ausente en el entrenamiento. Cambiar el modelo por uno más grande puede mejorar la precisión a costa de tiempo y memoria. También se puede aumentar el tamaño de entrada o entrenar con imágenes del dominio específico.

La ética y la privacidad son importantes. Las imágenes pueden contener rostros, placas u otra información personal. Antes de compartir un conjunto de datos se debe confirmar que existe permiso. Un sistema de visión también puede tener sesgos si los datos de entrenamiento no representan las condiciones reales de uso.

Una prueba sencilla con una silla y una taza permite comprobar el flujo completo: leer la imagen, ejecutar la inferencia, revisar las detecciones y guardar el resultado. No demuestra que el modelo funcione en todos los ambientes, pero sí permite entender cómo se conecta un modelo preentrenado con un programa de Python.

