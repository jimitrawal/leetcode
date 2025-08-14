class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        se=set()
        c=0
        for i in range(len(jewels)):
            se.add(jewels[i])
        for i in range(len(stones)):
            if stones[i] in se:
                c+=1
        return c