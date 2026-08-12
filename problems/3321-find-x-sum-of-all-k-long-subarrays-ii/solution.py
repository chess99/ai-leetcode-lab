# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:35Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        frequency = {}
        selected = {}
        lower = []
        upper = []
        selected_count = 0
        selected_sum = 0

        def clean_lower():
            while lower:
                count, value = lower[0]
                if (selected.get(value, False)
                        and frequency.get(value, 0) == count):
                    break
                heapq.heappop(lower)

        def clean_upper():
            while upper:
                negative_count, negative_value = upper[0]
                value = -negative_value
                if (not selected.get(value, False)
                        and frequency.get(value, 0) == -negative_count
                        and frequency.get(value, 0) > 0):
                    break
                heapq.heappop(upper)

        def move_to_selected(value):
            nonlocal selected_count, selected_sum
            selected[value] = True
            selected_count += 1
            selected_sum += frequency[value] * value
            heapq.heappush(lower, (frequency[value], value))

        def move_to_upper(value):
            nonlocal selected_count, selected_sum
            selected[value] = False
            selected_count -= 1
            selected_sum -= frequency[value] * value
            heapq.heappush(upper, (-frequency[value], -value))

        def rebalance():
            clean_lower();clean_upper()
            while selected_count > x:
                _, value = heapq.heappop(lower)
                move_to_upper(value)
                clean_lower()
            while selected_count < x and upper:
                clean_upper()
                if not upper:
                    break
                _, negative_value = heapq.heappop(upper)
                move_to_selected(-negative_value)
                clean_upper()
            clean_lower();clean_upper()
            while lower and upper and lower[0] < (-upper[0][0], -upper[0][1]):
                _, low_value = heapq.heappop(lower)
                _, negative_high_value = heapq.heappop(upper)
                high_value = -negative_high_value
                move_to_upper(low_value)
                move_to_selected(high_value)
                clean_lower();clean_upper()

        def change(value, difference):
            nonlocal selected_count, selected_sum
            old = frequency.get(value, 0)
            if old:
                if selected.get(value, False):
                    selected_count -= 1
                    selected_sum -= old * value
                selected.pop(value, None)
            frequency[value] = old + difference
            if frequency[value] > 0:
                clean_lower()
                key = (frequency[value], value)
                if selected_count < x or (lower and key > lower[0]):
                    selected[value] = True
                    selected_count += 1
                    selected_sum += frequency[value] * value
                    heapq.heappush(lower, key)
                else:
                    selected[value] = False
                    heapq.heappush(upper, (-key[0], -key[1]))
            rebalance()

        for value in nums[:k]:
            change(value, 1)
        answer = [selected_sum]
        for right in range(k, len(nums)):
            change(nums[right - k], -1)
            change(nums[right], 1)
            answer.append(selected_sum)
        return answer
