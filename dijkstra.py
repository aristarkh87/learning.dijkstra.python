from graph_dict import GRAPH as origin_graph
import sys

try:
    initial_node = sys.argv[1]
except IndexError:
    initial_node = list(origin_graph.keys())[0]


def get_current_node(labeled_graph, passed_nodes):
    current_node = None
    current_node_label = float("inf")
    for node, label in labeled_graph.items():
        if node not in passed_nodes:
            if label < current_node_label:
                current_node = node
                current_node_label = label
    return current_node


def print_result(labeled_graph):
    print("{}\t{}".format("Node", "Path"))
    for node, label in labeled_graph.items():
        print("{}\t{}".format(node, label))


if __name__ == "__main__":
    inf = float("inf")
    labeled_graph = { key: inf for key in origin_graph }
    labeled_graph[initial_node] = 0
    current_node = initial_node
    passed_nodes = list()

    while current_node is not None:
        for neighbour, weight in origin_graph[current_node].items():
            if neighbour not in passed_nodes:
                new_label = weight + labeled_graph[current_node]
                if new_label < labeled_graph[neighbour]:
                    labeled_graph[neighbour] = new_label
        passed_nodes.append(current_node)
        current_node = get_current_node(labeled_graph, passed_nodes)

    print_result(labeled_graph)
