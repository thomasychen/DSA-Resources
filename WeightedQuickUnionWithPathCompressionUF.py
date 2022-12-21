class WeightedQuickUnionWithPathCompressionUF:
    def __init__(self, n):
        self.arr = [-1] * n
    def connect(self, p, q) -> None:
        p_parent = self.parent(p)
        q_parent = self.parent(q)
        if p_parent != q_parent and self.arr[p_parent] != self.arr[q_parent]:
            big_p = max(p_parent, q_parent, key = lambda x: -self.arr[x])
            little_p= min(p_parent, q_parent, key = lambda x: -self.arr[x])
        elif p_parent != q_parent and self.arr[p_parent] == self.arr[q_parent]:
            big_p = min(p_parent, q_parent)
            little_p = max(p_parent, q_parent)
        child_size = self.arr[little_p]
        self.arr[big_p] += child_size
        self.arr[little_p] = big_p
    def find(self, p):
        parent = self.parent(p)
        if parent != p:
            self.arr[p] = parent
        return parent    
    def parent(self, i):
        if self.arr[i] < 0:
            return i
        return self.parent(self.arr[i])
    def is_connected(self, p, q):
        return p == q or self.find(p) == self.find(q)

groups = WeightedQuickUnionWithPathCompressionUF(10)
groups.connect(0,9)
groups.connect(1,8)
groups.connect(2,7)
groups.connect(3,6)
groups.connect(4,5)
print(groups.arr)
groups.connect(5,1)
groups.connect(8,7)
print(groups.arr)
groups.find(7)
groups.find(5)
print(groups.arr)