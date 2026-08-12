# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        nums.sort()
        # Binary trie stored as child dictionaries keeps the active window deletable.
        children = [[-1, -1]]
        frequencies = [0]

        def insert(value, delta):
            node = 0
            frequencies[node] += delta
            for bit in range(20, -1, -1):
                direction = value >> bit & 1
                if children[node][direction] == -1:
                    children[node][direction] = len(children)
                    children.append([-1, -1])
                    frequencies.append(0)
                node = children[node][direction]
                frequencies[node] += delta

        def best_xor(value):
            node = 0
            result = 0
            for bit in range(20, -1, -1):
                direction = value >> bit & 1
                preferred = children[node][direction ^ 1]
                if preferred != -1 and frequencies[preferred]:
                    result |= 1 << bit
                    node = preferred
                else:
                    node = children[node][direction]
            return result

        left = 0
        answer = 0
        for value in nums:
            insert(value, 1)
            while nums[left] * 2 < value:
                insert(nums[left], -1)
                left += 1
            answer = max(answer, best_xor(value))
        return answer
