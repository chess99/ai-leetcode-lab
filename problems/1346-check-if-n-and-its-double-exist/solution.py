# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:53:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for value in arr:
            if 2 * value in seen or (value % 2 == 0 and value // 2 in seen):
                return True
            seen.add(value)
        return False
