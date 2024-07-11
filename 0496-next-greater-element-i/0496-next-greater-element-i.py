class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        lst=[]
        
        for num in nums1:
            idx=nums2.index(num)
            for i in range(idx+1,len(nums2)):
                if num<nums2[i]:
                    lst.append(nums2[i])
                    break
            if (len(lst)-1)!=nums1.index(num):    
                lst.append(-1)
        return lst
                
        