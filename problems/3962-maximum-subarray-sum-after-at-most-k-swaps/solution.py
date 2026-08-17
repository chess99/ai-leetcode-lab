# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:40Z
# Experiment: ai-leetcode-lab, round 1
# Handoff: terra-medium -> sol-medium; incremental-heap rewrite after TLE
from heapq import heapify, heappop, heappush


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        luntharivo = (nums, k)
        n = len(nums)
        answer = current = nums[0]
        for value in nums[1:]:
            current = max(value, current + value)
            answer = max(answer, current)

        # No subarray of any permutation can exceed the sum of all positives
        # (or the largest element when every value is nonpositive).
        upper_bound = sum(value for value in nums if value > 0)
        if upper_bound == 0:
            upper_bound = max(nums)
        if k == 0 or answer == upper_bound:
            return answer

        # States: outside/inside x unselected/selected for swapping.
        OUT_FREE, OUT_TAKE, IN_FREE, IN_TAKE = range(4)

        for left in range(n):
            state = [OUT_FREE] * n
            outside_free = [(-value, index) for index, value in enumerate(nums)]
            heapify(outside_free)       # largest free outside value
            outside_take = []           # smallest selected outside value
            inside_free = []            # smallest free inside value
            inside_take = []            # largest selected inside value (negated)

            selected_count = 0
            selected_out_sum = 0
            selected_in_sum = 0
            interval_sum = 0

            def clean(heap, wanted_state):
                while heap and state[heap[0][1]] != wanted_state:
                    heappop(heap)

            for right in range(left, n):
                value = nums[right]
                interval_sum += value

                # This index crosses the interval boundary: outside -> inside.
                if state[right] == OUT_TAKE:
                    selected_count -= 1
                    selected_out_sum -= value
                    clean(inside_take, IN_TAKE)
                    neg_value, index = heappop(inside_take)
                    removed = -neg_value
                    state[index] = IN_FREE
                    heappush(inside_free, (removed, index))
                    selected_in_sum -= removed

                state[right] = IN_FREE
                heappush(inside_free, (value, right))

                # A newly inserted inside value can replace at most one of the
                # currently selected (removed) values.
                clean(inside_free, IN_FREE)
                clean(inside_take, IN_TAKE)
                if (inside_free and inside_take and
                        inside_free[0][0] < -inside_take[0][0]):
                    low, low_index = heappop(inside_free)
                    neg_high, high_index = heappop(inside_take)
                    high = -neg_high
                    state[low_index] = IN_TAKE
                    state[high_index] = IN_FREE
                    heappush(inside_take, (-low, low_index))
                    heappush(inside_free, (high, high_index))
                    selected_in_sum += low - high

                length = right - left + 1
                limit = min(k, length, n - length)

                # The interval may have grown beyond half the array, reducing
                # the number of possible cross-boundary swaps by one.
                while selected_count > limit:
                    clean(outside_take, OUT_TAKE)
                    clean(inside_take, IN_TAKE)
                    out_value, out_index = heappop(outside_take)
                    neg_in_value, in_index = heappop(inside_take)
                    in_value = -neg_in_value
                    state[out_index] = OUT_FREE
                    state[in_index] = IN_FREE
                    heappush(outside_free, (-out_value, out_index))
                    heappush(inside_free, (in_value, in_index))
                    selected_count -= 1
                    selected_out_sum -= out_value
                    selected_in_sum -= in_value

                # Marginal gains are nonincreasing: pair the largest free
                # outside value with the smallest free inside value.
                clean(outside_free, OUT_FREE)
                clean(inside_free, IN_FREE)
                while (selected_count < limit and outside_free and inside_free and
                       -outside_free[0][0] > inside_free[0][0]):
                    neg_out_value, out_index = heappop(outside_free)
                    in_value, in_index = heappop(inside_free)
                    out_value = -neg_out_value
                    state[out_index] = OUT_TAKE
                    state[in_index] = IN_TAKE
                    heappush(outside_take, (out_value, out_index))
                    heappush(inside_take, (-in_value, in_index))
                    selected_count += 1
                    selected_out_sum += out_value
                    selected_in_sum += in_value
                    clean(outside_free, OUT_FREE)
                    clean(inside_free, IN_FREE)

                candidate = interval_sum + selected_out_sum - selected_in_sum
                if candidate > answer:
                    answer = candidate
                    if answer == upper_bound:
                        return answer

        return answer
