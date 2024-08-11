class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        for i in range(0,len(rectangles)):
            rectangles[i]=rectangles[i][0]/rectangles[i][1]
    
        dic={}
        for i in rectangles:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=0
        l=dic.values()
        for i in l:
            ans+=(i*(i-1)//2)
        return ans