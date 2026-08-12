from collections import Counter
class Solution:
    def threeSumSortMethod(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        lenNum = len(nums)
        for i in range(lenNum-2):
            j = i + 1
            k = lenNum - 1
            target = 0 - nums[i]
            while(j < k):
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return result

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        FrqArr = Counter(nums)
        Length = len(FrqArr)
        for val, freq in FrqArr.items():


nums = list(map(int, input().split()))
obj = Solution()
result = obj.threeSum(nums)
print(result)