import argparse
import graph_config
from graph import Graph


def parse_args():
    parser = argparse.ArgumentParser(
        description="Implementation of Diykstra's algorithm.")
    parser.add_argument(
        "-t", "--type",
        dest="graph_type",
        choices=["dict", "matrix"],
        default="dict",
        help="type of graph description.")
    parser.add_argument(
        "initial_node",
        type=str,
        help="initial node in graph.")
    return parser.parse_args()


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
    labeled_graph = {key: float("inf") for key in graph.get_nodes()}
    current_node = initial_node
    labeled_graph[current_node] = 0
    visited_nodes = list()

    while current_node is not None:
        if graph.get_edges(current_node):
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
    args = parse_args()
    graph = eval("create_graph_from_{}(graph_config.GRAPH_{})".format(
        args.graph_type,
        args.graph_type.upper()))
    print_result(dijkstra(graph, args.initial_node))
