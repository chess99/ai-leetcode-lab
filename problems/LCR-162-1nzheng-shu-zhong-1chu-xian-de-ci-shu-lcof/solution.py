# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def digitOneInNumber(self, num: int) -> int:
        answer = 0
        factor = 1
        while factor <= num:
            lower = num % factor
            current = num // factor % 10
            higher = num // (factor * 10)
            if current == 0:
                answer += higher * factor
            elif current == 1:
                answer += higher * factor + lower + 1
            else:
                answer += (higher + 1) * factor
            factor *= 10
        return answer
