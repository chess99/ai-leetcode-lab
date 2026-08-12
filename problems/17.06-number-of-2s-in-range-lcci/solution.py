# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        answer = 0
        factor = 1
        while factor <= n:
            lower = n % factor
            current = n // factor % 10
            higher = n // (factor * 10)
            answer += higher * factor
            if current == 2:
                answer += lower + 1
            elif current > 2:
                answer += factor
            factor *= 10
        return answer
