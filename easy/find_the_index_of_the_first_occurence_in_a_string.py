class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        # sliding window comparison
        for i in range(len(haystack)-len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
                break
        return -1

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))