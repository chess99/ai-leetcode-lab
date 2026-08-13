# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid = []

        for coupon, line, active in zip(code, businessLine, isActive):
            valid_code = coupon and all(
                char.isascii() and (char.isalnum() or char == "_")
                for char in coupon
            )
            if valid_code and line in order and active:
                valid.append((order[line], coupon))

        valid.sort()
        return [coupon for _, coupon in valid]
