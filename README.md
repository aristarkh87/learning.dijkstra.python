# Dijkstra's algorithm
[![Build Status](https://travis-ci.com/aristarkh87/learning.dijkstra.python.svg?branch=master)](https://travis-ci.com/aristarkh87/learning.dijkstra.python)

Dijkstra's algorithm in Python. Example from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm.

## Usage
```
usage: main.py [-h] [-t {dict,matrix}] initial_node

Implementation of Dijkstra's algorithm.

positional arguments:
  initial_node          initial node in graph.

optional arguments:
  -h, --help            show this help message and exit
  -t {dict,matrix}, --type {dict,matrix}
                        type of graph description.
```

## Run tests
```bash
python -m unittest discover -v
```

## Graph_config
```Python
GRAPH_DICT = {
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

GRAPH_MATRIX = [
    [0, int(weight0_0), int(weight0_1), ..., int(weight0_N)],
    ...
    [int(weightN_0), int(weightN_1), ..., 0]
]
```