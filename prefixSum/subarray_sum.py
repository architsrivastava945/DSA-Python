# Problem:Given an integer array nums (which can have negative numbers, zeros, and positives) and an integer k, return the total number of continuous subarrays whose sum equals k.Example: nums = [1, 1, 1], k = 2 $\to$ Output: 2 (the subarrays are nums[0..1] and nums[1..2]).Example: nums = [1, -1, 0], k = 0 $\to$ Output: 3 (subarrays: [1, -1], [0], [1, -1, 0]).

nums = list(map(int, input().split()))
k = int(input())
prefix_counts = {0:1} #presum : freq, to handle case when current_sum becomes k
current_sum = 0
ans = 0

for num in nums:
    current_sum += num
    if current_sum - k in prefix_counts:
        ans += prefix_counts[current_sum-k]
    prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

print(ans)