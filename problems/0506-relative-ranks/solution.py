# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:41:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [""] * len(score)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for rank, index in enumerate(sorted(range(len(score)), key=lambda i: -score[i])):
            result[index] = medals[rank] if rank < 3 else str(rank + 1)
        return result
