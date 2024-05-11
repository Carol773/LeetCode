class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        miss=1
        nums.sort()
        for i in nums:
            if i==miss:
                miss+=1
        return miss
        