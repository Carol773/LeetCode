class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        c=0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                if (hours[i]+hours[j])%24==0:
                    c+=1
        return c
        