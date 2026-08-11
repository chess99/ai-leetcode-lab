# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:40Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))
        def find(index):
            while parent[index] != index:
                parent[index] = parent[parent[index]]
                index = parent[index]
            return index
        for first, second in pairs:
            first, second = find(first), find(second)
            if first != second: parent[first] = second
        groups = defaultdict(list)
        for index in range(len(s)): groups[find(index)].append(index)
        answer = list(s)
        for indices in groups.values():
            for index, char in zip(sorted(indices), sorted(s[i] for i in indices)):
                answer[index] = char
        return ''.join(answer)
