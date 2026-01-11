import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:        
        if n == 0 or  n < 0:
            return False
        checkType = math.log(n, 4)
        if checkType.is_integer():
            return True
        else:
            return False       
