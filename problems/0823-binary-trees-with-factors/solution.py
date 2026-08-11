# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        modulo = 1_000_000_007
        arr.sort()
        index = {value: i for i, value in enumerate(arr)}
        trees = [1] * len(arr)
        for i, value in enumerate(arr):
            for j in range(i):
                if value % arr[j] == 0 and value // arr[j] in index:
                    trees[i] = (trees[i] + trees[j] * trees[index[value // arr[j]]]) % modulo
        return sum(trees) % modulo
