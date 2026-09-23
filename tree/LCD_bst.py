def lcd_in_bst(root, p, q):
    if not root or p.val <= root.val <= q.val:
        return root
    right_travel = lcd_in_bst(root.right, p, q)
    left_travel = lcd_in_bst(root.left, p, q)

    return right_travel if right_travel else left_travel