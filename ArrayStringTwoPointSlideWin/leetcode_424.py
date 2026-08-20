# 424. Longest Repeating Character Replacement
class Solution:
    def calc_unmatch(self, tempS):
        if len(tempS) < 1:
            return 0
        tempS = list(tempS)
        tempS.sort()
        key = tempS[int(len(tempS)/2)]
        unmatch = 0
        for i in tempS:
            if i != key:
                unmatch += 1
        return unmatch

    def characterReplacement(self, s: str, k: int) -> int:
        unmatch = 0
        maxLen = 0
        i,j = 0,0
        while j < len(s):
            if unmatch > k:
                i += 1
                unmatch = self.calc_unmatch(s[i:j])
            else:
                j += 1
                unmatch = self.calc_unmatch(s[i:j])
            if unmatch <= k:
                maxLen = max(maxLen, j-i)
        return maxLen


s = input()
k = int(input())
Obj = Solution()
result = Obj.characterReplacement(s, k)
print(result)