# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        previous_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(":")
            function_id = int(function_id)
            timestamp = int(timestamp)
            if action == "start":
                if stack:
                    result[stack[-1]] += timestamp - previous_time
                stack.append(function_id)
                previous_time = timestamp
            else:
                result[stack.pop()] += timestamp - previous_time + 1
                previous_time = timestamp + 1
        return result
