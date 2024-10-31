class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2 and nums[0]<nums[1]:
            return 1
        elif len(nums)==2 and nums[0]>nums[1]:
            return 0
        else:
            if nums[0]>nums[1]:
                return 0
            elif nums[-1]>nums[-2]:
                return len(nums)-1
            else:
            
        
                for i in range(1,len(nums)-1):
                    if nums[i]>nums[i+1] and nums[i-1]<nums[i]:
                        return i
        
        
            
        