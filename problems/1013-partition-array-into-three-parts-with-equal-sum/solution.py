# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:16:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3: return False
        target=sum(arr)//3; total=parts=0
        for value in arr:
            total+=value
            if total==target: parts+=1; total=0
        return parts>=3
