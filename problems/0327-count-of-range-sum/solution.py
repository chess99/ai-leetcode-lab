# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        def sort_count(left, right):
            if right - left <= 1:
                return 0
            middle = (left + right) // 2
            count = sort_count(left, middle) + sort_count(middle, right)
            low = high = middle
            for start in prefix[left:middle]:
                while low < right and prefix[low] - start < lower:
                    low += 1
                while high < right and prefix[high] - start <= upper:
                    high += 1
                count += high - low
            merged = []
            first, second = left, middle
            while first < middle and second < right:
                if prefix[first] <= prefix[second]:
                    merged.append(prefix[first])
                    first += 1
                else:
                    merged.append(prefix[second])
                    second += 1
            merged.extend(prefix[first:middle])
            merged.extend(prefix[second:right])
            prefix[left:right] = merged
            return count

        return sort_count(0, len(prefix))
