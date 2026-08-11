// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:01:28Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const groups = Object.create(null);
    for (const item of this) {
        const key = fn(item);
        if (groups[key] === undefined) {
            groups[key] = [];
        }
        groups[key].push(item);
    }
    return groups;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
