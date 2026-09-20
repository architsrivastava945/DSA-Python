# Challenge Problem: Next Greater Element (Infosys Classic)Given an array of integers nums = [2, 1, 2, 4, 3], return an array res of the same length where res[i] is the next greater element to the right of nums[i]. If no greater element exists to the right, put -1.For 2 (index 0), next greater is 4.For 1 (index 1), next greater is 2.For 2 (index 2), next greater is 4.For 4 (index 3), next greater is -1 (no one taller to the right).For 3 (index 4), next greater is -1.Output: [4, 2, 4, -1, -1].The Task:Solve this in $O(N)$ time using a monotonic stack.Do you store the values or the indices on the stack? Why?When you see a new number x that is larger than the stack top, what happens to the elements on the stack?Outline your logic or write the Python loop!

nums = list(map(int, input().split()))
stack = [] #store indices
n = len(nums)
ans = [0]*n

for i in range(n-1, -1, -1):
    if not stack or nums[i] > nums[stack[-1]]:
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()
        stack.append(i)
    ans[i] = nums[stack[-1]]

print(ans)

#Ai ans
def next_greater_element(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [-1] * n
    stack = []  # Stores indices of elements in monotonic descending order
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Kick out everyone who is shorter than or equal to current person
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
            
        # If someone survived, they are the first taller person to the right
        if stack:
            ans[i] = nums[stack[-1]]
            
        # Push current index onto the stack
        stack.append(i)
        
    return ans