# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        remove_left = remove_right = 0
        for char in s:
            if char == '(':
                remove_left += 1
            elif char == ')':
                if remove_left:
                    remove_left -= 1
                else:
                    remove_right += 1
        answer = set()

        def search(index, balance, left, right, path):
            if index == len(s):
                if balance == 0 and left == 0 and right == 0:
                    answer.add(''.join(path))
                return
            char = s[index]
            if char == '(':
                if left:
                    search(index + 1, balance, left - 1, right, path)
                path.append(char)
                search(index + 1, balance + 1, left, right, path)
                path.pop()
            elif char == ')':
                if right:
                    search(index + 1, balance, left, right - 1, path)
                if balance:
                    path.append(char)
                    search(index + 1, balance - 1, left, right, path)
                    path.pop()
            else:
                path.append(char)
                search(index + 1, balance, left, right, path)
                path.pop()

        search(0, 0, remove_left, remove_right, [])
        return list(answer)
