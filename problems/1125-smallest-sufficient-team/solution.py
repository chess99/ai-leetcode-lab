# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_index = {skill: index for index, skill in enumerate(req_skills)}
        person_masks = []
        for skills in people:
            mask = 0
            for skill in skills:
                if skill in skill_index:
                    mask |= 1 << skill_index[skill]
            person_masks.append(mask)
        teams = {0: []}
        for person, person_mask in enumerate(person_masks):
            if person_mask == 0:
                continue
            for covered, team in list(teams.items()):
                combined = covered | person_mask
                if combined not in teams or len(team) + 1 < len(teams[combined]):
                    teams[combined] = team + [person]
        return teams[(1 << len(req_skills)) - 1]
