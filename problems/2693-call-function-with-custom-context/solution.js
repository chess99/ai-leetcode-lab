// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:14:12Z
// Experiment: ai-leetcode-lab, round 1
Function.prototype.callPolyfill = function(context, ...args) {
    const key = Symbol();
    context[key] = this;
    const result = context[key](...args);
    delete context[key];
    return result;
};
