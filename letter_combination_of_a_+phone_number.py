class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        output= []
        
        
        def backtrack(combinations, leftover):
            if len(leftover) == 0:
                output.append(combinations)
            else:
                for letter in phone[leftover[0]]:
                    backtrack(combinations+letter, leftover[1:])
        
        if len(digits)>0:
            backtrack("", digits)
        else:
            return []
                    
        return output
                