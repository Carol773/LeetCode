class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        org=[]
        
        for num in nums:
            if num not in org:
                org.append(num)
                
        for i in range(len(org)):
            nums[i]=org[i]
        return len(org)
        