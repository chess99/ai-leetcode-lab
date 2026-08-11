# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:18:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = releaseTimes[0]
        answer = keysPressed[0]
        for index in range(1, len(releaseTimes)):
            duration = releaseTimes[index] - releaseTimes[index - 1]
            if duration > longest or (duration == longest and keysPressed[index] > answer):
                longest = duration
                answer = keysPressed[index]
        return answer
