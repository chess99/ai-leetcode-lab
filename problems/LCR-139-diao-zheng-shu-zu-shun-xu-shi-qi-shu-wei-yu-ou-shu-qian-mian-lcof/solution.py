# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:42:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        return [value for value in actions if value % 2] + [value for value in actions if value % 2 == 0]
