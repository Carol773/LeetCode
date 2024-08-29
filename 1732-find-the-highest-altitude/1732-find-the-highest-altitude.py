class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=[0]*(len(gain)+1)
        
        for i in range(len(gain)):
            dist=(gain[i]+alt[i])
            alt[i+1]=dist
        return max(alt)
        
        
        