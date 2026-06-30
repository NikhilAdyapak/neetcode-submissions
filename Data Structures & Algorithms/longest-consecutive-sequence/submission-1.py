class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        longest_streak = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                current_streak = 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak