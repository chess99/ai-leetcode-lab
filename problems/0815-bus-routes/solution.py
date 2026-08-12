# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:52Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:return 0
        buses=defaultdict(list)
        for i,route in enumerate(routes):
            for stop in route:buses[stop].append(i)
        queue=deque([(source,0)]);seen_stops={source};seen_routes=set()
        while queue:
            stop,count=queue.popleft()
            for route_id in buses[stop]:
                if route_id in seen_routes:continue
                seen_routes.add(route_id)
                for following in routes[route_id]:
                    if following==target:return count+1
                    if following not in seen_stops:seen_stops.add(following);queue.append((following,count+1))
        return -1
