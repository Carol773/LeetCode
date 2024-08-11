import math
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        a=2
        b=n
        
        lcm=a*b//gcd(a,b)
        return lcm
        
        
        
        