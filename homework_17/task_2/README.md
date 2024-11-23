# Graph Path Finder

This Python program implements a path finding algorithm for directed graphs. It can determine whether a path exists between any two vertices and can also print all possible paths between them.

## Graph Visualization

### Simple Graph (from original example)
```
A ─────► B ─────► D
│
└────────► C ─────► E
```

### Test Graph
```
          ┌─────► E ─────► I ───┐
          │                     │
A ─────► B ─────► F ─────► J ───┤
│                               │
├─────► C ─────► G ──────► K ───┤
│                │         │    │
│       ┌────────┘         │    │
│       │                  │    │
└─────► D ─────► H ────────┘    └─►L
```

## Features

- Path existence checking using depth-first search (DFS)
- All possible paths enumeration between two vertices
- Comprehensive test cases for both simple and complex graphs
- Support for any directed graph represented as an adjacency list

## Usage

```python
# Create a graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

# Check if path exists
result = has_path(graph, 'A', 'E')  # Returns True

# Print all possible paths
print_all_paths(graph, 'A', 'E')  # Prints: A -> C -> E
```

## Test Cases

The program includes test cases for both the simple graph and a larger test graph. The test cases verify:
- Direct paths
- Multi-hop paths
- Non-existent paths
- Dead-end scenarios
- Multiple possible paths between vertices

## Implementation Details

- The `has_path` function uses DFS to efficiently determine path existence
- The `print_all_paths` function uses a modified DFS to find and print all possible paths
- Both functions handle cases where vertices don't exist in the graph
- The implementation prevents infinite loops by tracking visited vertices


# What is Depth-First Search (DFS)

Depth-First Search (DFS) is a popular algorithm used for traversing or searching through graph or tree data structures. It explores as far as possible along each branch before backtracking, making it a "depth-first" approach.

---

## Characteristics of DFS

1. **Recursive Nature**:  
   DFS can be implemented recursively or iteratively using a stack.

2. **Complete Exploration**:  
   DFS explores every possible path before moving to other branches, ensuring thorough exploration.

3. **Backtracking**:  
   When DFS reaches a node with no unvisited neighbors, it backtracks to the previous node and continues the search.

4. **Space Complexity**:  
   - Space complexity is determined by the recursion stack or the stack used in the iterative approach.
   - Worst case: \(O(V)\), where \(V\) is the number of vertices.

5. **Time Complexity**:  
   - The time complexity of DFS is \(O(V + E)\), where:
     - \(V\) is the number of vertices.
     - \(E\) is the number of edges.

---

## Algorithm Steps

### Input
- A graph represented as an adjacency list or adjacency matrix.
- A starting vertex.

### Output
- A list or sequence of visited nodes.

### Procedure
1. **Initialization**:  
   Mark the starting node as visited.

2. **Visit Neighbors**:  
   For each unvisited neighbor of the current node:
   - Mark it as visited.
   - Recursively (or iteratively) visit its neighbors.

3. **Backtrack**:  
   If a node has no unvisited neighbors, return to the previous node and repeat.

---

## Pseudocode (Recursive Implementation)

```python
def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

## Viualization
**Consider the Graph**

```plaintext
    A
   / \
  B   C
 /   / \
D   E   F
```
**Adjacency List**
```python
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': []
}
```

**DFS Traversal Starting from 'A'**

    Order of Visiting: A → B → D → C → E → F

## Key Considerations

 - DFS is not guaranteed to find the shortest path in graphs. For shortest paths, consider using Breadth-First Search (BFS) or Dijkstra's algorithm.
 - In large graphs, DFS might go very deep, leading to potential stack overflow in recursive implementations.
