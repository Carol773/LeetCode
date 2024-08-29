from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        new=set()
        l=[]
        
        for i in range(0,len(s)):
            dna=s[i:i+10]
            if dna in new:
                if dna not in l:
                    l.append(dna)
            new.add(dna)
        return l
        