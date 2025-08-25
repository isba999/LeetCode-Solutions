class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splitted_s = s.split()
        
        return len(splitted_s[-1])

sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))