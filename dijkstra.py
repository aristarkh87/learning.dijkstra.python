from graph import Graph
from graph_dict import GRAPH as graph_dict
import sys


def create_graph(graph_dict):
    graph = Graph()
    for node, edges in graph_dict.items():
        for neighbour, weight in edges.items():
            graph.set_edge(node, neighbour, weight)
    return graph


def get_current_node(labeled_graph, visited_nodes):
    current_node = None
    current_node_label = float("inf")
    for node, label in labeled_graph.items():
        if node not in visited_nodes:
            if label < current_node_label:
                current_node = node
                current_node_label = label
    return current_node


def print_result(labeled_graph):
    print("{}\t{}".format("Node", "Path"))
    for node, label in labeled_graph.items():
        print("{}\t{}".format(node, label))


if __name__ == "__main__":
    graph = create_graph(graph_dict)

    try:
        initial_node = sys.argv[1]
    except IndexError:
        initial_node = graph.get_nodes()[0]

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

    print_result(labeled_graph)
