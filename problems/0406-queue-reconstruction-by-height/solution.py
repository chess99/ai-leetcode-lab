# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:53:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        for person in sorted(people, key=lambda item: (-item[0], item[1])):
            queue.insert(person[1], person)
        return queue
