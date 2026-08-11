# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:38:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = {}
        result = 0
        for a, b in dominoes:
            key = (a, b) if a <= b else (b, a)
            result += counts.get(key, 0)
            counts[key] = counts.get(key, 0) + 1
        return result
