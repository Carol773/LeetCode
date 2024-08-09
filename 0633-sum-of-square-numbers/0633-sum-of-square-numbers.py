import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        lst=set()
        
        for i in range(0,int(floor(math.sqrt(c)+1))):
            lst.add(i*i)
            if (c-i*i) in lst or 2*i*i==c:
                return True
        return False
        