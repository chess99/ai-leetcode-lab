// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:14:12Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj.filter(Boolean).map(compactObject);
    }
    if (obj !== null && typeof obj === "object") {
        const result = {};
        for (const [key, value] of Object.entries(obj)) {
            if (Boolean(value)) {
                result[key] = compactObject(value);
            }
        }
        return result;
    }
    return obj;
};
