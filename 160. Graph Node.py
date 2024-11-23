def find_all_path(graph):
    def dfs(node, path):
        if node == len(graph)-1:
            res.append(path)
            return
        for neighbor in graph[node]:
            dfs(neighbor, path+[neighbor])
        
    res = []
    dfs(0, [0])
    return res

graph = [[1,2],[3],[3],[]]
print(find_all_path(graph))  # Output: [[0,1,3],[0,2,3]]