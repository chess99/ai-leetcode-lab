# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
用统一的 advance 驱动 generator.next 与 generator.throw。每次 yield 都绑定一个递增代号，只有当前代号的 Promise 结算才可继续生成器。取消时先让旧 Promise 失效，再把字符串 "Cancelled" 通过 generator.throw 抛回：若生成器捕获它，就继续处理其下一次 yield 或返回值；若未捕获，外层 Promise 才拒绝。
## 复杂度
时间与 yield 次数成正比，额外空间 O(1)。
## 边界条件与本地验证
验证了立即完成、普通 resolve/reject、等待中取消且未捕获、捕获取消后返回已有结果，以及取消后旧 Promise 结算不会再次执行生成器。
