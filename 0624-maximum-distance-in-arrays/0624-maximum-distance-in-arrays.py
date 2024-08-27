class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        max_dist=0
        smallest=arrays[0][0]
        biggest=arrays[0][-1]
        
        for i in range(1,len(arrays)):
            arr=arrays[i]
            max_dist=max(max_dist,abs(arr[-1]-smallest),abs(biggest-arr[0]))
            smallest=min(smallest,arr[0])
            biggest=max(biggest,arr[-1])
        return max_dist
                        
                
            
            
            
        