class Graph:
 
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
    
    def addEdge(self, u, v):
 
        # Add v to u’s list.
        self.adj[u].append(v)

    def count_dfs(self, graph, u, d, vis):
        if(u == d):
            return 1
        vis[u] = True
        ans = 0
        for v in graph[u]:
            if(vis[v] == False):
                ans += self.count_dfs(graph, v, d, vis)
        vis[u] = False
        return ans
        
    def possible_paths(self, graph, n, s, d):
        # graph = [[] for i in range(n)]
        # for e in edges:
        #     graph[e[0]].append(e[1])
        vis = [False for i in range(n)]
        return self.count_dfs(graph, s, d, vis)

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    # g.addEdge(0, 2)
    g.addEdge(0, 3)
    # g.addEdge(2, 0)
    g.addEdge(1, 2)
    g.addEdge(3, 2)
    print(g.adj)
    n = 4 
    s = 0
    d = 2
    r = g.possible_paths(g.adj, n, s, d)
    print("possible_paths", r)