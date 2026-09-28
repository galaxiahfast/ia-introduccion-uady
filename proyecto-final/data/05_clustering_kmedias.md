# Clustering con K-medias

El clustering agrupa ejemplos sin usar etiquetas de clase. Es una tarea no supervisada porque el algoritmo recibe características, pero no recibe la respuesta correcta para cada fila. El objetivo es descubrir una estructura posible en los datos. Los grupos encontrados no siempre coinciden con categorías reales; dependen de las variables, la escala y la medida de distancia.

K-medias representa cada grupo mediante un centroide. Primero elige k centroides iniciales. Después asigna cada punto al centroide más cercano y actualiza cada centroide con la media de los puntos asignados. Estos dos pasos se repiten hasta que los centros dejan de cambiar de forma importante o se alcanza el máximo de iteraciones.

La inicialización aleatoria puede producir resultados diferentes. Una mala selección inicial puede llevar a una solución local con grupos poco naturales. El método k-means++ separa mejor los centroides iniciales y normalmente mejora la estabilidad. El parámetro `n_init` ejecuta el algoritmo varias veces y conserva la solución con menor inercia. Fijar `random_state` ayuda a reproducir un experimento.

La inercia es la suma de las distancias cuadradas entre cada punto y su centroide. Siempre disminuye o se mantiene cuando aumenta k, porque más centros permiten ajustar mejor los datos. Esto significa que no se debe escoger k solamente buscando la inercia más pequeña. El método del codo grafica la inercia para varios valores de k y busca el punto donde agregar grupos produce una mejora cada vez menor.

El coeficiente de silueta compara qué tan cerca está un punto de su propio grupo frente al grupo vecino más próximo. Un valor cercano a uno indica buena separación, un valor cercano a cero indica una frontera dudosa y un valor negativo puede indicar una asignación incorrecta. El promedio permite comparar valores de k, mientras que el diagrama de silueta muestra cómo se distribuyen los puntos dentro de cada grupo.

K-medias funciona mejor con grupos compactos y aproximadamente redondos. Puede fallar cuando los grupos tienen tamaños muy distintos, formas curvas o densidades diferentes. También es sensible a valores atípicos porque la media puede desplazarse. En esos casos pueden probarse algoritmos como DBSCAN, clustering jerárquico o mezclas gaussianas.

La escala de las variables es importante. Si una característica varía entre cero y mil y otra entre cero y uno, la primera dominará la distancia euclidiana. Estandarizar transforma las variables para que tengan escalas comparables. Esta decisión debe tomarse según el significado de los datos; no es solamente un paso automático.

En un conjunto generado con `make_blobs`, los centros y desviaciones permiten controlar la separación. Si varios centros están muy cerca, el método del codo puede sugerir menos grupos que los usados para crear los datos. Al separar los centros y reducir las desviaciones, los grupos se distinguen mejor y la mejor silueta puede coincidir con el número esperado.

Una gráfica de regiones de decisión colorea cada zona según el centroide más cercano. Las fronteras forman un diagrama de Voronoi. Esta visualización permite entender por qué un punto es asignado a un grupo y cómo cambia la partición cuando se mueve un centroide.

En el conjunto Iris se pueden graficar la longitud y el ancho del pétalo. Las especies conocidas sirven solo para comparar visualmente, no para entrenar K-medias. El resultado puede separar bien una especie y mezclar otras dos. Eso no significa necesariamente que el algoritmo esté mal; puede indicar que las dos variables no ofrecen una separación clara o que los grupos reales no tienen la forma que K-medias supone.

