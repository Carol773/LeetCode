class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lst=[]
        i=0
        p_sort=sorted(p)
        p_len=len(p)
        while i < (len(s)-p_len+1):
            if p_sort==sorted(s[i:i+len(p)]):
                lst.append(i)
            i+=1
        return lst
            
        