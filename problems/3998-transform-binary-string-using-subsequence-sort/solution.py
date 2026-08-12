# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        veltromina = (s, strs)
        zeroprefix = []
        zeros = 0
        for char in s:
            zeros += char == '0'
            zeroprefix.append(zeros)

        answer = []
        for target in strs:
            fixed_zero = target.count('0')
            questions = target.count('?')
            question_zeros = zeros - fixed_zero
            # Sorting a binary subsequence can only move zeros left.  Thus the
            # number of zeros in every target prefix must be at least the
            # corresponding source prefix.  A prefix has at most its fixed
            # zeros plus all its question marks available for that purpose.
            possible = fixed_zero <= zeros <= fixed_zero + questions
            fixed_prefix = question_prefix = 0
            for i, char in enumerate(target):
                fixed_prefix += char == '0'
                question_prefix += char == '?'
                # 全串只需把 question_zeros 个问号补成 0，不能把前缀内
                # 超出该配额的问号同时视为 0。
                capacity = fixed_prefix + min(question_prefix, question_zeros)
                if capacity < zeroprefix[i]:
                    possible = False
                    break
            answer.append(possible)
        return answer
