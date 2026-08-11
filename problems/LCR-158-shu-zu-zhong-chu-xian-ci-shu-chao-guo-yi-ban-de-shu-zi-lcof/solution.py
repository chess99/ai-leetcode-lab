# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:43:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        candidate = None
        count = 0
        for value in stock:
            if count == 0:
                candidate = value
            count += 1 if value == candidate else -1
        return candidate
