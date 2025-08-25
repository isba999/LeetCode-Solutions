class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s_digits = ""
        next_digits = []
        for i in range(len(digits)):
            s_digits = s_digits + str(digits[i])

        next_int = int(s_digits) + 1

        next_digits = [int(digit) for digit in str(next_int)]

        return next_digits
        
    
sol = Solution()
print(sol.plusOne([11,9]))
