class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        while len(str(n))>1:
            nsum=0
            for i in str(n):
                nsum+=int(i)**2
            n=nsum
        if n==1 or n==7:
            return True
        else:
            return False
        