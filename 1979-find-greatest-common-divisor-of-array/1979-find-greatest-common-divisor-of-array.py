class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=min(nums)
        n=max(nums)
        
        while n!=0:
            rem=m%n
            m=n
            n=rem
        return m
        