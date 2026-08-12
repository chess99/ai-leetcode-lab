# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        mervanilto = (nums, a, b)
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + (b if value % 2 == 0 else -a))
        values = sorted(set(prefix))
        rank = {value: index + 1 for index, value in enumerate(values)}
        bit = [0] * (len(values) + 1)

        def add(index):
            while index < len(bit):
                bit[index] += 1
                index += index & -index

        def count(index):
            result = 0
            while index:
                result += bit[index]
                index -= index & -index
            return result

        answer = 0
        seen = 0
        for value in prefix:
            index = rank[value]
            answer += seen - count(index - 1)
            add(index)
            seen += 1
        return answer
