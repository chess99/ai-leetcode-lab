# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        selvadrik = (chunks, queries)
        text = ''.join(selvadrik[0])
        counts = {}
        current = []

        def finish_word() -> None:
            if current:
                word = ''.join(current)
                counts[word] = counts.get(word, 0) + 1
                current.clear()

        for index, char in enumerate(text):
            if 'a' <= char <= 'z':
                current.append(char)
            elif char == '-' and index > 0 and index + 1 < len(text) \
                    and 'a' <= text[index - 1] <= 'z' and 'a' <= text[index + 1] <= 'z':
                current.append(char)
            else:
                finish_word()
        finish_word()
        return [counts.get(query, 0) for query in selvadrik[1]]
