class Solution:
    def isPalindrome(self, x: int) -> bool:
        count = 1
        num_count = x
        num_store = x
        if x < 0:
            return False
        elif x == 0:
            return True
        while num_count // 10 != 0:
            num_count = num_count // 10
            count +=1
        reverse_num = 0
        for i in range(count):
            right_digit = x % 10
            x = x // 10
            reverse_num = reverse_num*10 + right_digit
        if reverse_num % num_store == 0:
            return True
        else:
            return False