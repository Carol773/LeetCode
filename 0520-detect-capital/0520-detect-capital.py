class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if word.islower() or word.isupper() or word.istitle():
            return True
        else:
            return False