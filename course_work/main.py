class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def kruskal(vertices, edges):
    mst = []
    disjoint_set = DisjointSet(vertices)
    total_weight = 0

    merge_sort(edges)

    for weight, v1, v2 in edges:
        if disjoint_set.find(v1) != disjoint_set.find(v2):
            disjoint_set.union(v1, v2)
            mst.append((v1, v2, weight))
            total_weight += weight

    return mst, total_weight


def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        vertices = file.readline().strip().split()
        graph = Graph(vertices)
        for i, line in enumerate(file.readlines()):
            weights = line.strip().split()
            for j, weight in enumerate(weights):
                if i != j and int(weight) > 0:
                    if graph.edges.count((int(weight), vertices[j], vertices[i])) == 0:
                        graph.add_edge(vertices[i], vertices[j], int(weight))
    return graph



file_path = 'graph.txt'
graph = read_graph_from_file(file_path)
mst, total_weight = kruskal(graph.vertices, graph.edges)

print("Минимальное остовное дерево:")
for edge in mst:
    print(f"{edge[0]} {edge[1]} вес {edge[2]}")
print(f"Суммарный вес: {total_weight}")
