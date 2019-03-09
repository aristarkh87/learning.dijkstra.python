class Graph(dict):
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
        all_nodes = set(self.graph)
        for node, neighbours in self.graph.items():
            all_nodes.add(node)
            for neighbour in neighbours:
                all_nodes.add(neighbour)
        return sorted(list(all_nodes))

    def get_edges(self, node):
        return self.graph.get(node)

    def get_weight(self, node, neighbour):
        if self.graph.get(node):
            return self.graph.get(node).get(neighbour)
        else:
            return None
