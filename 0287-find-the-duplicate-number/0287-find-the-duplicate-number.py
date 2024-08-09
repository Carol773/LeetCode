class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
                
        for k,v in freq.items():
            if v!=1:
                return k
        