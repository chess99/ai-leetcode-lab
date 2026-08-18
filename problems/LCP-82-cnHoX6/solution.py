# AI solution attribution
# Initially created by: Codex Desktop / gpt-5.6-terra / medium / terra-medium
# Previous candidate by: Codex Desktop / gpt-5.6-sol / high / sol-high
# Upgraded by: Codex Desktop / gpt-5.6-sol / xhigh / sol-xhigh
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial
from typing import List


class Solution:
    def treeOfInfiniteSouls(self, gem: List[int], p: int, target: int) -> int:
        n = len(gem)
        catalan = factorial(2 * n - 2) // (factorial(n - 1) * factorial(n))
        total_trees = catalan * factorial(n)

        # Every serialization ends in 9.  These moduli therefore do not need
        # any enumeration (p == 1 is kept although 1 is not prime).
        if p in (1, 2, 5):
            return total_trees if target == 9 % p else 0

        digit_lengths = [len(str(value)) for value in gem]
        values = [value % p for value in gem]
        full_length = sum(digit_lengths) + 4 * n - 2
        pow10 = [1] * (full_length + 1)
        for length in range(1, full_length + 1):
            pow10[length] = pow10[length - 1] * 10 % p

        inv10 = pow(10, p - 2, p)
        invpow10 = [1] * (full_length + 1)
        for length in range(1, full_length + 1):
            invpow10[length] = invpow10[length - 1] * inv10 % p

        all_mask = (1 << n) - 1
        bit_count = [mask.bit_count() for mask in range(1 << n)]
        digit_sum_by_mask = [0] * (1 << n)
        length_by_mask = [0] * (1 << n)
        for mask in range(1, 1 << n):
            low_bit = mask & -mask
            index = low_bit.bit_length() - 1
            digit_sum_by_mask[mask] = (digit_sum_by_mask[mask ^ low_bit]
                                       + digit_lengths[index])
            length_by_mask[mask] = (digit_sum_by_mask[mask]
                                    + 4 * bit_count[mask] - 2)

        def masks_of_size(size):
            for chosen in combinations(range(n), size):
                mask = 0
                for index in chosen:
                    mask |= 1 << index
                yield mask

        # Count every labelled ordered subtree by its serialization remainder.
        # Sizes at most five are shared by all size-six constructions.
        tree_counts = {}
        for index in range(n):
            remainder = ((pow10[digit_lengths[index]] + values[index])
                         * 10 + 9) % p
            tree_counts[1 << index] = Counter((remainder,))

        def build_tree_counts(mask):
            result = Counter()
            left_mask = (mask - 1) & mask
            while left_mask:
                right_mask = mask ^ left_mask
                left_counts = tree_counts[left_mask]
                right_counts = tree_counts[right_mask]
                right_length = length_by_mask[right_mask]
                left_coefficient = pow10[right_length + 1]
                constant = (pow10[length_by_mask[left_mask]
                                  + right_length + 1] + 9) % p
                for left_remainder, left_amount in left_counts.items():
                    base = (constant
                            + left_remainder * left_coefficient) % p
                    for right_remainder, right_amount in right_counts.items():
                        remainder = (base + right_remainder * 10) % p
                        result[remainder] += left_amount * right_amount
                left_mask = (left_mask - 1) & mask
            return result

        for size in range(2, min(5, n) + 1):
            for mask in masks_of_size(size):
                tree_counts[mask] = build_tree_counts(mask)

        if n <= 5:
            return tree_counts[all_mask].get(target, 0)
        if n == 6:
            return build_tree_counts(all_mask).get(target, 0)

        # None is an ordinary leaf.  An internal shape is a (left, right) pair.
        @lru_cache(None)
        def shapes(leaves):
            if leaves == 1:
                return (None,)
            result = []
            for left_size in range(1, leaves):
                for left in shapes(left_size):
                    for right in shapes(leaves - left_size):
                        result.append((left, right))
            return tuple(result)

        # Test whether collapsing the canonical balanced subtree to leaf
        # position `hole` gives this context.  Real leaves weigh one and the
        # hole weighs `subtree_size`.
        def is_canonical_context(shape, hole, subtree_size):
            leaf_index = 0

            def annotate(node):
                nonlocal leaf_index
                if node is None:
                    is_hole = leaf_index == hole
                    leaf_index += 1
                    return ([subtree_size if is_hole else 1,
                             is_hole, None, None])
                left = annotate(node[0])
                right = annotate(node[1])
                return [left[0] + right[0], left[1] or right[1],
                        left, right]

            node = annotate(shape)
            while True:
                left, right = node[2], node[3]
                if left[0] > 6:
                    node = left
                elif right[0] > 6:
                    node = right
                else:
                    chosen = left if left[0] >= right[0] else right
                    return chosen[1] and chosen[2] is None

        # Compile the structural strings before and after a hole.  G marks an
        # ordinary leaf value and H marks the whole missing subtree.
        def context_parts(shape, hole):
            tokens = []
            leaf_index = 0

            def visit(node):
                nonlocal leaf_index
                if node is None:
                    if leaf_index == hole:
                        tokens.append("H")
                    else:
                        tokens.extend(("1", "G", "9"))
                    leaf_index += 1
                    return
                tokens.append("1")
                visit(node[0])
                visit(node[1])
                tokens.append("9")

            visit(shape)
            hole_at = tokens.index("H")

            def chunks(side):
                result = [""]
                for token in side:
                    if token == "G":
                        result.append("")
                    else:
                        result[-1] += token
                return tuple((int(chunk) % p if chunk else 0, len(chunk))
                             for chunk in result)

            return chunks(tokens[:hole_at]), chunks(tokens[hole_at + 1:])

        contexts = {}
        for subtree_size in range(4, min(6, n - 1) + 1):
            ordinary_leaves = n - subtree_size
            compiled = []
            for shape in shapes(ordinary_leaves + 1):
                for hole in range(ordinary_leaves + 1):
                    if is_canonical_context(shape, hole, subtree_size):
                        before, after = context_parts(shape, hole)
                        compiled.append((before, after, hole))
            contexts[subtree_size] = compiled

        def side_remainder(chunks, order):
            remainder = chunks[0][0]
            for position, index in enumerate(order):
                remainder = (remainder * pow10[digit_lengths[index]]
                             + values[index]) % p
                chunk_value, chunk_length = chunks[position + 1]
                remainder = (remainder * pow10[chunk_length]
                             + chunk_value) % p
            return remainder

        answer = 0
        for subtree_size, compiled_contexts in contexts.items():
            for subtree_mask in masks_of_size(subtree_size):
                if subtree_size == 6:
                    # All proper submasks have size at most five and are cached.
                    subtree_counts = build_tree_counts(subtree_mask)
                else:
                    subtree_counts = tree_counts[subtree_mask]

                outside = tuple(index for index in range(n)
                                if not (subtree_mask >> index) & 1)
                subtree_length = length_by_mask[subtree_mask]

                for before, after, hole in compiled_contexts:
                    after_structural_length = sum(length for _, length in after)
                    for order in permutations(outside):
                        before_remainder = side_remainder(before, order[:hole])
                        after_order = order[hole:]
                        after_remainder = side_remainder(after, after_order)
                        after_length = (after_structural_length
                                        + sum(digit_lengths[index]
                                              for index in after_order))
                        constant = (before_remainder
                                    * pow10[subtree_length + after_length]
                                    + after_remainder) % p
                        needed = ((target - constant)
                                  * invpow10[after_length]) % p
                        answer += subtree_counts.get(needed, 0)

        return answer
