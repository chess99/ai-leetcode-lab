// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:14:11Z
// Experiment: ai-leetcode-lab, round 1
/** @param {Array} arr @return {Generator} */
var inorderTraversal = function*(arr) {
    const stack = [[arr, 0]];
    while (stack.length) {
        const top = stack[stack.length - 1];
        if (top[1] === top[0].length) { stack.pop(); continue; }
        const value = top[0][top[1]++];
        if (Array.isArray(value)) stack.push([value, 0]);
        else yield value;
    }
};
