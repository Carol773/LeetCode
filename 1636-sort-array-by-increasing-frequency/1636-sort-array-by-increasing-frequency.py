class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        lst=[]
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
                
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
        