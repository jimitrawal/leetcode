class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = dict()
        i=0
        tag = False
        tot=len(s)
        while i < len(s):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
            i+=1
        for i in hashmap.values():
            if tag==True and i%2 == 1:
                tot-= 1
            elif i%2 == 1:
                tag = True
        return tot