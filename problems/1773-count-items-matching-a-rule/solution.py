# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:35:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = {'type': 0, 'color': 1, 'name': 2}[ruleKey]
        return sum(item[index] == ruleValue for item in items)
