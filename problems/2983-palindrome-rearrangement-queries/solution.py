# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Handoff: optimized independently after terra-medium timed out
from typing import List


class Solution:
    def canMakePalindromeQueries(
        self, s: str, queries: List[List[int]]
    ) -> List[bool]:
        n = len(s)
        half = n // 2
        left = s[:half]
        right = s[half:][::-1]

        def build_prefix(text: str) -> List[List[int]]:
            prefix = [[0] * 26]
            for ch in text:
                row = prefix[-1].copy()
                row[ord(ch) - ord("a")] += 1
                prefix.append(row)
            return prefix

        left_count = build_prefix(left)
        right_count = build_prefix(right)

        mismatch = [0] * (half + 1)
        for i in range(half):
            mismatch[i + 1] = mismatch[i] + (left[i] != right[i])

        answer = []
        total_mismatch = mismatch[half]

        for left_l, left_r, original_right_l, original_right_r in queries:
            # Mirror the interval in the original right half onto right's coordinates.
            right_l = n - 1 - original_right_r
            right_r = n - 1 - original_right_l

            overlap_l = max(left_l, right_l)
            overlap_r = min(left_r, right_r)
            has_overlap = overlap_l <= overlap_r

            covered_mismatch = (
                mismatch[left_r + 1]
                - mismatch[left_l]
                + mismatch[right_r + 1]
                - mismatch[right_l]
            )
            if has_overlap:
                covered_mismatch -= (
                    mismatch[overlap_r + 1] - mismatch[overlap_l]
                )
            if covered_mismatch != total_mismatch:
                answer.append(False)
                continue

            # Cache every prefix row once.  In particular, do not construct a
            # 26-element range-count list inside the loop over the alphabet.
            li0 = left_count[left_l]
            li1 = left_count[left_r + 1]
            lj0 = left_count[right_l]
            lj1 = left_count[right_r + 1]
            ri0 = right_count[left_l]
            ri1 = right_count[left_r + 1]
            rj0 = right_count[right_l]
            rj1 = right_count[right_r + 1]
            if has_overlap:
                lk0 = left_count[overlap_l]
                lk1 = left_count[overlap_r + 1]
                rk0 = right_count[overlap_l]
                rk1 = right_count[overlap_r + 1]

            possible = True
            for ch in range(26):
                left_available = li1[ch] - li0[ch]
                right_available = rj1[ch] - rj0[ch]

                # I \ J must consume from left to match the fixed right side.
                fixed_right_need = ri1[ch] - ri0[ch]
                # J \ I must consume from right to match the fixed left side.
                fixed_left_need = lj1[ch] - lj0[ch]
                if has_overlap:
                    fixed_right_need -= rk1[ch] - rk0[ch]
                    fixed_left_need -= lk1[ch] - lk0[ch]

                left_remaining = left_available - fixed_right_need
                right_remaining = right_available - fixed_left_need
                if (
                    left_remaining < 0
                    or right_remaining < 0
                    or left_remaining != right_remaining
                ):
                    possible = False
                    break

            answer.append(possible)

        return answer
