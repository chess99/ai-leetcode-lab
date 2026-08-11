# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:25:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(len(text := str(value)) % 2 == 0 and sum(map(int, text[:len(text)//2])) == sum(map(int, text[len(text)//2:])) for value in range(low, high+1))
