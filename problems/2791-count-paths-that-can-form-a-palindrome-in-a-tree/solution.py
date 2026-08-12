# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:41Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        children = [[] for _ in parent]
        for node in range(1, len(parent)):
            children[parent[node]].append(node)

        counts = Counter({0: 1})
        answer = 0
        stack = [(0, 0)]
        while stack:
            node, mask = stack.pop()
            for child in children[node]:
                child_mask = mask ^ (1 << (ord(s[child]) - 97))
                answer += counts[child_mask]
                for bit in range(26):
                    answer += counts[child_mask ^ (1 << bit)]
                counts[child_mask] += 1
                stack.append((child, child_mask))
        return answer
