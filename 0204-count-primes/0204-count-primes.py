class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst=[]
        
        isPrime=[True]*(n)
        if n<=2:
            return 0
        i=2
        while i*i<n:
            if isPrime[i]:
                for j in range(i*i,n,i):
                    isPrime[j]=False
            i+=1
            
        
        return isPrime.count(True)-2
        