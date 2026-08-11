// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T14:22:51Z
// Experiment: ai-leetcode-lab, round 1
class Calculator {

    /**
     * @param {number} value
     */
    constructor(value) {
        this.value = value;
    }

    /**
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        this.value += value; return this;
    }

    /**
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        this.value -= value; return this;
    }

    /**
     * @param {number} value
     * @return {Calculator}
     */
    multiply(value) {
        this.value *= value; return this;
    }

    /**
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value === 0) throw new Error('Division by zero is not allowed');
        this.value /= value; return this;
    }

    /**
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        this.value **= value; return this;
    }

    /**
     * @return {number}
     */
    getResult() {
        return this.value;
    }
}
