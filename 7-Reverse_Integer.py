class Solution(object):
    def reverse(self, x):
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        sign = -1 if x < 0 else 1
        
        reversed_str = str(abs(x))[::-1]
        
        result = int(reversed_str) * sign
        
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result
