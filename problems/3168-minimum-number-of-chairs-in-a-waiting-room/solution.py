# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumChairs(self, s: str) -> int:
        occupied = 0
        answer = 0
        for event in s:
            if event == "E":
                occupied += 1
                answer = max(answer, occupied)
            else:
                occupied -= 1
        return answer
