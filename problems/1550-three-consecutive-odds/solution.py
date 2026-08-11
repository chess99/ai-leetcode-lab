# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:41:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive = 0
        for number in arr:
            consecutive = consecutive + 1 if number % 2 else 0
            if consecutive == 3:
                return True
        return False
