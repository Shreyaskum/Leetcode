class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = {}
        prev = ''
        if numRows == 1:
            return s
        for j in range(len(s)):
            z = j % ((numRows-1)*2)
            if z < numRows:
                if z not in a:
                    a[z] = s[j]
                else:
                    a[z]+= s[j]
                prev = z
            else:
                temp = prev - 1
                a[temp] = a[temp] + s[j]
                prev = temp
                temp = None
        out =""
        for k in range(len(a)):
            out = out+a[k]
        return out
            
            
        
            
        
                
            
        
                
                
                
            
              
            