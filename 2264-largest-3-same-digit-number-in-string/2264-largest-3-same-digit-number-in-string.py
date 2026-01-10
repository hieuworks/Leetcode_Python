class Solution:
    def largestGoodInteger(self, num: str) -> str:
        size = len(str(num))
        dic = {}
        for i in range(1, size + 1):
            right_digits=int(num) % 10
            num = int(num) // 10
            dic[i] = right_digits

        compare = [] 
         #e.g size = 5 -> 1-4 / n digits -> 1 - n-2 digits -> 1, size -1 ( size - 1 = n - 2 )
        for i in range(1, size - 1): 
           
            if dic[i] == dic[i+1] and dic[i+1] == dic[i+2]:
                triple = dic[i], dic[i+1], dic[i+2]
                compare.append(triple)
        if len(compare) == 0:
            return ""
        else:
            largest_triple = max(compare)
            if largest_triple[0] > 0:
                a = largest_triple[0] * 100 + largest_triple[1] * 10 + largest_triple[2]
                result = f"{a}"
            elif largest_triple[0] == 0:
                result = "000"
            return result


