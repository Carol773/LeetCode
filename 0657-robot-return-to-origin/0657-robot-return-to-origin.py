class Solution:
    def judgeCircle(self, moves: str) -> bool:
        U=0
        L=0
        D=0
        R=0
        for ch in moves:
            if ch=='U':
                U+=1
            elif ch=='D':
                D+=1
            elif ch=='L':
                L+=1
            elif ch=='R':
                R+=1
                
        if R==L and U==D:
            return True
        else:
            return False
        