class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        n1=1
        n2=1
        
        for i in range(n-1):
            temp=n1
            n1=n1+n2
            n2=temp
        return n1
        