# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def dismantlingAction(self, arr: str) -> int:
        last_seen = {}
        left = answer = 0
        for right, char in enumerate(arr):
            if char in last_seen:
                left = max(left, last_seen[char] + 1)
            last_seen[char] = right
            answer = max(answer, right - left + 1)
        return answer
