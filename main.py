import sys
from graph import Graph
from graph_dict import GRAPH as graph_dict
from graph_matrix import GRAPH as graph_matrix


def create_graph_from_dict(graph_dict):
    graph = Graph()
    for node, edges in graph_dict.items():
        for neighbour, weight in edges.items():
            graph.set_edge(node, neighbour, weight)
    return graph


def create_graph_from_matrix(graph_matrix):
    graph = Graph()
    for node, edges in enumerate(graph_matrix):
        for neighbour, weight in enumerate(edges):
            if weight > 0:
                graph.set_edge(str(node), str(neighbour), weight)
    return graph


def get_graph(graph_type):
    if graph_type == "dict":
        graph = create_graph_from_dict(graph_dict)
    elif graph_type == "matrix":
        graph = create_graph_from_matrix(graph_matrix)
    return graph


def get_initial_node():
    try:
        initial_node = sys.argv[2]
    except IndexError:
        initial_node = graph.get_nodes()[0]
    return initial_node


def get_current_node(labeled_graph, visited_nodes):
    current_node = None
    current_node_label = float("inf")
    for node, label in labeled_graph.items():
        if node not in visited_nodes:
            if label < current_node_label:
                current_node = node
                current_node_label = label
    return current_node


def dijkstra(graph, initial_node):
    labeled_graph = { key: float("inf") for key in graph.get_nodes() }
    current_node = initial_node
    labeled_graph[current_node] = 0
    visited_nodes = list()

    while current_node is not None:
        for neighbour, weight in graph.get_edges(current_node).items():
            if neighbour not in visited_nodes:
                new_label = weight + labeled_graph[current_node]
                if new_label < labeled_graph[neighbour]:
                    labeled_graph[neighbour] = new_label
        visited_nodes.append(current_node)
        current_node = get_current_node(labeled_graph, visited_nodes)
    return labeled_graph


def print_result(graph_paths):
    print("{}\t{}".format("Node", "Path"))
    for node, label in graph_paths.items():
        print("{}\t{}".format(node, label))


if __name__ == "__main__":
    graph = get_graph(sys.argv[1])
    initial_node = get_initial_node()
    print_result(dijkstra(graph, initial_node))
