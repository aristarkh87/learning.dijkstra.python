class Graph():
    def __init__(self):
        self._graph = {}

    def add_node(self, node):
        if node not in self._graph:
            self._graph[node] = {}

    def set_edge(self, node, neighbour, weight=float("inf")):
        if not self._graph.get(node):
            self.add_node(node)
        self._graph[node].update({neighbour: weight})

    def get_nodes(self):
        all_nodes = set(self._graph)
        for node, neighbours in self._graph.items():
            all_nodes.add(node)
            for neighbour in neighbours:
                all_nodes.add(neighbour)
        return sorted(list(all_nodes))

    def get_edges(self, node):
        return self._graph.get(node)

    def get_weight(self, node, neighbour):
        if self._graph.get(node):
            return self._graph.get(node).get(neighbour)
        else:
            return None

    def get_dict(self):
        return self._graph

    def get_matrix(self):
        matrix = []
        nodes = self.get_nodes()
        for node in nodes:
            matrix_row = []
            for neighbour in nodes:
                weight = self.get_weight(node, neighbour)
                if weight:
                    matrix_row.append(weight)
                else:
                    matrix_row.append(0)
            matrix.append(matrix_row)
        return matrix
