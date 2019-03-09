# Example from
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

GRAPH = {
    "a": {
        "b": 7,
        "c": 9,
        "f": 14
    },
    "b": {
        "a": 7,
        "c": 10,
        "d": 15
    },
    "c": {
        "a": 9,
        "b": 10,
        "d": 11,
        "f": 2
    },
    "d": {
        "b": 15,
        "c": 11,
        "e": 6
    },
    "e": {
        "d": 6,
        "f": 9
    },
    "f": {
        "a": 14,
        "c": 2,
        "e": 9
    }
}
