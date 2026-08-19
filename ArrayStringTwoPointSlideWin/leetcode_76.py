# Minimum Window Substring
# abc end = 2, start = 0, i = 0, j= 2, ab, abc
class Solution:
    def minWindow(self, s: str, t: str) -> str:  
        if len(t) > len(s):
            return ""
        start, end = 0, 0
        result = ""
        dub = []
        tempT = list(t)
        while(end < len(s)):
            for j in range(end, len(s)):
                if s[j] in tempT:
                    tempT.remove(s[j])
                    if len(tempT) == 0:
                        end = j + 1
                        break
                elif s[j] in t:
                    dub.append(s[j])
                    if len(tempT) == 0:
                        end = j + 1
                        break

            if len(tempT) > 0:
                break

            for i in range(start, len(s)):
                if s[i] not in t:
                    continue
                elif s[i] in dub:
                    dub.remove(s[i])
                else:
                    start = i
                    break

            if result == "" or end-start < len(result):
                result = s[start : end]

            tempT.append(s[start])
            start += 1
        return result        

s = input()
t = input()
obj = Solution()
result = obj.minWindow(s, t)
print(result)