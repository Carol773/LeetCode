class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m=len(grid[0])
        n=len(grid)
        neg=0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]<0:
                    neg+=1
        return neg
        