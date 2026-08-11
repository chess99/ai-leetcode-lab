# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        hours = 0
        for energy, experience in zip(energy, experience):
            if initialEnergy <= energy:
                hours += energy - initialEnergy + 1
                initialEnergy = energy + 1
            initialEnergy -= energy
            if initialExperience <= experience:
                hours += experience - initialExperience + 1
                initialExperience = experience + 1
            initialExperience += experience
        return hours
