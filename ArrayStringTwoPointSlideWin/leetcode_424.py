# 424. Longest Repeating Character Replacement
from collections import Counter
class Solution:
    def calc_unmatch(self, tempS):
        if len(tempS) < 1:
            return (0, "NA")
        freq = Counter(tempS)
        maxFreq = freq[tempS[0]]
        maxKey = tempS[0]
        for key, value in freq.items():
            if value > maxFreq:
                maxFreq = value
                maxKey = key
        return (len(tempS) - maxFreq, maxKey)


    def characterReplacement(self, s: str, k: int) -> int:
        unmatch = 0
        i,j = 0,k
        maxLen = j - i
        (unmatch, key) = self.calc_unmatch(s[i:j])
        while j < len(s):
            if unmatch > k:
                if s[i] != key:
                    unmatch -= 1
                i += 1
            else:
                if s[j] != key:
                    unmatch += 1
                j += 1
            if unmatch > ((j-i)/2):
                (unmatch, key) = self.calc_unmatch(s[i:j])
            if unmatch <= k:
                localMax = j - i
                if localMax > maxLen:
                    maxLen = localMax
        return maxLen


s = input()
k = int(input())
Obj = Solution()
result = Obj.characterReplacement(s, k) 
print(result)

# Input: s = "AABABBA", k = 1
# Output: 4