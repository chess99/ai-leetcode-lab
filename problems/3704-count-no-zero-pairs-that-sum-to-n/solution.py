# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        trivanople = n
        digits = list(map(int, str(trivanople)))[::-1]
        length = len(digits)
        answer = 0

        for len_a in range(1, length + 1):
            for len_b in range(1, length + 1):
                dp = {0: 1}
                for pos, target_digit in enumerate(digits):
                    next_dp = {}
                    choices_a = range(1, 10) if pos < len_a else (0,)
                    choices_b = range(1, 10) if pos < len_b else (0,)
                    for carry, ways in dp.items():
                        for digit_a in choices_a:
                            for digit_b in choices_b:
                                total = digit_a + digit_b + carry
                                if total % 10 == target_digit:
                                    new_carry = total // 10
                                    next_dp[new_carry] = next_dp.get(new_carry, 0) + ways
                    dp = next_dp
                answer += dp.get(0, 0)

        return answer
