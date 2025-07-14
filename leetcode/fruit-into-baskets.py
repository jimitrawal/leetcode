class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a=0
        b=0
        maxlen = 1
        dict_fruit = dict()
        count = 0
        valid = True
        while b<len(fruits):
            if fruits[b] in dict_fruit.keys():
                dict_fruit[fruits[b]] += 1
                b+=1
                valid = True
            elif count< 2:
                dict_fruit[fruits[b]] = 1
                b+=1
                count +=1
                valid = True
            else:
                dict_fruit[fruits[a]] -= 1
                if dict_fruit[fruits[a]] == 0:
                    count-=1
                    del dict_fruit[fruits[a]]
                valid = False
                a+=1
            if valid and b-a > maxlen:
                maxlen=b-a
        return maxlen