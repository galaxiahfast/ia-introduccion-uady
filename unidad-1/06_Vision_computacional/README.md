# Ejercicio 1 - YOLO

Ejecuté la notebook en Google Colab. Primero dejé las pruebas originales con `zidane.jpg` y `bus.jpg`. Después subí una foto propia de una taza con el nombre `mi_foto.jpg` y usé ese mismo archivo en las dos formas de predicción.

No cambié `yolov8n.pt`, el conjunto `coco128.yaml` ni las 3 épocas de entrenamiento.

## Resultados

- En la foto de Zidane detectó 2 personas y 1 corbata.
- En la foto del autobús detectó 4 personas, 1 autobús y 1 señal de alto.
- En mi foto detectó la taza como `cup` con 0.97 de confianza. También marcó `tv` con 0.28 y `dining table` con 0.27.

La taza fue reconocida correctamente. La impresora que aparece al fondo no fue etiquetada porque `printer` no es una clase del conjunto COCO. Las etiquetas secundarias tuvieron una confianza baja, por lo que pueden cambiar entre la ejecución por consola y `model(...)`.

## Archivos

- `13_YOLO_ultralytics.ipynb`: copia de la notebook usada en Colab.
- `mi_foto.jpg`: imagen propia utilizada para las dos predicciones.
- `evidencias/01_bus_original.jpg`: detección sobre la imagen original del autobús.
- `evidencias/02_taza_yolo.jpg`: detección sobre mi imagen.
- `evidencias/03_ejecucion_colab.png`: captura de la ejecución en Colab.
