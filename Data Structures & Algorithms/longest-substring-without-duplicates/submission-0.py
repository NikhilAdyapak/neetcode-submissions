class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lon = 0
        # for i in range(0,len(s)):
        #     substr = ''
        #     for j in range(i, len(s)):
        #         if s[j] not in substr:
        #             substr += s[j]
        #         else:
        #             if len(substr) > lon:
        #                 lon = len(substr)
        #             break
        # return len(substr)

        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r-l+1)
        return res

        