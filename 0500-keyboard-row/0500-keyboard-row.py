class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=list("qwertyuiop")
        b=list("asdfghjkl")
        c=list("zxcvbnm")
        k=[]
        
        def keyboard(word,l):
            return all(k in l for k in word.lower())
        
        for i in words:
            if keyboard(i,a) or keyboard(i,b) or keyboard(i,c)==True:
                k.append(i)
        return k
        
        
        
        
        