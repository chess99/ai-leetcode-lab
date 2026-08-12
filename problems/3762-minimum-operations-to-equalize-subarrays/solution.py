# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        dalmerinth = (nums, k, queries)
        values = sorted(set(nums))
        rank = {value: index for index, value in enumerate(values)}

        left_child = [0]
        right_child = [0]
        counts = [0]
        sums = [0]

        def clone(node: int) -> int:
            left_child.append(left_child[node])
            right_child.append(right_child[node])
            counts.append(counts[node])
            sums.append(sums[node])
            return len(counts) - 1

        def insert(old_root: int, position: int, value: int) -> int:
            new_root = clone(old_root)
            old_node, new_node = old_root, new_root
            low, high = 0, len(values) - 1
            while low < high:
                counts[new_node] += 1
                sums[new_node] += value
                middle = (low + high) // 2
                if position <= middle:
                    child = clone(left_child[old_node])
                    left_child[new_node] = child
                    old_node, new_node = left_child[old_node], child
                    high = middle
                else:
                    child = clone(right_child[old_node])
                    right_child[new_node] = child
                    old_node, new_node = right_child[old_node], child
                    low = middle + 1
            counts[new_node] += 1
            sums[new_node] += value
            return new_root

        roots = [0]
        for value in nums:
            roots.append(insert(roots[-1], rank[value], value))

        def kth_and_left_sum(left_root: int, right_root: int, order: int):
            low, high = 0, len(values) - 1
            passed_count = passed_sum = 0
            while low < high:
                middle = (low + high) // 2
                left_count = counts[left_child[right_root]] - counts[left_child[left_root]]
                if order <= left_count:
                    left_root = left_child[left_root]
                    right_root = left_child[right_root]
                    high = middle
                else:
                    passed_count += left_count
                    passed_sum += sums[left_child[right_root]] - sums[left_child[left_root]]
                    order -= left_count
                    left_root = right_child[left_root]
                    right_root = right_child[right_root]
                    low = middle + 1
            return values[low], passed_count, passed_sum

        size = 1
        while size < len(nums):
            size <<= 1
        min_rem = [10 ** 18] * (size * 2)
        max_rem = [-1] * (size * 2)
        for index, value in enumerate(nums):
            residue = value % k
            min_rem[size + index] = max_rem[size + index] = residue
        for node in range(size - 1, 0, -1):
            min_rem[node] = min(min_rem[node * 2], min_rem[node * 2 + 1])
            max_rem[node] = max(max_rem[node * 2], max_rem[node * 2 + 1])

        def residue_range(left: int, right: int):
            minimum, maximum = 10 ** 18, -1
            left += size
            right += size + 1
            while left < right:
                if left & 1:
                    minimum = min(minimum, min_rem[left])
                    maximum = max(maximum, max_rem[left])
                    left += 1
                if right & 1:
                    right -= 1
                    minimum = min(minimum, min_rem[right])
                    maximum = max(maximum, max_rem[right])
                left >>= 1
                right >>= 1
            return minimum, maximum

        answer = []
        prefix_sum = [0]
        for value in nums:
            prefix_sum.append(prefix_sum[-1] + value)
        for left, right in queries:
            minimum, maximum = residue_range(left, right)
            if minimum != maximum:
                answer.append(-1)
                continue
            length = right - left + 1
            median, smaller_count, smaller_sum = kth_and_left_sum(
                roots[left], roots[right + 1], (length + 1) // 2
            )
            total_sum = prefix_sum[right + 1] - prefix_sum[left]
            median_count = counts[roots[right + 1]] - counts[roots[left]]
            # kth 查询返回严格较小分支的汇总；相等元素对代价没有贡献。
            left_cost = median * smaller_count - smaller_sum
            right_cost = total_sum - smaller_sum - median * (length - smaller_count)
            answer.append((left_cost + right_cost) // k)
        return answer
