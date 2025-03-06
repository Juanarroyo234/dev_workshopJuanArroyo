class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):  # Recorremos la lista de atrás hacia adelante
            lista_invertida.append(lista[i])
        return lista_invertida

    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)): 
            if lista[i] == elemento:  
                return i  
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        lista_sin_duplicados = []
        for elemento in lista:  
            if elemento not in lista_sin_duplicados: 
                lista_sin_duplicados.append(elemento)
        return lista_sin_duplicados
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        resultado = []
        i, j = 0, 0  # Índices para recorrer las listas

        # Comparar elementos y agregar el menor a la lista resultado
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

    # Agregar los elementos restantes (si los hay)
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:  # Si la lista está vacía, retornar tal cual
            return lista
    
        n = len(lista)
        k = k % n  # Para evitar rotaciones innecesarias si k > n

        for _ in range(k):
            ultimo = lista.pop()  # Sacamos el último elemento
            lista.insert(0, ultimo)  # Lo insertamos al inicio

        return lista
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        n = len(lista) + 1  # Se asume que falta un número en la secuencia completa 1..n
        suma_esperada = n * (n + 1) // 2  # Fórmula de la suma de los primeros n números naturales
        suma_real = sum(lista)  # Suma de los números en la lista dada
        return suma_esperada - suma_real  # El número faltante
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for elemento in conjunto1:  # Recorremos cada elemento del posible subconjunto
         if elemento not in conjunto2:  # Si un elemento no está en el conjunto principal, no es subconjunto
            return False
         return True 
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
    def implementar_pila(self):
        pila = []

        def push(elemento):
            pila.append(elemento)

        def pop():
            return pila.pop() if not is_empty() else None

        def peek():
            return pila[-1] if not is_empty() else None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        
        cola = []

        def enqueue(elemento):
            cola.append(elemento)

        def dequeue():
            return cola.pop(0) if not is_empty() else None

        def peek():
            return cola[0] if not is_empty() else None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }

    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
