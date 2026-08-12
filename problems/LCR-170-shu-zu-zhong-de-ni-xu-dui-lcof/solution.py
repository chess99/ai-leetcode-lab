# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def reversePairs(self, record: List[int]) -> int:
        buffer = [0] * len(record)

        def sort_count(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            middle = (left + right) // 2
            answer = sort_count(left, middle) + sort_count(middle, right)
            first, second, write = left, middle, left
            while first < middle and second < right:
                if record[first] <= record[second]:
                    buffer[write] = record[first]
                    first += 1
                else:
                    buffer[write] = record[second]
                    second += 1
                    answer += middle - first
                write += 1
            while first < middle:
                buffer[write] = record[first]
                first += 1
                write += 1
            while second < right:
                buffer[write] = record[second]
                second += 1
                write += 1
            record[left:right] = buffer[left:right]
            return answer

        return sort_count(0, len(record))
