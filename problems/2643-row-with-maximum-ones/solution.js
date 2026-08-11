// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T14:10:22Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var rowAndMaximumOnes = function(mat) {
    let answer = [0, 0];
    for (let i = 0; i < mat.length; i++) {
        const count = mat[i].reduce((a, b) => a + b, 0);
        if (count > answer[1]) answer = [i, count];
    }
    return answer;
};
