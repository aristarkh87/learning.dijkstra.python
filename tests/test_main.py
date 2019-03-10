import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.graph_dict = {
            "a": {"b": 30, "c": 10},
            "b": {"d": 40},
            "c": {"a": 50},
            "d": {"c": 20}
        }
        self.graph_matrix = [
            [0, 30, 10, 0],
            [0, 0, 0, 40],
            [50, 0, 0, 0],
            [0, 0, 20, 0]
        ]
        self.labeled_graph = {"a": 3, "b": 1, "c": 2}

    def test_create_graph_from_dict(self):
        result = self.graph_dict
        self.assertEqual(
            main.create_graph_from_dict(self.graph_dict).get_dict(),
            result)

    def test_create_graph_from_matrix(self):
        result = {
            "0": {"1": 30, "2": 10},
            "1": {"3": 40},
            "2": {"0": 50},
            "3": {"2": 20}
        }
        self.assertEqual(
            main.create_graph_from_matrix(self.graph_matrix).get_dict(),
            result)

    def test_get_current_node(self):
        visited_nodes = ["b"]
        result = "c"
        self.assertEqual(
            main.get_current_node(self.labeled_graph, visited_nodes),
            result)

    def test_get_current_node_none(self):
        visited_nodes = ["a", "b", "c"]
        self.assertIsNone(
            main.get_current_node(self.labeled_graph, visited_nodes))

    def test_dijkstra(self):
        graph = main.create_graph_from_dict(self.graph_dict)
        initial_node = "a"
        result = {"a": 0, "b": 30, "c": 10, "d": 70}
        self.assertEqual(
            main.dijkstra(graph, initial_node),
            result)
