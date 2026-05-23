class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # s_seen = {}
        # t_seen = {}

        # for i in range(len(s)):
        #     if s[i] in s:
        #         s_seen.get(s[i], 0) + 1

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False