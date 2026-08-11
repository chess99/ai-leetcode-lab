// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:01:28Z
// Experiment: ai-leetcode-lab, round 1
var TimeLimitedCache = function() {
    this.values = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    const entry = this.values.get(key);
    const existed = entry !== undefined && entry.expiresAt > now;
    this.values.set(key, { value, expiresAt: now + duration });
    return existed;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const entry = this.values.get(key);
    if (entry === undefined || entry.expiresAt <= Date.now()) {
        this.values.delete(key);
        return -1;
    }
    return entry.value;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    for (const [key, entry] of this.values) {
        if (entry.expiresAt <= now) {
            this.values.delete(key);
        }
    }
    return this.values.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
