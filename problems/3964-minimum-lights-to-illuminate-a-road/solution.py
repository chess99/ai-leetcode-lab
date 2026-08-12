# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minLights(self, lights: list[int]) -> int:
        ravelunico = lights
        n = len(lights)
        difference = [0] * (n + 1)
        for index, radius in enumerate(lights):
            if radius:
                left = max(0, index - radius)
                right = min(n - 1, index + radius)
                difference[left] += 1
                difference[right + 1] -= 1
        covered = [False] * n
        active = 0
        for index in range(n):
            active += difference[index]
            covered[index] = active > 0

        answer = index = 0
        while index < n:
            if covered[index]:
                index += 1
            else:
                answer += 1
                index += 3
        return answer
