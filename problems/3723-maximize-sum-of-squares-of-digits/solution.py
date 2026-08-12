# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        drevantor = (num, sum)
        if sum > 9 * num: return ''
        nines, remainder = divmod(sum, 9)
        return '9' * nines + (str(remainder) if remainder else '') + '0' * (num - nines - bool(remainder))
