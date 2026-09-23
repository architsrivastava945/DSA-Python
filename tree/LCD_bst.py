def lcd_in_bst(root, p, q):
    if not root or p.val <= root.val <= q.val:
        return root
    right_travel = lcd_in_bst(root.right, p, q)
    left_travel = lcd_in_bst(root.left, p, q)

    return right_travel if right_travel else left_travel

def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    
    while curr:
        # If both p and q are smaller than curr, go left
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        # If both p and q are greater than curr, go right
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            # They have split! Current node is the LCA
            return curr
            
    return None