def has_path(graph, start, end):
    """
    Determines if there is a path between two vertices in a directed graph using DFS.

    Args:
        graph: Dictionary representing the directed graph
        start: Starting vertex
        end: Target vertex

    Returns:
        bool: True if path exists, False otherwise
    """
    if start not in graph:
        return False

    visited = set()

    def dfs(current):
        if current == end:
            return True

        visited.add(current)

        # Check all neighbors of current vertex
        for neighbor in graph.get(current, []):
            if neighbor not in visited and dfs(neighbor):
                return True

        return False

    return dfs(start)


def print_all_paths(graph, start, end):
    """
    Prints all possible paths between two vertices in a directed graph.

    Args:
        graph: Dictionary representing the directed graph
        start: Starting vertex
        end: Target vertex
    """
    paths = []

    def dfs_paths(current, path, visited):
        if current == end:
            paths.append(path[:])
            return

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                path.append(neighbor)
                dfs_paths(neighbor, path, visited.copy())
                path.pop()

    dfs_paths(start, [start], set())

    if not paths:
        print(f"No path exists from {start} to {end}")
    else:
        print(f"All paths from {start} to {end}:")
        for path in paths:
            print(" -> ".join(path))


# Example graph from the task
simple_graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

# Larger test graph
test_graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': ['K'],
    'I': ['L'],
    'J': ['L'],
    'K': ['L'],
    'L': []
}


# Test cases
def run_tests():
    print("Testing simple graph:")
    test_cases_simple = [
        ('A', 'E', True), # expected True
        ('C', 'D', False),
        ('A', 'D', True),
        ('B', 'A', False),
        ('D', 'E', False)
    ]

    for start, end, expected in test_cases_simple:
        result = has_path(simple_graph, start, end)
        print(f"Path from {start} to {end}: {result} (Expected: {expected})")
        if result:
            print_all_paths(simple_graph, start, end)
        print()

    print("\nTesting larger graph:")
    test_cases_large = [
        ('A', 'L', True),
        ('C', 'L', True),
        ('E', 'K', False),
        ('G', 'J', False),
        ('A', 'K', True)
    ]

    for start, end, expected in test_cases_large:
        result = has_path(test_graph, start, end)
        print(f"Path from {start} to {end}: {result} (Expected: {expected})")
        if result:
            print_all_paths(test_graph, start, end)
        print()


if __name__ == "__main__":
    run_tests()