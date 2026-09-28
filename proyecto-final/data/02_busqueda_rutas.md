# Búsqueda de rutas

Un problema de búsqueda se define con un estado inicial, acciones posibles, un modelo de transición, una prueba de meta y, cuando se requiere, un costo de ruta. Los estados representan situaciones relevantes y las acciones generan estados sucesores. La frontera guarda los nodos que todavía pueden explorarse. También se acostumbra mantener un conjunto de estados visitados para evitar ciclos y trabajo repetido.

La búsqueda en anchura o BFS usa una cola FIFO: el primer nodo que entra es el primero que sale. Explora primero todos los nodos de profundidad uno, después los de profundidad dos y así sucesivamente. Es completa en espacios finitos y encuentra una ruta con el menor número de pasos cuando todas las acciones tienen el mismo costo. Su problema principal es la memoria porque conserva muchos nodos de la frontera.

La búsqueda en profundidad o DFS usa una pila LIFO. Avanza por una rama hasta que ya no puede continuar y entonces retrocede. Consume menos memoria que BFS, pero puede perder tiempo en una rama muy larga. No garantiza la ruta más corta y, sin control de visitados o límite de profundidad, puede quedar atrapada en ciclos. Es adecuada cuando la memoria es limitada y las soluciones se encuentran a gran profundidad, siempre que el espacio esté controlado.

La búsqueda de costo uniforme o UCS ordena la frontera por el costo acumulado g(n). Siempre expande la ruta disponible con menor costo total. Si los costos de las acciones son positivos, es completa y óptima. Se diferencia de BFS porque una ruta con pocas aristas puede ser más cara que otra con más pasos. En un mapa de carreteras, UCS considera kilómetros o tiempo en lugar de solamente contar ciudades.

Las búsquedas informadas usan una heurística h(n), que estima el costo desde un nodo hasta la meta. La búsqueda voraz o Greedy elige el nodo con menor h(n). Puede avanzar muy rápido hacia un destino, pero ignora lo que ya costó llegar al nodo. Por eso no garantiza la mejor ruta. Una heurística común para ciudades es la distancia en línea recta al destino.

El algoritmo A estrella combina el costo recorrido y la estimación restante mediante f(n) = g(n) + h(n). Si la heurística es admisible, es decir, nunca sobreestima el costo real, A estrella encuentra una solución óptima. Si además es consistente, el valor estimado respeta la desigualdad triangular y se reduce la necesidad de volver a abrir nodos. Con h(n) igual a cero, A estrella se comporta como costo uniforme.

En el mapa clásico de Rumania, una consulta frecuente consiste en viajar de Arad a Bucarest. Greedy suele dirigirse por las ciudades con menor distancia recta, mientras que A estrella equilibra esa distancia con el costo acumulado. El ejemplo permite observar que una decisión aparentemente cercana al destino no siempre produce la ruta total más barata.

Para representar un mapa se puede usar un grafo. Cada ciudad es un nodo y cada carretera es una arista con peso. La lista de adyacencia guarda para cada ciudad sus vecinas y las distancias. Un nodo de búsqueda también conserva el padre que lo generó; al llegar a la meta se recorren esos padres en sentido inverso para reconstruir la ruta.

La comparación entre algoritmos debe usar más de una medida. Conviene registrar la ruta encontrada, su costo, los nodos expandidos, el tamaño máximo de la frontera y el tiempo. En problemas pequeños todos pueden parecer rápidos, pero el número de nodos muestra diferencias que serían importantes en un espacio grande.

No existe un algoritmo mejor para todos los casos. BFS es sencillo y óptimo para pasos iguales, DFS ahorra memoria, UCS maneja costos diferentes, Greedy puede ser rápido con una buena heurística y A estrella ofrece un equilibrio entre costo real y estimación. La elección depende de la información disponible y de las garantías que necesita el problema.

