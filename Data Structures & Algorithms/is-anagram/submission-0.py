class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            scounts={}
            for char in s:
                if char in scounts:
                    scounts[char]=scounts[char]+1
                else:
                    scounts[char]=1;
            tcount={}
            for char in t:
                if char in tcount:
                    tcount[char]=tcount[char]+1
                else:
                    tcount[char]=1
        return scounts == tcount