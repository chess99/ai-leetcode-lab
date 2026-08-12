# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        trevolimna = (nums, queries)
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        # (count, first, last, sum((p_i-p_{i-1})*p_i))
        tree = [(0, -1, -1, 0) for _ in range(size * 2)]

        def merge(left, right):
            if left[0] == 0:
                return right
            if right[0] == 0:
                return left
            return (left[0] + right[0], left[1], right[2],
                    left[3] + right[3] + (right[1] - left[2]) * right[1])

        def is_peak(index):
            return (0 < index < n - 1 and nums[index] > nums[index - 1]
                    and nums[index] > nums[index + 1])

        def update(index):
            node = size + index
            tree[node] = (1, index, index, 0) if is_peak(index) else (0, -1, -1, 0)
            node >>= 1
            while node:
                tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
                node >>= 1

        def query(left, right):
            if left > right:
                return (0, -1, -1, 0)
            left += size
            right += size + 1
            before = after = (0, -1, -1, 0)
            while left < right:
                if left & 1:
                    before = merge(before, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    after = merge(tree[right], after)
                left >>= 1
                right >>= 1
            return merge(before, after)

        for index in range(1, n - 1):
            if is_peak(index):
                tree[size + index] = (1, index, index, 0)
        for node in range(size - 1, 0, -1):
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        answer = []
        for query_data in queries:
            if query_data[0] == 2:
                _, index, value = query_data
                nums[index] = value
                for changed in range(max(1, index - 1), min(n - 1, index + 2)):
                    update(changed)
            else:
                _, left, right = query_data
                summary = query(left + 1, right - 1)
                if summary[0] == 0:
                    answer.append(0)
                else:
                    _, first, last, internal_cost = summary
                    answer.append(right * (last - left) -
                                  ((first - left) * first + internal_cost))
        return answer
