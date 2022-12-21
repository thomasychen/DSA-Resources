class Node:
        def __init__(self, k:int, val:str, size:int):
            self.value = val
            self.key = k
            self.left = None
            self.right = None
            self.size = size
class BST:
    def __init__(self):
        self.root = None
    def isEmpty(self) -> bool:
        return self.size() == 0
    def get_size(self) -> int:
        return self.size(self.root)
    def size(self, node: Node) -> int:
        return 0 if not node else node.size
    def add(self, key:int, val:str) -> None:
        if key and val:
            self.root = self.put(self.root,key, val)
        elif not key:
            return None
        else:
            self.delete(key)
    def put(self, node:Node, key:int, val:str) ->  Node:
        if not node:
            return Node(key, val, 1)
        elif key < node.key: 
            node.left = self.put(node.left, key, val)
        elif key > node.key:
            node.right = self.put(node.right, key, val)
        else: 
            node.value = val
        node.size = 1+ self.size(node.right) + self.size(node.left) 
        return node
    def contains(self, key:int) -> bool:
        return self.get(self.root,key) != None
    def get(self,node:Node, key: int) -> str:
        if not node:
            return None
        elif key < node.key:
            return self.get(node.left, key)
        elif key > node.key:
            return self.get(node.right, key)
        else:
            return node.value
    def remove(self, key: int) -> None:
        self.root = self.delete(self.root, key)
    def delete(self, node: Node, key:int) -> Node:
        if not node:
            return None
        elif key < node.key: 
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.left = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = node
            node = self.minimum(temp.right)
            node.right = self.deleteMin(temp.right)
            node.left = temp.left 
        node.size = self.size(node.left) + self.size(node.right) + 1
        return node
    def minimum(self, node:Node) -> Node:
        return node if not node.left else self.minimum(node.left)
    def deleteMin(self, node:Node) -> Node:
        if not node.left:
            return node.right
        node.left = self.deleteMin(node.left)
        node.size = self.size(node.left) + self.size(node.right) + 1
        return node
    def print_inorder(self):
        return self.inorder(self.root)
    def inorder(self, node:Node):
        if node:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)
r = BST()
r.add(50, "T")
r.add(30, "O")
r.add(20, "M")
r.add(40, "M")
r.add(70,"Y")
r.add(60, " ")
r.add(80, "C")
# Print inoder traversal of the BST
r.print_inorder()
print(r.root.value)
r.remove(50)
r.print_inorder()
print(r.root.value)
print(r.contains(80))
print(r.get_size())
    
