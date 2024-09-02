class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)!=len(s.split()):
            return False
        else:  
             return (len(set([x+y for x,y in zip (pattern,s.split())]))==(len(set(pattern))) and (len(set([x+y for x,y in zip (pattern,s.split())]))==(len(set(s.split()))))) 