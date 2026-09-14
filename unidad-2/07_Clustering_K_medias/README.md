# Ejercicio 1 - Clustering K-medias

En esta prueba comparé los blobs originales de la notebook con cinco centros nuevos más separados. Mantuve 2000 puntos, `random_state=7` y el mismo procedimiento de K-means para valores de `k` entre 1 y 9.

## Centros utilizados

```python
centros_nuevos = np.array([
    [0.3, 2.5],
    [-1.5, 2.3],
    [-3.3, 0.8],
    [-3.5, 2.8],
    [-2.4, 4.3]
])
std_nuevos = np.array([0.3, 0.3, 0.25, 0.25, 0.25])
```

## Resultados

| Datos | Inercia k=3 | Inercia k=5 | Inercia k=8 | Mejor silueta |
|---|---:|---:|---:|---:|
| Originales | 653.217 | 224.074 | 127.131 | k=4, 0.6885 |
| Modificados | 1715.686 | 286.118 | 224.745 | k=5, 0.7366 |

En los datos originales, los tres grupos de la izquierda están casi pegados y K-means puede tratarlos como un solo grupo. Por eso el codo se aprecia en `k=4`, aunque se usaron cinco centros.

Con los centros nuevos se distinguen cinco nubes. La mejor silueta cambió a `k=5` y el codo también se observa alrededor de 5. Si siguiera apareciendo en 4, tendría que separar más los centros o reducir las desviaciones.

La notebook fue ejecutada completa en Google Colab y conserva las salidas originales y modificadas. Las ocho figuras están en `evidencias` y las capturas del entorno están en `evidencias_colab`.
