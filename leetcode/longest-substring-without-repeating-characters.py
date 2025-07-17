class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        start = 0
        chars = set()
        maxlen = 1
        end = 0
        while end < len(s):
            if s[end] not in chars:
                chars.add(s[end])
                if 1+end-start > maxlen:
                    maxlen = 1+end-start
                end+=1
            else:
                chars.remove(s[start])
                start+=1
            
        return maxlen