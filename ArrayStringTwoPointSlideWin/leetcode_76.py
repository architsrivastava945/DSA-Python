# Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end = 0, 0
        result = ""
        while(end < len(s)):
            tempT = list(t)
            dub = []
            nextItr = end
            for j in range(nextItr, len(s)):
                if s[j] in tempT:
                    tempT.remove(s[j])
                    if len(tempT) == 0:
                        end = j
                        break
                elif s[j] in t:
                    dub.append(s[j])
            for i in range(nextItr, len(s)):
                if s[i] not in t:
                    continue
                elif s[i] in dub:
                    dub.remove(s[i])
                else:
                    start = i
                    break
            if j-i+1 < len(result):
                result = s[i:j+1]
        return result
        


s = input()
t = input()
obj = Solution()
result = obj.minWindow(s, t)
print(result)