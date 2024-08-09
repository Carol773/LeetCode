class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst=[]
        n=len(nums)
        for i in range(len(nums)):
            if n%(i+1)==0:
                lst.append(nums[i]*nums[i])
        return sum(lst)
            
        