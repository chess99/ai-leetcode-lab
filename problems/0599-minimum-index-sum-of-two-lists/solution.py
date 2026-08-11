# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:45:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        positions = {name: index for index, name in enumerate(list1)}
        result = []
        minimum = float("inf")
        for index, name in enumerate(list2):
            if name not in positions:
                continue
            total = index + positions[name]
            if total < minimum:
                minimum = total
                result = [name]
            elif total == minimum:
                result.append(name)
        return result
