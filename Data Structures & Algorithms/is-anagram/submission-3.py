from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        print(Counter(s))
        return Counter(s) == Counter(t)
        