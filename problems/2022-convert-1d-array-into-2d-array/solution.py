# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:52:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [original[i*n:(i+1)*n] for i in range(m)] if len(original)==m*n else []
