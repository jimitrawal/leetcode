class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        end = 0
        vowels = {"a","e","i","o","u"}
        maxlen = 0
        vowelcount = 0
        while end<len(s):
            if end-start<k:
                if s[end] in vowels:
                    vowelcount+=1
                end+=1
                if vowelcount>maxlen:
                    maxlen=vowelcount
            else:
                if s[start] in vowels:
                    vowelcount-=1
                start+=1
        return maxlen