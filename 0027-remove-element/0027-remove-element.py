class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lst=[]
        
        for num in nums:
            if num!=val:
                lst.append(num)
        
        for i in range(len(lst)):
            nums[i]=lst[i]
        
        return len(lst)
        