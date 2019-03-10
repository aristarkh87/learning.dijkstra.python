import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph._graph = {
            "a": {
                "b": 30,
                "c": 10
            },
            "b": {
                "d": 40
            },
            "c": {
                "a": 50
            },
            "d": {
                "c": 20
            }
        }

    def test_add_node(self):
        node = "e"
        self.graph.add_node(node)
        self.assertTrue(node in self.graph._graph)

    def test_set_edge_without_weight(self):
        node = "a"
        neighbour = "b"
        weight = float("inf")
        self.graph.set_edge(node, neighbour)
        self.assertEqual(self.graph._graph[node][neighbour], weight)

    def test_set_edge_with_weight(self):
        node = "a"
        neighbour = "b"
        weight = 100
        self.graph.set_edge(node, neighbour, weight)
        self.assertEqual(self.graph._graph[node][neighbour], weight)

    def test_get_nodes(self):
        result = ["a", "b", "c", "d"]
        self.assertEqual(self.graph.get_nodes(), result)

    def test_get_edges(self):
        result = {"b": 30, "c": 10}
        self.assertEqual(self.graph.get_edges("a"), result)

    def test_get_weight(self):
        self.assertEqual(self.graph.get_weight("a", "b"), 30)

    def test_get_weight_none(self):
        self.assertIsNone(self.graph.get_weight("x", "y"))

    def test_get_dict(self):
        result = self.graph._graph
        self.assertEqual(self.graph.get_dict(), result)

    def test_get_matrix(self):
        result = [
            [0, 30, 10, 0],
            [0, 0, 0, 40],
            [50, 0, 0, 0],
            [0, 0, 20, 0]
        ]
        self.assertEqual(self.graph.get_matrix(), result)


if __name__ == "__main__":
    unittest.main()
