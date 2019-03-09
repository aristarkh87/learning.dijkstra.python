import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_node(self):
        node = "a"
        self.graph.add_node(node)
        result = {node: {}}
        self.assertEqual(self.graph.graph, result)

    def test_set_edge_without_weight(self):
        node = "a"
        neighbour = "b"
        inf = float("inf")
        self.graph.set_edge(node, neighbour)
        result = {node: {neighbour: inf}}
        self.assertEqual(self.graph.graph, result)

    def test_set_edge_with_weight(self):
        node = "a"
        neighbour = "b"
        weight = 10
        self.graph.set_edge(node, neighbour, weight)
        result = {node: {neighbour: weight}}
        self.assertEqual(self.graph.graph, result)

    def test_get_nodes(self):
        self.graph.graph = {"a": {"b": 10}, "c": {}}
        result = ["a", "c"]
        self.assertEqual(self.graph.get_nodes(), result)

    def test_get_edges(self):
        node = "a"
        self.graph.graph = {node: {"b": 10, "c": 20}}
        result = {"b": 10, "c": 20}
        self.assertEqual(self.graph.get_edges(node), result)

    def test_get_weight(self):
        node = "a"
        neighbour = "b"
        weight = 10
        self.graph.graph = {node: {neighbour: weight}}
        self.assertEqual(self.graph.get_weight(node, neighbour), weight)


if __name__ == "__main__":
    unittest.main()
