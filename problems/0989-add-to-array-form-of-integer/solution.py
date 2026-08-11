# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:19:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
                num[i] = k % 10
                i -= 1
            else:
                num.insert(0, k % 10)
            k //= 10
        return num
