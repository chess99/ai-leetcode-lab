# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        size = len(parent)
        children = [[] for _ in parent]
        for node in range(1, size):
            children[parent[node]].append(node)

        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            stack.extend(children[node])
        postorder = order[::-1]
        position = [0] * size
        subtree_size = [1] * size
        text = []
        for index, node in enumerate(postorder):
            position[node] = index
            text.append(s[node])
            if parent[node] != -1:
                subtree_size[parent[node]] += subtree_size[node]
        text = ''.join(text)

        odd = [0] * size
        left = 0;right = -1
        for index in range(size):
            radius = 1 if index > right else min(odd[left + right - index], right - index + 1)
            while index - radius >= 0 and index + radius < size and text[index-radius] == text[index+radius]:
                radius += 1
            odd[index] = radius
            if index + radius - 1 > right:
                left, right = index - radius + 1, index + radius - 1

        even = [0] * size
        left = 0;right = -1
        for index in range(size):
            radius = 0 if index > right else min(even[left + right - index + 1], right - index + 1)
            while index - radius - 1 >= 0 and index + radius < size and text[index-radius-1] == text[index+radius]:
                radius += 1
            even[index] = radius
            if index + radius - 1 > right:
                left, right = index - radius, index + radius - 1

        answer = []
        for node in range(size):
            length = subtree_size[node]
            end = position[node]
            start = end - length + 1
            if length & 1:
                middle = (start + end) // 2
                answer.append(odd[middle] >= length // 2 + 1)
            else:
                middle = start + length // 2
                answer.append(even[middle] >= length // 2)
        return answer
