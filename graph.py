class Graph():
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def set_edge(self, node, neighbour, weight=float("inf")):
        if not self.graph.get(node):
            self.add_node(node)
        self.graph[node].update({neighbour: weight})

    def get_nodes(self):
        return list(self.graph)

    def get_edges(self, node):
        return self.graph.get(node)

    def get_weight(self, node, neighbour):
        if self.graph.get(node):
            return self.graph.get(node).get(neighbour)
        else:
            return None
