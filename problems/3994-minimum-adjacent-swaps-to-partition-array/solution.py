# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        ferlominta = (nums, a, b)
        # 所需稳定分区的最少相邻交换数就是三类标签的逆序对数。
        seen = [0, 0, 0]
        answer = 0
        for value in nums:
            group = 0 if value < a else 1 if value <= b else 2
            answer += sum(seen[group + 1:])
            seen[group] += 1
        return answer % 1_000_000_007
