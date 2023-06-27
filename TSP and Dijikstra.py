import networkx as nx
import matplotlib.pyplot as plt
import time

def calculate_dijkstra(graph, source, destination):
    start_time = time.time()

    # Inisialisasi variabel
    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    visited = {node: False for node in graph.nodes}

    distances[source] = 0

    while True:
        min_distance = float('inf')
        min_node = None

        for node in graph.nodes:
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            break

        visited[min_node] = True

        for neighbor in graph.neighbors(min_node):
            if not visited[neighbor]:
                new_distance = distances[min_node] + graph[min_node][neighbor]['weight']
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = min_node

    path = []
    current_node = destination

    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous[current_node]

    end_time = time.time()

    print("Hasil Dijkstra:")
    print("Jalur Terpendek:", path)
    print("Jarak Terpendek:", distances[destination])
    print("Waktu komputasi:", end_time - start_time, "detik")

    draw_graph(graph, path)


def draw_graph(graph, path):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='red', width=2)

    plt.show()


graph = nx.Graph()

graph.add_edge('a', 'b', weight=12)
graph.add_edge('a', 'c', weight=10)
graph.add_edge('a', 'g', weight=12)
graph.add_edge('b', 'c', weight=8)
graph.add_edge('b', 'd', weight=12)
graph.add_edge('c', 'g', weight=9)
graph.add_edge('c', 'e', weight=3)
graph.add_edge('c', 'd', weight=11)
graph.add_edge('d', 'e', weight=11)
graph.add_edge('d', 'f', weight=10)
graph.add_edge('e', 'f', weight=6)
graph.add_edge('e', 'g', weight=7)
graph.add_edge('f', 'g', weight=9)

while True:
    print("Pilih algoritma:")
    print("1. TSP (Traveling Salesman Problem)")
    print("2. Dijkstra")
    print("0. Keluar")

    choice = int(input("Masukkan pilihan (0/1/2): "))

    if choice == 0:
        break
    elif choice == 1:
        calculate_tsp(graph)
    elif choice == 2:
        source = input("Masukkan node awal: ")
        destination = input("Masukkan node tujuan: ")
        calculate_dijkstra(graph, source, destination)
    else:
        print("Pilihan tidak valid. Silakan pilih 0, 1, atau 2.")
