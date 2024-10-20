import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, color_map):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [color_map[node[0]] for node in tree.nodes(data=True)]
    labels = nx.get_node_attributes(tree, 'label')

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Генеруємо градієнт кольорів від темного до світлого
def generate_color_gradient(n):
    base_color = "#1296F0"  # Темний базовий колір
    cmap = plt.get_cmap('Blues')  # Використовуємо вбудовану колірну карту Blues
    gradient = [mcolors.to_hex(cmap(i / n)) for i in range(n)]
    return gradient[::-1]  # Інвертуємо порядок кольорів

# Обхід у глибину (DFS) з використанням стека
def dfs(tree_root):
    stack = [tree_root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited

# Обхід у ширину (BFS) з використанням черги
def bfs(tree_root):
    queue = [tree_root]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited

# Функція для візуалізації обходу
def visualize_traversal(tree_root, traversal_type='DFS'):
    if traversal_type == 'DFS':
        visited = dfs(tree_root)
    else:
        visited = bfs(tree_root)

    color_map = {}
    colors = generate_color_gradient(len(visited))

    # Присвоюємо кольори вузлам відповідно до їхнього порядку відвідування
    for idx, node in enumerate(visited):
        color_map[node.id] = colors[idx]

    # Візуалізуємо дерево з відображенням кольорів
    draw_tree(tree_root, color_map)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходу в глибину
print("DFS (обхід у глибину):")
visualize_traversal(root, traversal_type='DFS')

# Візуалізація обходу в ширину
print("BFS (обхід у ширину):")
visualize_traversal(root, traversal_type='BFS')
