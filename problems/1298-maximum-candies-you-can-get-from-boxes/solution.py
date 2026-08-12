# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:48Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        owned=set(initialBoxes);opened=set();queue=deque(box for box in owned if status[box]);answer=0
        while queue:
            box=queue.popleft()
            if box in opened:continue
            opened.add(box);answer+=candies[box]
            for key in keys[box]:
                status[key]=1
                if key in owned and key not in opened:queue.append(key)
            for following in containedBoxes[box]:
                owned.add(following)
                if status[following] and following not in opened:queue.append(following)
        return answer
