class TreeNode:
    def __init__(self, L, R, sum=0):
        self.L = L
        self.R = R
        self.sum = sum
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.root = TreeNode(0, len(array) - 1)
    
    def build(self, L, R):
        if L == R:
            return TreeNode(L, R, self.array[L])
        
        M = (L + R) // 2
        node = TreeNode(L, R)
        node.left = self.build(L, M)
        node.right = self.build(M + 1, R)
        node.sum = node.left.sum + node.right.sum

        return node

    def update(self, index, val, node):
        if node.L == index == node.R:
            node.sum = val