'''
Depth First Search Algorithm

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges

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

'''
C++ Version of DFS
------------------------------
#include <vector>
#include <stack>
#include <set>
#include <map>

/*
 * This function implements the Depth-First Search (DFS) algorithm.
 *
 * Parameters:
 * graph (map<string, set<string>>): A map representing an adjacency list of the graph.
 * start (string): The starting vertex.
 *
 * Returns:
 * visited (vector<string>): A vector of vertices in the order they were visited.
 */

std::vector<std::string> dfs(std::map<std::string, std::set<std::string>> graph, std::string start) {
    // Create a vector to store the visited vertices
    std::vector<std::string> visited;

    // Create a stack for DFS
    std::stack<std::string> stack;
    stack.push(start);

    while (!stack.empty()) {
        // Pop a vertex from the stack
        std::string vertex = stack.top();
        stack.pop();

        // If the vertex is not visited before
        if (std::find(visited.begin(), visited.end(), vertex) == visited.end()) {
            // Mark the vertex as visited
            visited.push_back(vertex);

            // Add the vertices adjacent to the current vertex to the stack
            for (std::string adj : graph[vertex]) {
                if (std::find(visited.begin(), visited.end(), adj) == visited.end()) {
                    stack.push(adj);
                }
            }
        }
    }

    return visited;
}
'''