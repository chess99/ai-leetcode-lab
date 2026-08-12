# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:31Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod=1_000_000_007
        @lru_cache(None)
        def count(city,left):
            answer=int(city==finish)
            for following in range(len(locations)):
                cost=abs(locations[city]-locations[following])
                if following!=city and cost<=left:answer+=count(following,left-cost)
            return answer%mod
        return count(start,fuel)
