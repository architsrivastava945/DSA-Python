def permute(nums: list[int]) -> list[list[int]]:
    result = []
    
    def backtrack(current_permutation: list[int], visited: list[bool]):
        # Base Case: If our permutation is the same length as nums, we found a full lineup!
        if len(current_permutation) == len(nums):
            result.append(list(current_permutation))
            return
            
        # For permutations, we always loop from 0 to len(nums) 
        # because we can pick any available number from the start!
        for i in range(len(nums)):
            # If this number is already used in our current path, skip it
            if visited[i]:
                continue
                
            # 1. Choose: Mark as visited and add to current permutation
            visited[i] = True
            current_permutation.append(nums[i])
            
            # 2. Explore: Recurse deeper
            backtrack(current_permutation, visited)
            
            # 3. Un-choose (Backtrack): Reset for the next branch
            current_permutation.pop()
            visited[i] = False

    backtrack([], [False] * len(nums))
    return result