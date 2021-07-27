class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        ls_bk = list(brokenLetters)
        ls_txt = text.split(' ')
        for word in ls_txt:
            for letter in ls_bk:
                if letter in word:
                    res+=1
                    break
        return len(ls_txt) -res

test = 'hello world'
brokenLetters = 'ad'
print(Solution().canBeTypedWords(test,brokenLetters))