# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        ravolqedin = nums1
        odds = [value for value in nums1 if value & 1]
        evens = [value for value in nums1 if value % 2 == 0]
        if not odds or not evens:
            return True
        # 最小奇数无法通过减去正数改成偶数，目标只能全为奇数。
        # 每个偶数均须减去一个更小的奇数，最小奇数足够作为共同减数。
        return min(evens) > min(odds)
