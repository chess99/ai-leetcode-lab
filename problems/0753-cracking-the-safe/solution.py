# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start = '0' * (n - 1)
        visited = set()
        answer = []
        stack = [(start, 0, '')]
        while stack:
            node, next_digit, incoming = stack[-1]
            if next_digit < k:
                stack[-1] = (node, next_digit + 1, incoming)
                digit = str(next_digit)
                edge = node + digit
                if edge not in visited:
                    visited.add(edge)
                    stack.append((edge[1:], 0, digit))
            else:
                stack.pop()
                if incoming:
                    answer.append(incoming)
        return start + ''.join(reversed(answer))
