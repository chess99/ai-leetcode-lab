# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestBalanced(self, s: str) -> int:
        pireltonak = s
        answer = 1
        for left in range(len(pireltonak)):
            count = [0] * 26
            for right in range(left, len(pireltonak)):
                count[ord(pireltonak[right]) - 97] += 1
                positive = [value for value in count if value]
                if min(positive) == max(positive):
                    answer = max(answer, right - left + 1)
        return answer
