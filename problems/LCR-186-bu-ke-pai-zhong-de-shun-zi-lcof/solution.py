# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:52:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        places.sort()
        jokers = places.count(0)
        for index in range(jokers + 1, len(places)):
            if places[index] == places[index - 1]:
                return False
        return places[-1] - places[jokers] < 5 if jokers < 5 else True
