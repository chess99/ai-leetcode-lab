# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
最大频次超过一半时它无法全部配对，剩余为 `2*maxFreq-n`；否则只由总长度奇偶决定。
## 复杂度
时间 `O(n)`，空间 `O(n)`。
## 边界条件与本地验证
全部相同与所有可配对情形均覆盖；已验证样例。
