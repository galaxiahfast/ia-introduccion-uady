# Perceptrón multicapa

Una neurona artificial recibe valores de entrada, multiplica cada uno por un peso, suma un sesgo y aplica una función de activación. Los pesos indican la importancia de cada entrada. El sesgo permite desplazar la frontera de decisión. Sin una activación no lineal, varias capas densas se comportarían como una sola transformación lineal y la red perdería capacidad para aprender patrones complejos.

El perceptrón multicapa está formado por una capa de entrada, una o más capas ocultas y una capa de salida. En el conjunto Iris se usan cuatro características: longitud y ancho del sépalo, y longitud y ancho del pétalo. La salida puede contener tres neuronas, una para cada especie. Una arquitectura sencilla es 4-3-3: cuatro entradas, tres neuronas ocultas y tres salidas.

La propagación hacia adelante calcula la salida de la red. Cada capa recibe la salida de la capa anterior. Durante el entrenamiento se compara la predicción con el valor esperado mediante una función de pérdida. Para clasificación multiclase suele usarse entropía cruzada con softmax, aunque en ejercicios didácticos también puede aparecer error cuadrático medio con activación sigmoide.

La retropropagación calcula cómo contribuyó cada peso al error. Empieza en la salida y aplica la regla de la cadena hacia las capas anteriores. El gradiente obtenido señala la dirección en la que crece la pérdida. Un optimizador como descenso de gradiente estocástico actualiza los pesos en la dirección contraria. La tasa de aprendizaje controla el tamaño de cada ajuste.

Una época significa recorrer todos los ejemplos de entrenamiento una vez. Entrenar más épocas no siempre mejora el modelo. Al principio la pérdida normalmente disminuye, pero un entrenamiento excesivo puede memorizar los datos. Para vigilarlo se separan datos de entrenamiento y validación. Si la pérdida de entrenamiento baja mientras la de validación sube, existe una señal de sobreajuste.

Antes de entrenar conviene escalar las características. Las variables de Iris usan unidades parecidas, pero aun así la normalización puede facilitar la optimización. También se debe convertir la clase a una representación adecuada. Con `sparse_categorical_crossentropy` se conservan etiquetas enteras; con `categorical_crossentropy` se utiliza codificación one-hot.

Agregar capas aumenta la profundidad, pero no garantiza una exactitud mayor. Una red 4-3-3-3-3-3 tiene más transformaciones que una 4-3-3. Puede aprender relaciones adicionales, aunque también puede sufrir gradientes pequeños, entrenamiento lento o sobreajuste. Por eso una comparación debe conservar la tasa de aprendizaje, el número de épocas y los mismos datos. De esa forma el cambio principal es la arquitectura.

La curva de pérdida ayuda a interpretar el entrenamiento. Una disminución suave indica que el optimizador está aprendiendo. Una curva que oscila puede señalar una tasa demasiado alta. Una curva casi plana puede indicar una tasa muy baja, una activación saturada o un problema en los datos. La exactitud complementa la pérdida, pero no explica por sí sola la confianza de las predicciones.

Keras permite declarar una red con `Sequential` y capas `Dense`. `model.summary()` muestra la forma de salida y el número de parámetros. Una capa densa con cuatro entradas y tres neuronas tiene quince parámetros: doce pesos y tres sesgos. Si la siguiente capa recibe tres valores y tiene tres neuronas, agrega doce parámetros.

Para obtener resultados repetibles se fija una semilla aleatoria. Aun así, pequeñas diferencias de hardware o librerías pueden cambiar los decimales. Lo importante es documentar la arquitectura, los datos, la pérdida, el optimizador y las épocas. Una evidencia útil incluye el resumen del modelo, la curva de entrenamiento y una medida final calculada sobre datos que no se usaron para ajustar los pesos.

