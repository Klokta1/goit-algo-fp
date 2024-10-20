import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Клас для графа
class Graph:
    def __init__(self):
        self.edges = {}  # Словник суміжності для представлення графа

    def add_edge(self, from_node, to_node, weight):
        # Додаємо ребро в обох напрямках (для неорієнтованого графа)
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []

        # Додаємо ребро в обох напрямках з однаковою вагою
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

# Функція алгоритму Дейкстри
def dijkstra(graph, start_node):
    # Ініціалізуємо відстані до всіх вершин як нескінченні, крім початкової
    distances = {node: float('inf') for node in graph.edges}
    distances[start_node] = 0

    # Мін-купа для вибору вершини з мінімальною відстанню
    priority_queue = [(0, start_node)]  # (відстань, вершина)

    # Словник для відстеження найкоротшого шляху
    shortest_path_tree = {start_node: None}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо поточна відстань більше записаної, пропускаємо
        if current_distance > distances[current_node]:
            continue

        # Обходимо всіх сусідів поточної вершини
        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            # Якщо знайшли коротший шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_node

    return distances, shortest_path_tree

# Функція для відображення результатів
def print_result(distances, shortest_path_tree, start_node):
    print(f"Найкоротші відстані від {start_node}:")
    for node, distance in distances.items():
        print(f"Вершина {node}: {distance}")

    print("\nШляхи:")
    for node in distances:
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = shortest_path_tree[current]
        path.reverse()
        print(f"Шлях до {node}: {' -> '.join(path)}")

# Функція для візуалізації графа
def visualize_graph(graph, distances, start_node):
    G = nx.Graph()

    # Додаємо всі ребра в граф
    for node, neighbors in graph.edges.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    # Малюємо граф
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title(f"Граф {start_node}")
    plt.show()

# Приклад використання:
graph = Graph()

# Додавання ребер (вершина1, вершина2, вага)
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_node = 'A'
distances, shortest_path_tree = dijkstra(graph, start_node)

# Виведення результатів
print_result(distances, shortest_path_tree, start_node)

# Візуалізація графа
visualize_graph(graph, distances, start_node)
