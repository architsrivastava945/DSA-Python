class Solution:
    def findSubstringOld(self, s: str, words: list[str]) -> list[int]:
        cartisianTable = []
        cartisianTable.append([words.pop()])
        for word in words:
            lenght = len(cartisianTable[0])
            tempCartisianTable = cartisianTable
            # print("tempcartisiantable:",tempCartisianTable)
            cartisianTable = []
            for i in tempCartisianTable:
                for j in range(lenght+1):
                    # print('i:',i,'j:',j)
                    newWord = [*i[:j],word,*i[j:]]
                    # print("newWord:",newWord)
                    if(newWord not in cartisianTable):
                        cartisianTable.append(newWord)
        # print("final cartisian : ", cartisianTable)
        updatedCartisianTable = list(map(''.join, cartisianTable))
        print(updatedCartisianTable)
        j = len(updatedCartisianTable[0])
        i = 0
        ans = []
        while(j <= len(s)):
            if(s[i:j] in updatedCartisianTable):
                ans.append(i)
            i += 1
            j += 1
        return ans

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        j = len("".join(words))
        i = 0
        while(j <= len(s)):
            for x in s[i:j]:
                tempWords = words
                for y in tempWords:
                    if x == y[0]:
                        z = len(y)
                        if s[i:z] == y:
                            s[i:z] = ""
                            tempWords.remove(y)
        



# s = input('s = ')
s = "xxx"
words = input('words = ').split()
# print(words)
object = Solution()
ans = object.findSubstring(s, words)
print(ans)