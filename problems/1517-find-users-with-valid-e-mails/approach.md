# 解题记录

- 初始创建：Codex Desktop / gpt-5.6-terra / medium / terra-medium
- 本轮接手：Codex Desktop / gpt-5.6-sol / medium / sol-medium
- 接手原因：terra-medium 三次真实提交均失败
- 轮次：1

## 失败交接

1. 第一次使用默认 `REGEXP`，平台排序规则的正则匹配不区分大小写，错误接受了 `winston@leetcode.COM`，远判为 `Wrong Answer`（27/29）。
2. 第二次改用 `REGEXP BINARY`，平台在第一个用例即报告：`Character set 'utf8mb3_general_ci' cannot be used in conjunction with 'binary' in call to regexp_like.`
3. 第三次仍为相同候选和相同错误，远判再次为 `Runtime Error`（0/29）。

## SQL 思路

使用 MySQL 8 的 `REGEXP_LIKE`，通过第三个参数 `'c'` 明确要求大小写敏感匹配：

- `^[A-Za-z]`：前缀必须由 ASCII 字母开头；
- `[A-Za-z0-9_.-]*`：前缀其余字符只允许字母、数字、下划线、点和连字符；
- `@leetcode[.]com$`：域名必须精确为小写 `@leetcode.com`，并位于字符串结尾。

`'c'` 是正则匹配参数，不把 `mail` 转成二进制字符串，也不指定一个与列字符集冲突的 binary 排序规则，因此既覆盖 `.COM` 的大小写边界，也避开 Terra 候选触发的字符集不兼容错误。

## 复杂度

设用户数为 `n`，邮箱最大长度为 `m`。查询扫描每行并检查邮箱，时间复杂度为 `O(nm)`；除结果集和正则引擎内部状态外，查询不建立额外表结构。

## 本地验证

- 使用独立、大小写敏感的完整匹配 oracle 验证题面 7 行样例，只保留用户 1、3、4。
- 边界覆盖合法的大小写前缀、数字/下划线/点/连字符，及非法首字符、`#`、缺失前缀、错误域名、额外后缀。
- 专门验证 `@leetcode.COM`、`@Leetcode.com`、`@leetcode.Com` 均被拒绝，精确小写 `@leetcode.com` 被接受。
- 静态检查 SQL 使用 `REGEXP_LIKE` 的 `'c'` 参数，且不再出现 `BINARY` 或 binary collation。
