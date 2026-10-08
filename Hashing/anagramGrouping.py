from collections import defaultdict
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for str in strs:
            freq = [0]*26
            for s in str:
                freq[ord(s) - ord('a')] += 1
            key = ""
            for i in range(26):
                if freq[i] > 0:
                    key = key + f"{chr(i+ord('a'))}{freq[i]}" # key = "" + "a1" + "e1" + "t1"
            result[key].append(str)
        return list(result.values())



    def groupAnagrams5percBeats(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for str in strs:
            freq = Counter(str)
            a = list(freq.items())
            y = sorted(a,key = lambda x: (x[0], x[1]))
            s = [f'{x[0]}{x[1]}' for x in y]
            result["".join(s)].append(str)
        return list(result.values())

strs = input().split()
obj = Solution()
result = obj.groupAnagrams(strs)
print(result)

