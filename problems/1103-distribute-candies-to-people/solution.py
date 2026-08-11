# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:28:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give = 1
        i = 0
        while candies:
            amount = min(candies, give)
            result[i % num_people] += amount
            candies -= amount; give += 1; i += 1
        return result
