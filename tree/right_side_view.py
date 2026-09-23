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

from collections import deque

def rightSideView(root):
    if not root:
        return []
        
    res = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            curr = queue.popleft() # FIFO: Process nodes level by level from left to right
            
            # If this is the last node in the current level, add it to our result!
            if i == level_size - 1:
                res.append(curr.val) # Assuming node attribute is .val (or .value)
                
            # Add children for the next level
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                
    return res