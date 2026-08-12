# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        size = len(s)
        tree = [None] * (4 * size)
        characters = list(s)

        def merge(left, right):
            left_char, right_char = left[0], right[1]
            length = left[5] + right[5]
            prefix = left[2]
            suffix = right[3]
            best = max(left[4], right[4])
            if left[1] == right[0]:
                joined = left[3] + right[2]
                best = max(best, joined)
                if left[2] == left[5]:
                    prefix = left[5] + right[2]
                if right[3] == right[5]:
                    suffix = right[5] + left[3]
            return (left_char, right_char, prefix, suffix, best, length)

        def build(node, left, right):
            if left == right:
                character = characters[left]
                tree[node] = (character, character, 1, 1, 1, 1)
                return
            middle = (left + right) // 2
            build(node * 2, left, middle)
            build(node * 2 + 1, middle + 1, right)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, left, right, index, character):
            if left == right:
                tree[node] = (character, character, 1, 1, 1, 1)
                return
            middle = (left + right) // 2
            if index <= middle:
                update(node * 2, left, middle, index, character)
            else:
                update(node * 2 + 1, middle + 1, right, index, character)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, size - 1)
        answer = []
        for index, character in zip(queryIndices, queryCharacters):
            characters[index] = character
            update(1, 0, size - 1, index, character)
            answer.append(tree[1][4])
        return answer
