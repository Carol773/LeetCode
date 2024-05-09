class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        word=set()
        maxele=0
        for r in range(len(s)):
            while s[r] in word:
                word.remove(s[l])
                l+=1
            word.add(s[r])
            maxele=max(maxele,r-l+1)
        return maxele