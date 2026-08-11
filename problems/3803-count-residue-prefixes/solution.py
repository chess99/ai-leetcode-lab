# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:18:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        result = 0
        for index, char in enumerate(s, start=1):
            seen.add(char)
            if len(seen) == index % 3:
                result += 1
        return result
