# Ejercicio 2: descripción PEAS de agentes inteligentes

PEAS permite describir el entorno de tarea de un agente a partir de su medida de
desempeño, el entorno en el que actúa, sus actuadores y sus sensores.

### 1. Asistente virtual de voz

- **Performance:** porcentaje de solicitudes entendidas y resueltas correctamente, tiempo de respuesta, satisfacción del usuario, baja tasa de activaciones falsas y protección de la privacidad.
- **Environment:** vivienda, usuario, otros hablantes, ruido ambiental, dispositivos inteligentes y servicios de internet. Es parcialmente observable, estocástico, secuencial, dinámico y combina datos continuos (audio) con acciones discretas.
- **Actuators:** reproducir voz o audio, mostrar información, enviar mensajes, crear alarmas y recordatorios, iniciar llamadas y controlar dispositivos compatibles.
- **Sensors:** micrófonos, palabra de activación, reconocimiento de voz, historial de conversación, perfil y preferencias, reloj, ubicación autorizada y respuestas de APIs.

La intención no se observa de forma directa y el ruido puede cambiar la interpretación. Además, una orden puede afectar las siguientes, por lo que la interacción es secuencial.

### 2. Robot aspirador doméstico

- **Performance:** porcentaje de superficie limpiada, cantidad de suciedad recogida, tiempo y energía consumidos, cobertura sin repeticiones innecesarias, ausencia de choques o caídas y regreso exitoso a la base.
- **Environment:** pisos, habitaciones, muebles, escaleras, personas, mascotas, cables y suciedad. Es parcialmente observable, estocástico, secuencial, dinámico y principalmente continuo.
- **Actuators:** mover ruedas, girar, activar cepillos y succión, modificar potencia, detenerse, regresar y acoplarse a la base.
- **Sensors:** sensores de distancia o LiDAR, cámara, parachoques, sensores anticaída, detectores de suciedad, encoders de ruedas, IMU, nivel de batería y señal de la base.

El robot solo percibe una parte de la casa en cada instante y los obstáculos pueden moverse. Cada desplazamiento modifica su posición y condiciona la ruta posterior.

### 3. Sistema de recomendación de streaming

- **Performance:** tasa de clic o reproducción, minutos consumidos, finalización de contenido, retención, diversidad, satisfacción y baja frecuencia de recomendaciones rechazadas.
- **Environment:** catálogo, plataforma, usuarios, contexto de uso, disponibilidad regional y tendencias. Es parcialmente observable, estocástico, secuencial, dinámico y discreto en la selección de contenidos.
- **Actuators:** ordenar filas y resultados, recomendar títulos o canciones, crear listas, enviar notificaciones y ajustar la portada o explicación mostrada.
- **Sensors:** historial de reproducciones, búsquedas, clics, pausas, abandonos, valoraciones, hora, dispositivo, idioma, metadatos del catálogo y comportamiento agregado.

El gusto real del usuario está oculto y una misma sugerencia puede recibir respuestas distintas. Las recomendaciones también influyen en el historial futuro.

### 4. Vehículo autónomo en ciudad

- **Performance:** cero colisiones e infracciones, llegada correcta, tiempo de viaje, comodidad, consumo de energía y capacidad de mantener distancias seguras.
- **Environment:** calles, carriles, semáforos, señales, clima, obras, otros vehículos, ciclistas y peatones. Es parcialmente observable, estocástico, secuencial, dinámico, continuo y multiagente.
- **Actuators:** dirección, acelerador, freno, transmisión, luces, direccionales, limpiaparabrisas y claxon.
- **Sensors:** cámaras, radar, LiDAR, ultrasonido, GPS, mapas, IMU, velocímetro, odometría y comunicaciones autorizadas con infraestructura.

No puede conocerse con certeza la intención de otros usuarios de la vía. El entorno cambia mientras el sistema decide y pequeños controles continuos afectan toda la trayectoria.

### 5. Agente de trading algorítmico en bolsa

- **Performance:** rendimiento neto ajustado por riesgo, pérdidas máximas, volatilidad, costos de transacción, deslizamiento, liquidez y cumplimiento de límites regulatorios.
- **Environment:** bolsas, libros de órdenes, intermediarios, participantes, noticias y condiciones macroeconómicas. Es parcialmente observable, estocástico, secuencial, dinámico, continuo y multiagente.
- **Actuators:** enviar, modificar o cancelar órdenes; comprar o vender; seleccionar tipo, precio y volumen; cerrar posiciones y aplicar límites de riesgo.
- **Sensors:** cotizaciones, libro de órdenes, operaciones ejecutadas, volumen, indicadores, noticias estructuradas, posición actual, saldo, comisiones y confirmaciones del bróker.

El agente no conoce las estrategias de los demás y los precios cambian incluso durante su cálculo. Cada operación altera el capital y el riesgo disponible después.

### 6. Sistema de diagnóstico médico asistido por IA

- **Performance:** sensibilidad, especificidad, precisión, calibración, reducción de falsos negativos, tiempo de respuesta, utilidad clínica y seguridad del paciente.
- **Environment:** hospital o clínica, pacientes, expediente electrónico, laboratorio, equipos de imagen y personal de salud. Es parcialmente observable, estocástico, secuencial, dinámico y mixto entre variables discretas y continuas.
- **Actuators:** mostrar diagnósticos diferenciales, marcar regiones sospechosas, calcular niveles de riesgo, recomendar estudios adicionales y emitir alertas para revisión médica.
- **Sensors:** síntomas registrados, antecedentes, signos vitales, resultados de laboratorio, medicamentos, notas clínicas e imágenes como radiografías, tomografías o resonancias.

La enfermedad verdadera no siempre se observa directamente y las pruebas tienen incertidumbre. Es un sistema de apoyo: la decisión clínica final permanece bajo responsabilidad del profesional.

### 7. Dron de inspección de infraestructura

- **Performance:** cobertura de la estructura, detección precisa de grietas, corrosión o fugas, calidad de las imágenes, tiempo, consumo de batería y vuelo sin colisiones.
- **Environment:** puente, tubería o línea eléctrica, obstáculos, viento, lluvia, iluminación, señal GPS y personal cercano. Es parcialmente observable, estocástico, secuencial, dinámico y continuo.
- **Actuators:** variar empuje de motores, ascender, descender, girar, cambiar trayectoria, estabilizarse, orientar la cámara y regresar o aterrizar.
- **Sensors:** cámara RGB, cámara térmica cuando aplica, GPS, IMU, altímetro, LiDAR o ultrasonido, brújula, medidor de batería y sensores de viento.

El dron solo observa las superficies visibles y las ráfagas introducen incertidumbre. Cada maniobra afecta la energía, la posición y las tomas que podrá obtener después.

### 8. Agente jugador de ajedrez

- **Performance:** ganar o empatar, maximizar la evaluación de la posición, evitar jugadas ilegales, administrar el reloj y reducir errores tácticos.
- **Environment:** tablero, piezas, reglas, reloj y oponente. Es totalmente observable, determinista, secuencial, semidinámico, discreto y multiagente competitivo.
- **Actuators:** seleccionar y ejecutar una jugada legal, ofrecer o aceptar tablas y abandonar la partida.
- **Sensors:** posición completa del tablero, turno, movimientos previos, derechos de enroque, posibilidad de captura al paso, reloj propio y del rival, y jugada del oponente.

El tablero es visible por completo y una jugada tiene un resultado definido por las reglas. Se considera semidinámico porque la posición espera, pero el reloj sigue avanzando.

## Conclusión

Aunque todos son agentes, sus entornos cambian mucho. El ajedrez tiene reglas y
estado visibles, mientras que los sistemas físicos y humanos trabajan con datos
incompletos e incertidumbre. Por eso las métricas, acciones y percepciones deben
definirse para cada problema concreto y no de manera genérica.

