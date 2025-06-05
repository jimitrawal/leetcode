class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic=dict()
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in dic:
                return False
            else:
                dic[t[i]] -= 1
        return max(dic.values())==0 and min(dic.values())==0