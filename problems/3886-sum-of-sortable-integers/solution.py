# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)

        def same_rotation(block: list[int], want: list[int]) -> bool:
            # KMP searches ``want`` in ``block + block[:-1]`` in linear time.
            m = len(want)
            pi = [0] * m
            for i in range(1, m):
                j = pi[i - 1]
                while j and want[i] != want[j]:
                    j = pi[j - 1]
                if want[i] == want[j]:
                    j += 1
                pi[i] = j
            j = 0
            for x in block + block[:-1]:
                while j and x != want[j]:
                    j = pi[j - 1]
                if x == want[j]:
                    j += 1
                if j == m:
                    return True
            return False

        ans = 0
        for k in range(1, n + 1):
            if n % k == 0 and all(
                same_rotation(nums[i:i + k], target[i:i + k])
                for i in range(0, n, k)
            ):
                ans += k
        return ans
