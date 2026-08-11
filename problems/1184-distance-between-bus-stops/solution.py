# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination: start,destination=destination,start
        direct=sum(distance[start:destination])
        return min(direct,sum(distance)-direct)
