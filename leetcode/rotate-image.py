class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix)-1
        t = 0
        b = len(matrix)-1
        while l<r:
            for i in range(r-l):
                xtra = matrix[t+i][l]
                matrix[t+i][l] = matrix[b][l+i]
                matrix[b][l+i] = matrix[b-i][r]
                matrix[b-i][r] = matrix[t][r-i] 
                matrix[t][r-i] = xtra
            l+=1
            r-=1
            t+=1
            b-=1