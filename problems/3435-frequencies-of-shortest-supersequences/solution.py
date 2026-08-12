# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        letters = sorted(set(''.join(words)))
        index = {char: i for i, char in enumerate(letters)}
        size = len(letters)
        edges = [[] for _ in range(size)]
        forced = 0
        for word in words:
            first, second = map(index.get, word)
            if first == second:
                forced |= 1 << first
            else:
                edges[first].append(second)

        def acyclic(repeated: int) -> bool:
            state = [0] * size

            def visit(node: int) -> bool:
                state[node] = 1
                for neighbor in edges[node]:
                    if repeated >> neighbor & 1:
                        continue
                    if state[neighbor] == 1 or (state[neighbor] == 0 and not visit(neighbor)):
                        return False
                state[node] = 2
                return True

            return all(
                repeated >> node & 1 or state[node] or visit(node)
                for node in range(size)
            )

        best = size + 1
        masks = []
        for mask in range(1 << size):
            if mask & forced != forced:
                continue
            count = mask.bit_count()
            if count <= best and acyclic(mask):
                if count < best:
                    best = count
                    masks.clear()
                masks.append(mask)

        answer = []
        for mask in masks:
            frequencies = [0] * 26
            for char, bit in index.items():
                frequencies[ord(char) - 97] = 1 + (mask >> bit & 1)
            answer.append(frequencies)
        return answer
