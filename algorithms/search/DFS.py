'''
Depth First Search Algorithm

If you want to watch a video instead I recommend this: 
https://youtu.be/PMMc4VsIacU?si=pa59yt-6OHQTgYcZ

How DFS Work
Its a Graph Traversal Algorithm that visits every vertex of the graph
DFS works by recursively going to the adjacent unvisited vertices

DFS is also known by some people as one of the usual ways people
explore Minecraft caves. You keep exploring a path until you hit a dead end
then you move back and find another path.

DFS ends when you come back to the starting node
'''

# https://youtu.be/PMMc4VsIacU?si=Qg7YafgBFGooq5vm&t=572

def dfs(graph, start):
    """
    This function implements the Depth-First Search (DFS) algorithm.

    Parameters:
    graph (dict): A dictionary representing an adjacency list of the graph.
    start (str): The starting vertex.

    Returns:
    visited (list): A list of vertices in the order they were visited.

    """

    # Create a list to store the visited vertices
    visited = []

    # Create a stack for DFS
    stack = [start]

    while stack:
        # Pop a vertex from the stack
        vertex = stack.pop()

        # If the vertex is not visited before
        if vertex not in visited:
            # Mark the vertex as visited
            visited.append(vertex)

            # Add the vertices adjacent to the current vertex to the stack
            stack.extend(graph[vertex] - set(visited))

    return visited