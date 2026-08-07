class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
        return new == new[::-1]
        
        '''
        s = s.join(" "), s.lower()
        for i in s:
            for j in reversed(s):
                if i == j:
                    return True
                    break
        '''        
