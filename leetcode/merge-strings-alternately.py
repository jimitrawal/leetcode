class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        short=0
        if len(word1)>len(word2):
            short=word2
            longe=word1
        else:
            short=word1
            longe=word2

        final=""
        for i in range(len(short)):
            final+=word1[i]
            final+=word2[i]
        final+=longe[len(short):]
        return final