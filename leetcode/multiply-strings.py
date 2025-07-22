class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        res = 0
        for i in range(len(num1)):
            temp_res = ""
            for j in range(len(num2)):
                temp_res += str((carry+int(num1[i])*int(num2[j]))%10)
                carry = (carry+int(num1[i])*int(num2[j]))//10
                if carry>0 and j==len(num2)-1:
                    temp_res += str(carry)
            carry = 0
            res += int(temp_res[::-1])*(10**i)
        return str(res)