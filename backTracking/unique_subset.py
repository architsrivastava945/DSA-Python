# Challenge Problem: Combinations / Subsets II (With Duplicates)
# Let's test this template on an interview problem.

# Problem:
# Given an integer array nums that may contain duplicates (e.g., nums = [1, 2, 2]), return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example: nums = [1, 2, 2]

# Valid output:
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

# Notice that [2] appears only once in the output, even though there were two 2s in the input!

# Think About This:
# If we sort nums first (nums.sort()), identical numbers sit right next to each other: [1, 2, 2].

# When we are deciding which number to pick at a given step, how do we avoid picking the second 2 if we already explored picking the first 2 at this same level?

# nums = list(map(int, input().split()))

# def unique_subsets(nums):
#     nums.sort()
#     i, j = 0, 0
#     ans = [[]]
#     while i < len(nums):
#         localAns = []
#         while j < len(nums):
#             localAns.append(nums[j])
#             ans.append(localAns)


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()  # Step 1: Sorting clusters identical elements together
    result = []
    
    def backtrack(start_index: int, current_subset: list[int]):
        # Every state we land on is a valid subset!
        # We must append a COPY of current_subset
        result.append(list(current_subset))
        
        for i in range(start_index, len(nums)):
            # If this element is a duplicate of the previous element at the SAME level, skip it!
            if i > start_index and nums[i] == nums[i - 1]:
                continue
                
            # 1. Choose: Include nums[i] in the current subset
            current_subset.append(nums[i])
            
            # 2. Explore: Recurse forward to pick the next elements (starting at i + 1)
            backtrack(i + 1, current_subset)
            
            # 3. Un-choose (Backtrack): Remove nums[i] so we can try alternative paths
            current_subset.pop()

    backtrack(0, [])
    return result

print(subsets_with_dup([3,2,2,1,2]))
