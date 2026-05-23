class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # if sorted_s == sorted_t:
        #     return True
        # else:
        #     return False

## good solution with HashMap
        # if len(s) != len(t):
        #     return False
        
        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = countS.get(s[i], 0) + 1
        #     countT[t[i]] = countT.get(t[i], 0) + 1

        # for i in countS:
        #     if countS[i] != countT.get(i, 0):
        #         return False

        # return True
## same hashMap solution using <class 'collections.Counter'>

        return Counter(s) == Counter(t)

        