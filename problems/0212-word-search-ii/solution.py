# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for ch in word: node = node.setdefault(ch, {})
            node["#"] = word
        result = []
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node: return
            node = node[ch]; word = node.pop("#", None)
            if word: result.append(word)
            board[r][c] = ""
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc]: dfs(nr, nc, node)
            board[r][c] = ch
        for r in range(len(board)):
            for c in range(len(board[0])): dfs(r, c, root)
        return result
