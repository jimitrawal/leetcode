class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        og=0
        if (len(s)==0):
            return True
        if (len(t)==0):
            return False
        while (og<(len (s)) and (i<(len (t)))):
            if (s[og]==t[i]) and (og==len(s)-1):
                return True
            elif(s[og]==t[i]):
                og+=1
                i+=1
            elif ((og==len(s)-1) and (i==len(t)-1)) or (i==len(t)-1):
                return False
            else:
                i+=1
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """