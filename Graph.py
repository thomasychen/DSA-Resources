import heapq
class Graph:
    def __init__(self, v):
        self.size = v
        self.edges = {i:[] for i in range(v)}
    def addEdge(self, a, b, weight):
        self.edges[a].append((b, weight))
        self.edges[b].append((a, weight))
    def BFS(self, s):
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)
        while queue:
            s = queue.pop(0)
            print(s)
            for i,dist in self.edges[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
    def DFS(self, s):
        visited = set()
        stack = []
        stack.append(s)
        visited.add(s)
        while stack:
            s = stack.pop()
            print(s)
            for i,dist in self.edges[s]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
    def Djikstra(self, s):
        visited = set()
        priority_queue = []
        dist_to = {i:float("inf") for i in range(self.size)}
        edge_to = {i:None for i in range(self.size)}

        dist_to[s] = 0
        for i in dist_to:
            heapq.heappush(priority_queue, (dist_to[i], i, None))

        while priority_queue:
            poppedNode = heapq.heappop(priority_queue)[1]
            visited.add(poppedNode)

            for child in self.edges[poppedNode]:
                if child[0] not in visited:
                    potential_dist = dist_to[poppedNode] + child[1]
                    if potential_dist < dist_to[child[0]]:
                        priority_queue.remove((dist_to[child[0]],child[0], edge_to[child[0]]))
                        dist_to[child[0]] = potential_dist
                        edge_to[child[0]] = poppedNode
                        heapq.heappush(priority_queue, (dist_to[child[0]],child[0], edge_to[child[0]]))
        return dist_to, edge_to
    
    def AStar(self, s, f,h):
        visited = set()
        priority_queue = []
        dist_to = {i:float("inf") for i in range(self.size)}
        edge_to = {i:None for i in range(self.size)}

        dist_to[s] = 0
        heapq.heappush(priority_queue, (h(s), s, None))
        for i in dist_to:
            if i != s:
                heapq.heappush(priority_queue, (dist_to[i], i, None))

        while priority_queue:
            poppedNode = heapq.heappop(priority_queue)[1]
            visited.add(poppedNode)
            if poppedNode == f:
                path_to_f = self.get_shortest_path(edge_to, f)
                return dist_to[f], path_to_f
            for child in self.edges[poppedNode]:
                if child[0] not in visited:
                    potential_dist = dist_to[poppedNode] + child[1]
                    if potential_dist < dist_to[child[0]]:
                        priority_queue.remove((dist_to[child[0]],child[0], edge_to[child[0]]))
                        dist_to[child[0]] = potential_dist
                        edge_to[child[0]] = poppedNode
                        heapq.heappush(priority_queue, (dist_to[child[0]] + h(child[0]),child[0], edge_to[child[0]]))
                                 
    def get_shortest_path(self,edgeMap, f):
        if edgeMap[f] == None:
            return [f]
        else:
            return self.get_shortest_path(edgeMap, edgeMap[f]) + [f]
    
def heuristic(node):
    map = {0:4, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3,7: 5, 8: 5, 9:4}
    return map[node]
    
            


g = Graph(10)
g.addEdge(0,1, 1)
g.addEdge(1,2, 1)
g.addEdge(2,3, 1)
g.addEdge(3,4, 1) 
g.addEdge(0,5, 2)
g.addEdge(5,6, 2)
g.addEdge(6,7, 2)
g.addEdge(7,8, 2)
g.addEdge(8,9, 2)
g.DFS(0)
print("BFS")
g.BFS(0)
print(g.Djikstra(0))
print(g.AStar(0, 4, heuristic))

    
           
