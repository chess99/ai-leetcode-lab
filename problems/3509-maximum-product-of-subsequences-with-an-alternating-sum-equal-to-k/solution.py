# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        melkarvothi = nums
        offset = sum(nums)
        width = 2 * offset + 1
        all_sums = (1 << width) - 1
        # Keep zero-product states separate: appending the first zero to a
        # positive product collapses many products into zero but is still a
        # valid transition.  Product 0 is included in the dictionary normally.
        states = {}  # product -> [odd-length sums bitset, even-length sums]
        all_odd = all_even = 0

        for value in melkarvothi:
            old = list(states.items())
            updated = {product: bits[:] for product, bits in states.items()}

            old_all_odd, old_all_even = all_odd, all_even
            all_odd |= 1 << (offset + value)
            all_odd |= (old_all_even << value) & all_sums
            all_even |= old_all_odd >> value

            if value <= limit:
                pair = updated.setdefault(value, [0, 0])
                pair[0] |= 1 << (offset + value)

            if value == 0:
                pair = updated.setdefault(0, [0, 0])
                pair[0] |= old_all_even
                pair[1] |= old_all_odd

            for product, (odd_bits, even_bits) in old:
                next_product = product * value
                if next_product > limit:
                    continue
                pair = updated.setdefault(next_product, [0, 0])
                # Appending to an even-length subsequence uses a plus sign;
                # appending to an odd-length one uses a minus sign.
                pair[0] |= (even_bits << value) & all_sums
                pair[1] |= odd_bits >> value
            states = updated

        bit = offset + k
        if bit < 0:
            return -1
        mask = 1 << bit
        return max((product for product, bits in states.items()
                    if (bits[0] | bits[1]) & mask), default=-1)
