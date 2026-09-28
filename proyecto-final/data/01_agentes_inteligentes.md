# Agentes inteligentes

Un agente inteligente es un sistema que percibe un ambiente y realiza acciones sobre ese ambiente. La parte que recibe información puede estar formada por sensores, entradas de un programa, archivos o mensajes. La parte que actúa puede mover un robot, mostrar una respuesta, guardar un dato o elegir una acción. La idea importante es que el agente no trabaja aislado: siempre existe un ambiente que cambia y sobre el cual debe decidir.

La descripción PEAS sirve para definir una tarea antes de programar. Las letras significan medida de rendimiento, entorno, actuadores y sensores. La medida de rendimiento indica cuándo el comportamiento es bueno. En el mundo de Wumpus puede considerar salir con el oro, evitar pozos y gastar pocas acciones. El entorno contiene las casillas, paredes, peligros y objetos. Los actuadores permiten avanzar, girar, tomar el oro o disparar. Los sensores entregan percepciones como hedor, brisa, brillo, golpe o grito. Definir PEAS evita construir un programa sin saber qué debe observar y qué resultado debe optimizar.

Un agente de reflejo simple elige una acción mediante reglas condición-acción. Por ejemplo, si percibe brillo entonces toma el oro. Este tipo es fácil de programar y funciona cuando la percepción actual contiene todo lo necesario. Su limitación aparece cuando una decisión depende de algo visto antes. Si el agente salió de una casilla peligrosa y luego regresa, una regla sin memoria no puede recordar el riesgo.

El agente basado en modelo mantiene un estado interno. Ese estado resume aspectos del mundo que no están presentes en la percepción actual. En Wumpus puede registrar casillas visitadas, lugares seguros y posibles posiciones de pozos. El modelo también describe cómo cambian las cosas cuando se ejecuta una acción. Gracias a esta memoria, dos percepciones iguales pueden producir acciones distintas según la historia del recorrido.

El agente basado en metas agrega una descripción del objetivo. No se limita a reaccionar, sino que compara secuencias de acciones que podrían acercarlo a la meta. Para llegar a una casilla segura puede usar una búsqueda de rutas. Una meta responde qué estado se quiere alcanzar, pero no siempre distingue entre varias soluciones que cumplen el objetivo.

El agente basado en utilidad asigna un valor a los resultados posibles. Esto permite preferir una ruta corta sobre otra larga o escoger una opción con menor riesgo. La utilidad es especialmente útil cuando hay incertidumbre o metas que compiten. En Wumpus, salir con el oro tiene utilidad alta, caer en un pozo tiene utilidad muy baja y usar una flecha puede tener un costo pequeño.

Un agente con aprendizaje modifica su comportamiento a partir de la experiencia. Suele describirse con un elemento de desempeño, un elemento de aprendizaje, un crítico y un generador de problemas. El crítico compara el resultado con una medida de rendimiento. El aprendizaje usa esa retroalimentación para cambiar reglas, valores o modelos. El generador de problemas propone exploraciones que pueden aportar información nueva.

La racionalidad no significa conocer el futuro ni acertar siempre. Un agente racional selecciona la acción que espera que produzca el mejor resultado usando sus percepciones, conocimiento y recursos disponibles. Si el ambiente es parcialmente observable, una acción razonable puede terminar mal porque faltaba información. La evaluación debe considerar lo que el agente sabía al decidir, no solamente el resultado final.

Los ambientes pueden clasificarse como observables o parcialmente observables, deterministas o estocásticos, episódicos o secuenciales, estáticos o dinámicos, discretos o continuos, y de uno o varios agentes. El mundo de Wumpus es parcialmente observable, secuencial y discreto. Estas propiedades ayudan a elegir la arquitectura. Un entorno simple y observable puede resolverse con reglas, mientras que uno cambiante y con incertidumbre necesita estado, planificación o aprendizaje.

