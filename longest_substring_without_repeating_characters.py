class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = ""
        f = ""
        for i in range(len(s)):
            if s[i] not in f:
                f += s[i]
            else:
                if len(d) < len(f):
                    d = f
                f = f[f.index(s[i])+1::] + s[i]
              
        return max(len(d), len(f))
            
        