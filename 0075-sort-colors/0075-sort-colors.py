class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        mid=0
        h=len(nums)-1
        
        while mid<=h:
            if nums[mid]==0:
                nums[l],nums[mid]=nums[mid],nums[l]
                l+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[h],nums[mid]=nums[mid],nums[h]
                h-=1
                
        return nums
            
        