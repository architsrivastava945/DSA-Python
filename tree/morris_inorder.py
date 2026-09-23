class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morris_inorder(root: TreeNode) -> list[int]:
    res = []
    curr = root
    
    while curr:
        if not curr.left:
            # 1. No left child, visit current and go right
            res.append(curr.val)
            curr = curr.right
        else:
            # 2. Has left child. Find the predecessor (rightmost node in left subtree)
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
                
            if not pred.right:
                # Establish temporary thread back to curr
                pred.right = curr
                curr = curr.left
            else:
                # Thread already exists! Cut it, visit curr, and go right
                pred.right = None
                res.append(curr.val)
                curr = curr.right
                
    return res