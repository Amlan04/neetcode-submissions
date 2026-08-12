class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s))+"#"+s
        return st

    def decode(self, s: str) -> List[str]:
        i,res = 0,[]
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length]) 
            i = j+1+length
        return res
