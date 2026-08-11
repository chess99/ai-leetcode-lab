# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:41:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        valid = [row for row in restaurants if (not veganFriendly or row[2]) and row[3] <= maxPrice and row[4] <= maxDistance]
        return [row[0] for row in sorted(valid, key=lambda row: (row[1], row[0]), reverse=True)]
