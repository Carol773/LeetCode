class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        if (len(flowerbed)==1 and flowerbed[0]==0 and n>=0):
            return True
        elif len(flowerbed)==1 and n>=0:
            return False
        if flowerbed[0]==flowerbed[1]==0:
            flowerbed[0]=1
            n-=1
            if n==0:
                return True
        if flowerbed[len(flowerbed)-1]==flowerbed[len(flowerbed)-2]==0:
            flowerbed[len(flowerbed)-1]=1
            n-=1
            if n==0:
                return True
        
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
                if n==0:
                    return True
        
        return False
        