class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort()
        lastidx=intervals[0][1]
        c=0
        for first,last in intervals[1:]:
            if first>=lastidx:
                lastidx=last
            else:
                c+=1
                lastidx=min(last,lastidx)
        return c

            

        
        