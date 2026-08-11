# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:31:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        result = -1
        for mask in range(1 << len(cookbooks)):
            used = [0] * 5
            delicious = fullness = 0
            for index in range(len(cookbooks)):
                if mask >> index & 1:
                    used = [a + b for a, b in zip(used, cookbooks[index])]
                    delicious += attribute[index][0]
                    fullness += attribute[index][1]
            if fullness >= limit and all(a <= b for a, b in zip(used, materials)):
                result = max(result, delicious)
        return result
