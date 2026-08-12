# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:39:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        length = n + m - 1
        word = ['a'] * length
        forced = [False] * length

        for start, flag in enumerate(str1):
            if flag != 'T':
                continue
            for offset, char in enumerate(str2):
                position = start + offset
                if forced[position] and word[position] != char:
                    return ""
                word[position] = char
                forced[position] = True

        forbidden = [set() for _ in range(length)]
        for start, flag in enumerate(str1):
            current = ''.join(word[start:start + m])
            if flag == 'T':
                if current != str2:
                    return ""
                continue
            if current != str2:
                continue
            position = -1
            for candidate in range(start + m - 1, start - 1, -1):
                if not forced[candidate]:
                    position = candidate
                    break
            if position < 0:
                return ""
            forbidden[position].add(str2[position - start])
            for code in range(26):
                char = chr(97 + code)
                if char not in forbidden[position]:
                    word[position] = char
                    break

        return ''.join(word)
