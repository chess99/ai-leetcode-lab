// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:14:12Z
// Experiment: ai-leetcode-lab, round 1
class EventEmitter {
    constructor() { this.listeners = new Map(); }
    subscribe(eventName, callback) {
        if (!this.listeners.has(eventName)) this.listeners.set(eventName, []);
        const listeners = this.listeners.get(eventName);
        listeners.push(callback);
        return { unsubscribe: () => { const i = listeners.indexOf(callback); if (i !== -1) listeners.splice(i, 1); } };
    }
    emit(eventName, args = []) { return (this.listeners.get(eventName) || []).map(callback => callback(...args)); }
}
