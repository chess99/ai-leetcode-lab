# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = answer = 0
        for right, (first, second) in enumerate(zip(s, t)):
            cost += abs(ord(first) - ord(second))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            answer = max(answer, right - left + 1)
        return answer
