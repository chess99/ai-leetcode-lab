# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:53:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [index for index, _ in sorted(enumerate(mat), key=lambda item: (sum(item[1]), item[0]))[:k]]
