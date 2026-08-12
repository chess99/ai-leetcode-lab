# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        unchanged_mask = 0
        unchanged_parts = 0
        changed_states = {}

        def advance(mask, parts, bit):
            merged = mask | bit
            if merged.bit_count() > k:
                return bit, parts + 1
            return merged, parts

        for character in s:
            original_bit = 1 << (ord(character) - 97)
            next_states = {}
            for mask, parts in changed_states.items():
                next_mask, next_parts = advance(mask, parts, original_bit)
                next_states[next_mask] = max(
                    next_states.get(next_mask, -1), next_parts
                )
            for replacement in range(26):
                next_mask, next_parts = advance(
                    unchanged_mask, unchanged_parts, 1 << replacement
                )
                next_states[next_mask] = max(
                    next_states.get(next_mask, -1), next_parts
                )
            changed_states = next_states
            unchanged_mask, unchanged_parts = advance(
                unchanged_mask, unchanged_parts, original_bit
            )

        return max(unchanged_parts, *changed_states.values()) + 1
