# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:23:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result=[first]
        for value in encoded: result.append(result[-1]^value)
        return result
