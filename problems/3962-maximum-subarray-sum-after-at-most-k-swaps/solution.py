# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        luntharivo = (nums, k)
        n = len(nums)
        values = sorted(set(nums))
        ranks = {value: index + 1 for index, value in enumerate(values)}
        size = len(values)

        def add(bit, index, delta):
            while index <= size:
                bit[index] += delta
                index += index & -index

        def kth(bit, order):
            index = 0
            step = 1 << (size.bit_length() - 1)
            while step:
                nxt = index + step
                if nxt <= size and bit[nxt] < order:
                    order -= bit[nxt]
                    index = nxt
                step >>= 1
            return index + 1

        def prefix(bit, index):
            result = 0
            while index:
                result += bit[index]
                index -= index & -index
            return result

        global_count = [0] * (size + 1)
        global_sum = [0] * (size + 1)
        for value in nums:
            rank = ranks[value]
            add(global_count, rank, 1)
            add(global_sum, rank, value)

        answer = max(nums)
        for left in range(n):
            in_count = [0] * (size + 1)
            in_sum = [0] * (size + 1)
            out_count = global_count[:]
            out_sum = global_sum[:]
            current_sum = 0
            swaps = 0
            for right in range(left, n):
                value = nums[right]
                rank = ranks[value]
                add(out_count, rank, -1)
                add(out_sum, rank, -value)
                current_sum += value
                add(in_count, rank, 1)
                add(in_sum, rank, value)

                maximum_swaps = min(k, right - left + 1, n - (right - left + 1))
                outside_total = n - (right - left + 1)
                while swaps > maximum_swaps or (swaps and
                        values[kth(in_count, swaps) - 1] >=
                        values[kth(out_count, outside_total - swaps + 1) - 1]):
                    swaps -= 1
                while swaps < maximum_swaps:
                    candidate = swaps + 1
                    if (values[kth(in_count, candidate) - 1] >=
                            values[kth(out_count, outside_total - candidate + 1) - 1]):
                        break
                    swaps = candidate
                if swaps:
                    small_rank = kth(in_count, swaps)
                    before_count = prefix(in_count, small_rank - 1)
                    small_sum = prefix(in_sum, small_rank - 1)
                    small_sum += (swaps - before_count) * values[small_rank - 1]

                    cutoff = outside_total - swaps
                    if cutoff:
                        cut_rank = kth(out_count, cutoff)
                        before_count = prefix(out_count, cut_rank - 1)
                        lower_sum = prefix(out_sum, cut_rank - 1)
                        lower_sum += (cutoff - before_count) * values[cut_rank - 1]
                    else:
                        lower_sum = 0
                    outside_sum = prefix(out_sum, size)
                    gain = outside_sum - lower_sum - small_sum
                else:
                    gain = 0
                answer = max(answer, current_sum + gain)
        return answer
