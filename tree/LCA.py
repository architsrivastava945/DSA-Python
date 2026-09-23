def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Base Case: if tree is empty, or we found either p or q
    if not root or root == p or root == q:
        return root
        
    # Search in left and right subtrees
    left_result = lowest_common_ancestor(root.left, p, q)
    right_result = lowest_common_ancestor(root.right, p, q)
    
    # If p and q were found in separate subtrees, current root is the LCA!
    if left_result and right_result:
        return root
        
    # Otherwise, return whichever side found something (or None if neither)
    return left_result if left_result else right_result