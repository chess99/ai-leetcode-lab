# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n + 1)
        for number in range(1, n + 1):
            answer[number] = answer[number >> 1] + (number & 1)
        return answer
