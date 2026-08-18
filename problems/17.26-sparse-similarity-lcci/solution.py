# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:32Z
# Experiment: ai-leetcode-lab, round 1
# Upgrade handoff: terra-medium -> sol-medium (gpt-5.6-sol, medium)
from collections import defaultdict
from typing import List


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        def format_similarity(common: int, union: int) -> str:
            scaled, remainder = divmod(common * 10000, union)
            if remainder * 2 >= union:
                scaled += 1
            return f"{scaled // 10000}.{scaled % 10000:04d}"

        document_count = len(docs)
        if document_count < 2:
            return []

        containing = defaultdict(list)
        inverted_work = 0
        for document_id, document in enumerate(docs):
            for word in document:
                previous_documents = containing[word]
                inverted_work += len(previous_documents)
                previous_documents.append(document_id)

        lengths = [len(document) for document in docs]
        sorted_lengths = sorted(lengths)
        pairwise_work = sum(
            length * (document_count - index - 1)
            for index, length in enumerate(sorted_lengths)
        )

        # Updating Python counters is much more expensive than probing sets in C.
        # Keep the inverted index for genuinely sparse overlaps; switch when its
        # estimated pair updates are no longer substantially fewer.
        if inverted_work * 8 <= pairwise_work:
            intersections = [0] * (document_count * document_count)
            for previous_documents in containing.values():
                for position, second in enumerate(previous_documents):
                    for first in previous_documents[:position]:
                        intersections[first * document_count + second] += 1

            answer = []
            for first in range(document_count):
                row_start = first * document_count
                for second in range(first + 1, document_count):
                    common = intersections[row_start + second]
                    if common:
                        union = lengths[first] + lengths[second] - common
                        similarity = format_similarity(common, union)
                        answer.append(f"{first},{second}: {similarity}")
            return answer

        document_sets = [set(document) for document in docs]
        answer = []
        for first in range(document_count):
            for second in range(first + 1, document_count):
                common = len(document_sets[first] & document_sets[second])
                if common:
                    union = lengths[first] + lengths[second] - common
                    similarity = format_similarity(common, union)
                    answer.append(f"{first},{second}: {similarity}")
        return answer
