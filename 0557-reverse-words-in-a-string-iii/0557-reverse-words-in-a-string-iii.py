class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        lst=[]
        s=s.split()
        for ch in s:
            word=ch[::-1]
            lst.append(word)
            
        res=' '.join(x for x in lst)
        return res
        