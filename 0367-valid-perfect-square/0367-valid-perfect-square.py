class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        perf=int(math.sqrt(num))
        if (perf*perf)==num:
            return True
        else:
            return False
        