# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s); cuts = list(range(-1, n))
        for center in range(n):
            for left, right in ((center, center), (center - 1, center)):
                while left >= 0 and right < n and s[left] == s[right]:
                    cuts[right + 1] = min(cuts[right + 1], cuts[left] + 1)
                    left -= 1; right += 1
        return cuts[n]
