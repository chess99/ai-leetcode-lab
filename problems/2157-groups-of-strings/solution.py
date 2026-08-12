# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:11Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class DisjointSet:
    def __init__(self, sizes):
        self.parent = list(range(len(sizes)))
        self.size = list(sizes)

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, first, second):
        first = self.find(first)
        second = self.find(second)
        if first == second:
            return
        if self.size[first] < self.size[second]:
            first, second = second, first
        self.parent[second] = first
        self.size[first] += self.size[second]


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        frequencies = Counter()
        for word in words:
            mask = 0
            for character in word:
                mask |= 1 << (ord(character) - 97)
            frequencies[mask] += 1

        masks = list(frequencies)
        indices = {mask: index for index, mask in enumerate(masks)}
        groups = DisjointSet([frequencies[mask] for mask in masks])
        deleted_owner = {}

        for index, mask in enumerate(masks):
            for bit in range(26):
                neighbor = mask ^ (1 << bit)
                if neighbor in indices:
                    groups.union(index, indices[neighbor])

            bits = mask
            while bits:
                lowest = bits & -bits
                deleted = mask ^ lowest
                if deleted in deleted_owner:
                    groups.union(index, deleted_owner[deleted])
                else:
                    deleted_owner[deleted] = index
                bits -= lowest

        roots = {groups.find(index) for index in range(len(masks))}
        return [len(roots), max(groups.size[root] for root in roots)]
