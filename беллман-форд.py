def bellman_ford(graph, source):    #graph: Граф, представленный в виде словаря, где ключи - вершины, 
                                    #а значения - словари, содержащие смежные вершины и веса ребер.
                                    #source: Начальная вершина.
    #Шаг 1: Инициализация расстояний
    distances = {vertex: float('inf') for vertex in graph} #Все расстояния устанавливаем в бесконечность
    distances[source] = 0           #Расстояние от начальной вершины до самой себя равно 0

    #Шаг 2: Релаксация ребер |V| - 1 раз (|V| - количество вершин)
    for _ in range(len(graph) - 1): #Проходим по всем ребрам (|V| - 1) раз
        for u in graph:             #Перебираем все вершины
            for v, weight in graph[u].items():      #Перебираем все ребра, выходящие из вершины u
                                                    #Если расстояние до u не бесконечность и расстояние до v можно улучшить
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight    # Обновляем расстояние до v

    #Шаг 3: Проверка на наличие циклов с отрицательным весом
    for u in graph:  #Проверяем еще раз все ребра
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError('Graph contains negative weight cycle')    #Если нашли, то ошибка


    return distances         #Возвращаем словарь расстояний

graph = {
  'A': {'B': 1, 'C': 4,'D': 5},
  'C': { 'F': -7, 'E': 3, 'D': -2},
  'D': { 'E': 4 },
  'F': { 'G': -10 },
  'B': { 'C': 5, 'F': -2 },
  'G': {},
  'E': { 'F': 6, 'G': 0 },
}
source = 'A'

shortest_distances = bellman_ford(graph, source)
print(shortest_distances)

