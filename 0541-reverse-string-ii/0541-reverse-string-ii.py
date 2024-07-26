class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res=''
        div=2*k
        for i in range(0,len(s),k):
            if (i%div)==0:
                new=s[i:i+k]
                res+=new[::-1]
            else:
                res+=s[i:i+k]
        return res
            