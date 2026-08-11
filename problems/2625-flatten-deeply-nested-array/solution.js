// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:01:28Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const result = [];
    const visit = (items, depth) => {
        for (const item of items) {
            if (Array.isArray(item) && depth > 0) {
                visit(item, depth - 1);
            } else {
                result.push(item);
            }
        }
    };
    visit(arr, n);
    return result;
};
