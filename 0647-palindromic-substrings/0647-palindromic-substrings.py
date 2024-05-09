class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        def pal(l,r):
            c=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                c+=1
                l-=1
                r+=1
            return c
        
        for i in range(len(s)):
            ans+=pal(i,i)+pal(i,i+1)
        return ans
        