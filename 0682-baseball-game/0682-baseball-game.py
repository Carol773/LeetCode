class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        
        for op in operations:
            
            if op=='C':
                stack.pop()
            elif op=='D':
                ele=stack[-1]
                stack.append(2*ele)
            elif op=='+':
                op1=stack[-1]
                op2=stack[-2]
                res=int(op1)+int(op2)
                stack.append(res)
            else:
                int_op=int(op)
                stack.append(int_op)
        if stack:
            return sum(stack)
        else:
            return 0
                
        