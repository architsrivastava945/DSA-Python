class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        i,j = 0,0
        maxLen = 0
        while(j < len(s)-1):
            j += 1
            ch = s[j]
            dubIdx = i - 1
            for x in range(i,j):
                if s[x] == ch:
                    dubIdx = x
                    break
            i = dubIdx + 1
            maxLen = max(maxLen, j - i + 1)
        return maxLen
            

s = input()
obj = Solution()
ans = obj.lengthOfLongestSubstring(s)
print(ans)