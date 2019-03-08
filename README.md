# Dijkstra's algorithm

Dijkstra's algorithm in Python. Example from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm.

## Usage
```bash
python3 dijkstra.py ${initial_node}
```

## Graph
```Python
GRAPH = {
    "node1": {
        "neighbour1": int(weight1),
        "neighbour2": int(weight2),
        ...
        "neighbourN": int(weightN)
    },
    ...
    "nodeN": {
        "neighbour1": int(weight1),
        "neighbour2": int(weight2),
        ...
        "neighbourN": int(weightN)
    }
}
```
