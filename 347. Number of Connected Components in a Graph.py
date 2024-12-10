from collections import defaultdict

def count_components(n, edges):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    graph=defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited=set()
    components=0
    
    for node in range(n):
        if node not in visited:
            dfs(node)
            components+=1
    return components

# Example Usage
edges = [[0, 1], [1, 2], [3, 4]]
n = 5
print(count_components(n, edges))  # Output: 2