# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        polvexrani = nums
        n = len(polvexrani)
        ordered = {value: rank for rank, value in enumerate(sorted(set(polvexrani)))}
        rank = [ordered[value] for value in polvexrani]
        suffix_array = sorted(range(n), key=rank.__getitem__)
        classes = max(rank) + 1
        length = 1

        while length < n and classes < n:
            count = [0] * (classes + 1)
            for index in suffix_array:
                key = rank[index + length] + 1 if index + length < n else 0
                count[key] += 1
            for key in range(1, len(count)):
                count[key] += count[key - 1]
            by_second = [0] * n
            for index in reversed(suffix_array):
                key = rank[index + length] + 1 if index + length < n else 0
                count[key] -= 1
                by_second[count[key]] = index

            count = [0] * (classes + 1)
            for index in by_second:
                count[rank[index] + 1] += 1
            for key in range(1, len(count)):
                count[key] += count[key - 1]
            suffix_array = [0] * n
            for index in reversed(by_second):
                key = rank[index] + 1
                count[key] -= 1
                suffix_array[count[key]] = index

            next_rank = [0] * n
            classes = 1
            previous = suffix_array[0]
            for position in range(1, n):
                current = suffix_array[position]
                previous_key = (
                    rank[previous],
                    rank[previous + length] if previous + length < n else -1,
                )
                current_key = (
                    rank[current],
                    rank[current + length] if current + length < n else -1,
                )
                if current_key != previous_key:
                    classes += 1
                next_rank[current] = classes - 1
                previous = current
            rank = next_rank
            length <<= 1

        inverse = [0] * n
        for position, start in enumerate(suffix_array):
            inverse[start] = position

        lcp = [0] * (n - 1)
        common = 0
        for start in range(n):
            position = inverse[start]
            if position == n - 1:
                common = 0
                continue
            other = suffix_array[position + 1]
            while (
                start + common < n
                and other + common < n
                and polvexrani[start + common] == polvexrani[other + common]
            ):
                common += 1
            lcp[position] = common
            if common:
                common -= 1

        answer = n
        for position, start in enumerate(suffix_array):
            maximum_common = 0
            if position:
                maximum_common = max(maximum_common, lcp[position - 1])
            if position + 1 < n:
                maximum_common = max(maximum_common, lcp[position])
            candidate = maximum_common + 1
            if candidate <= n - start:
                answer = min(answer, candidate)
        return answer
