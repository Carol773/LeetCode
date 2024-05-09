class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sumele=0
        l=0
        res=float('inf')

        for r in range(len(nums)):
            sumele+=nums[r]
            while sumele>=target:
                res=min(res,r-l+1)
                sumele-=nums[l]
                l+=1
        if res!=float('inf'):
            return res
        else:
            return 0
        
            
        