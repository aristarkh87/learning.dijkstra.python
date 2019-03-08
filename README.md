# Dijkstra's algorithm

Dijkstra's algorithm in Python. Example from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm.

## Usage
```bash
python3 dijkstra.py dict ${initial_node_name}
```
or
```bash
python3 dijkstra.py matrix ${initial_node_index}
```

## Graph dict
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

## Graph matrix
```Python
GRAPH = [
    [0, int(weight0_0), int(weight0_1), ..., int(weight0_N)],
    ...
    [int(weightN_0), int(weightN_1), ..., 0]
]
```