# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestBalanced(self, s: str) -> int:
        tanqorivel = s
        first_zero = tanqorivel.find('0')
        first_one = tanqorivel.find('1')
        total_zero = tanqorivel.count('0')
        total_one = len(tanqorivel) - total_zero

        earliest = {}
        after_zero = {}
        after_one = {}
        balance = zeros = ones = 0
        answer = 0
        for prefix_index in range(len(tanqorivel) + 1):
            earliest.setdefault(balance, prefix_index)
            if first_zero >= 0 and prefix_index > first_zero:
                after_zero.setdefault(balance, prefix_index)
            if first_one >= 0 and prefix_index > first_one:
                after_one.setdefault(balance, prefix_index)

            answer = max(answer, prefix_index - earliest[balance])

            # 差为 2 时需把子串内的 1 与子串外的 0 交换。
            source = earliest if zeros < total_zero else after_zero
            if balance - 2 in source:
                answer = max(answer, prefix_index - source[balance - 2])

            # 差为 -2 时需把子串内的 0 与子串外的 1 交换。
            source = earliest if ones < total_one else after_one
            if balance + 2 in source:
                answer = max(answer, prefix_index - source[balance + 2])

            if prefix_index < len(tanqorivel):
                if tanqorivel[prefix_index] == '1':
                    balance += 1
                    ones += 1
                else:
                    balance -= 1
                    zeros += 1
        return answer
