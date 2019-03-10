import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_graph_dict(self):
        graph_type = "dict"
        result = {
            "a": {"b": 7, "c": 9, "f": 14},
            "b": {"a": 7, "c": 10, "d": 15},
            "c": {"a": 9, "b": 10, "d": 11, "f": 2},
            "d": {"b": 15, "c": 11, "e": 6},
            "e": {"d": 6, "f": 9},
            "f": {"a": 14, "c": 2, "e": 9}
        }
        self.assertEqual(main.get_graph(graph_type).get_dict(), result)

    def test_get_graph_matrix(self):
        graph_type = "matrix"
        result = {
            "0": {"1": 7, "2": 9, "5": 14},
            "1": {"0": 7, "2": 10, "3": 15},
            "2": {"0": 9, "1": 10, "3": 11, "5": 2},
            "3": {"1": 15, "2": 11, "4": 6},
            "4": {"3": 6, "5": 9},
            "5": {"0": 14, "2": 2, "4": 9}
        }
        self.assertEqual(main.get_graph(graph_type).get_dict(), result)

    def test_get_current_node(self):
        labeled_graph = {"a": 3, "b": 1, "c": 2}
        visited_nodes = ["b"]
        result = "c"
        self.assertEqual(main.get_current_node(labeled_graph, visited_nodes), result)

    def test_get_current_node_none(self):
        labeled_graph = {"a": 1, "b": 3, "c": 2}
        visited_nodes = ["a", "b", "c"]
        self.assertIsNone(main.get_current_node(labeled_graph, visited_nodes))

    def test_dijkstra(self):
        graph = main.get_graph("dict")
        initial_node = "a"
        result = {'a': 0, 'b': 7, 'c': 9, 'd': 20, 'e': 20, 'f': 11}
        self.assertEqual(main.dijkstra(graph, initial_node), result)
