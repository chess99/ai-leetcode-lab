# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:49Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        parent = {}

        def add(name: str) -> None:
            if name not in parent:
                parent[name] = name

        def find(name: str) -> str:
            root = name
            while parent[root] != root:
                root = parent[root]
            while parent[name] != name:
                following = parent[name]
                parent[name] = root
                name = following
            return root

        def union(first: str, second: str) -> None:
            add(first)
            add(second)
            root_first, root_second = find(first), find(second)
            if root_first == root_second:
                return
            if root_first < root_second:
                parent[root_second] = root_first
            else:
                parent[root_first] = root_second

        counts = defaultdict(int)
        for item in names:
            opening = item.rfind('(')
            name = item[:opening]
            counts[name] += int(item[opening + 1:-1])
            add(name)
        for item in synonyms:
            first, second = item[1:-1].split(',')
            union(first, second)

        totals = defaultdict(int)
        for name, count in counts.items():
            totals[find(name)] += count
        return [f'{name}({count})' for name, count in totals.items()]
