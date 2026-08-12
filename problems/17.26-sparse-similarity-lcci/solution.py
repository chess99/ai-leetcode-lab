# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        containing = defaultdict(list)
        intersections = defaultdict(int)
        for document_id, document in enumerate(docs):
            for word in document:
                previous_documents = containing[word]
                for previous_id in previous_documents:
                    intersections[(previous_id, document_id)] += 1
                previous_documents.append(document_id)
        answer = []
        for (first, second), common in intersections.items():
            union = len(docs[first]) + len(docs[second]) - common
            answer.append(f"{first},{second}: {common / union:.4f}")
        return answer
