# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        answer = [0] * numberOfUsers
        online_until = [0] * numberOfUsers
        for kind, time_text, data in sorted(events, key=lambda event: (int(event[1]), event[0] == 'MESSAGE')):
            time = int(time_text)
            if kind == 'OFFLINE':
                online_until[int(data)] = time + 60
            elif data == 'ALL':
                for user in range(numberOfUsers):
                    answer[user] += 1
            elif data == 'HERE':
                for user in range(numberOfUsers):
                    if online_until[user] <= time:
                        answer[user] += 1
            else:
                for token in data.split():
                    answer[int(token[2:])] += 1
        return answer
