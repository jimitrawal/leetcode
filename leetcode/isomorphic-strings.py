class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = dict()
        dic_t = dict()
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = [i]
            else:
                dic_s[s[i]].append(i)
        for i in range(len(t)):
            if t[i] not in dic_t:
                dic_t[t[i]] = [i]
            else:
                dic_t[t[i]].append(i)
        if len(dic_s.values()) != len(dic_t.values()):
            return False
        for i in range(len(dic_s.values())):
            lis_s = []
            lis_t = []
            lis_s = list(dic_s.values())[i]
            lis_t = list(dic_t.values())[i]
            if len(lis_s) != len(lis_t):
                return False
            for j in range(len(lis_s)):
                if lis_s[j] != lis_t[j]:
                    return False
        return True