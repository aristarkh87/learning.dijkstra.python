# Example from
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

GRAPH_DICT = {
    "a": {"b": 7, "c": 9, "f": 14},
    "b": {"a": 7, "c": 10, "d": 15},
    "c": {"a": 9, "b": 10, "d": 11, "f": 2},
    "d": {"b": 15, "c": 11, "e": 6},
    "e": {"d": 6, "f": 9},
    "f": {"a": 14, "c": 2, "e": 9}
}

GRAPH_MATRIX = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]
