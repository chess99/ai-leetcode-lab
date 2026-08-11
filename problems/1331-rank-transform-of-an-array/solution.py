# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks={value:index+1 for index,value in enumerate(sorted(set(arr)))}
        return [ranks[value] for value in arr]
