# Ejercicio 1 - Perceptrón multicapa

Modifiqué las dos notebooks de Iris para comparar la red original `4 x 3 x 3` con una red `4 x 3 x 3 x 3 x 3`.

En los dos casos mantuve 500 épocas, tasa de aprendizaje de 0.03, activación sigmoide y error MSE. En la notebook hecha con NumPy agregué las capas nuevas tanto en el forward como en el backpropagation. En Keras agregué dos capas `Dense` antes de la salida.

## Resultados

| Implementación | Red | Error final | Exactitud |
|---|---|---:|---:|
| NumPy | Original | 0.055616 | 96.67% |
| NumPy | Profunda | 0.330871 | 75.33% |
| Keras | Original | 0.184510 | 66.67% |
| Keras | Profunda | 0.222361 | 33.33% |

Agregar capas no mejoró el resultado. Las redes profundas se estancaron más, especialmente la de Keras. Esto puede pasar porque varias funciones sigmoides seguidas producen gradientes pequeños.

Las curvas de NumPy y Keras tampoco fueron iguales. Aunque usé la misma topología y los mismos parámetros generales, cambia la inicialización de pesos y la forma de actualizarlos.

Las capturas de las cuatro corridas y los dos resúmenes de Keras están en `evidencias_colab`.
