from graph import GRAPH as origin_graph
import sys

try:
    initial_node = sys.argv[1]
except IndexError:
    initial_node = "1"

def get_inf(graph):
    inf = 0
    for edges in graph.values():
        for weight in edges.values():
            inf += weight
    return inf + 1

def get_current_node(labeled_graph, passed_nodes, inf):
    current_node = None
    current_node_label = inf
    for node, label in labeled_graph.items():
        if node not in passed_nodes:
            if label < current_node_label:
                current_node = node
                current_node_label = label
    return current_node

if __name__ == "__main__":
    inf = get_inf(origin_graph)
    labeled_graph = { key: inf for key in origin_graph }
    labeled_graph[initial_node] = 0
    passed_nodes = list()
    current_node = initial_node

    while current_node is not None:
        for neighbour, weight in origin_graph[current_node].items():
            if neighbour not in passed_nodes:
                new_weight = weight + labeled_graph[current_node]
                if new_weight < labeled_graph[neighbour]:
                    labeled_graph[neighbour] = new_weight
        passed_nodes.append(current_node)
        current_node = get_current_node(labeled_graph, passed_nodes, inf)

    print(labeled_graph)
