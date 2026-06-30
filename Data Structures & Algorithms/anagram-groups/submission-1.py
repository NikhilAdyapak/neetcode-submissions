from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for i, s in enumerate(strs):
        #     strs[i] = Counter(s)

        def count_gen(s):
            arr = [0] * 26
            for i, char in enumerate(s):
                arr[ord(char) - ord('a')] += 1
            return tuple(arr)

        seen = {}
        # seen = defaultdict(list)
        # print(seen, type(seen))
        for s in strs:
            dict_key = count_gen(s)
            if dict_key in seen:
                seen[dict_key].append(s)
            else:
                seen[dict_key] = [s]
        return list(seen.values())