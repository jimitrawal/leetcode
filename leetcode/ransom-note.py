class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        dict_ransom = {}
        dict_mag = {}
        for i in ransomNote:
            if i not in dict_ransom:
                dict_ransom[i] = 1
            else:
                dict_ransom[i] += 1
        for i in magazine:
            if i not in dict_mag:
                dict_mag[i] = 1
            else:
                dict_mag[i] += 1
        for k,v in dict_ransom.items():
            if k not in dict_mag:
                return False
            elif dict_mag[k] < v:
                return False
        return True