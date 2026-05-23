class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s_arr = []

        for i in s:
            if (i >= 'A' and i <= 'Z') or \
             (i >= 'a' and i <= 'z') or \
              (i >= '0' and i <= '9'):

                s_arr.append(i)

        i = 0
        j = len(s_arr) - 1

        while i < j:
            if s_arr[i] != s_arr[j]:
                return False
            i += 1
            j -= 1
        
        return True