# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        bralvoteni = (nums, k)
        values = sorted(set(nums))
        rank = {value: index + 1 for index, value in enumerate(values)}
        size = len(values)

        class Bit:
            def __init__(self) -> None:
                self.data = [0] * (size + 1)

            def update(self, index: int, value: int) -> None:
                while index <= size:
                    if value > self.data[index]:
                        self.data[index] = value
                    index += index & -index

            def query(self, index: int) -> int:
                result = 0
                while index:
                    if self.data[index] > result:
                        result = self.data[index]
                    index -= index & -index
                return result

        # A rising final step needs a previous falling state with smaller value;
        # a falling final step needs a previous rising state with larger value.
        down_low = Bit()
        up_high = Bit()
        up = [0] * len(nums)
        down = [0] * len(nums)
        answer = 0

        for i, value in enumerate(nums):
            if i >= k:
                old_rank = rank[nums[i - k]]
                down_low.update(old_rank, down[i - k])
                up_high.update(size - old_rank + 1, up[i - k])

            current_rank = rank[value]
            up[i] = value + down_low.query(current_rank - 1)
            down[i] = value + up_high.query(size - current_rank)
            answer = max(answer, up[i], down[i])

        return answer
