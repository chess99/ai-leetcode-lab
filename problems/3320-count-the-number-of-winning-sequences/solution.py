# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countWinningSequences(self, s: str) -> int:
        modulus = 1_000_000_007
        creatures = {'F': 0, 'W': 1, 'E': 2}
        states = {(3, 0): 1}
        for character in s:
            alice = creatures[character]
            next_states = {}
            for (last, difference), ways in states.items():
                for bob in range(3):
                    if bob == last:
                        continue
                    result = 0 if bob == alice else (1 if (bob - alice) % 3 == 1 else -1)
                    key = (bob, difference + result)
                    next_states[key] = (next_states.get(key, 0) + ways) % modulus
            states = next_states
        return sum(ways for (_, difference), ways in states.items()
                   if difference > 0) % modulus
