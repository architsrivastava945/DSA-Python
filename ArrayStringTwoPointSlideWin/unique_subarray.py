def unique_subarray(nums):
    res = [[]]
    n = len(nums)
    for i in range(n):
        k = i
        while k and nums[k] == nums[k-1]:
            k += 1
        for j in range(k, n):
            res.append(nums[i:j+1]) 

    return res


print(unique_subarray([1,2,2,2,3]))