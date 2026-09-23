# Practice Challenge: Tree Views (Infosys Favorite)
# Problem: Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.

# Example:

# Plaintext
#       1 <---
#     /   \
#    2     3 <---
#     \     \
#      5     4 <---

def right_side_view(root):
    stack = [root]
    res = []
    while stack:
        level = []
        for _ in range(len(stack)):
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            level.append(curr.value)
        res.append(level[-1])
    return res