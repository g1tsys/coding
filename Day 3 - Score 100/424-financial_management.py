"""
**问题描述：**

给定 `m` 个理财产品，每个产品有：
- **投资回报率**（百分比）
- **风险值**
- **最大可投资额**

你需要在以下约束下，选择**最多2个产品**进行投资，使得：
- **总投资额 ≤ N**
- **总风险值 ≤ X**（风险值 = 各产品投资额 × 对应风险值）
- **总回报（投资额 × 回报率）最大化**

**输出：**
- 一个长度为 `m` 的整数数组，表示每个产品的**最优投资额**（按产品顺序输出）

**输入格式：**
- 第一行：`m`（产品数）、`N`（总投资额）、`X`（可接受总风险）
- 第二行：`m` 个整数，表示各产品的**回报率**
- 第三行：`m` 个整数，表示各产品的**风险值**
- 第四行：`m` 个整数，表示各产品的**最大投资额**

**输出格式：**
- 一个长度为 `m` 的整数序列，表示每个产品的**最优投资额**

**约束：**
- 投资额必须为整数，不能拆分
- 最多只能投资 2 个产品
- 总风险值 = 各产品投资额 × 对应风险值之和，不得超过 `X`

> 示例输入/输出格式可参考原文中的“样例1”和“样例2”部分（未提供具体数值）。


**输入格式：**
- 第一行：产品数 `m`（1–20）、总投资额 `N`（1–10000）、可接受总风险 `X`（1–200）
- 第二行：`m` 个整数，表示各产品的**投资回报率**（1–60）
- 第三行：`m` 个整数，表示各产品的**风险值**（1–100）
- 第四行：`m` 个整数，表示各产品的**最大投资额度**（1–10000）

**输出格式：**
- 一个长度为 `m` 的整数序列，表示每个产品的**最优投资额**（按产品顺序输出）

**约束条件：**
- 最多只能投资 **2 个产品**
- 总风险值 = 各产品投资额 × 对应风险值之和，不得超过 `X`
- 投资额必须为整数，不能拆分
- 目标：在风险约束下，使总回报（投资额 × 回报率）**最大化**

> 示例输入/输出格式可参考原文中的“样例1”和“样例2”部分（未提供具体数值）。

以下是图片中提取的**Python 解题思路**和**代码结构说明**：

---

### **Python 解题思路**

1. 定义函数 `find_best_investment` 来寻找最优投资方案。
2. 初始化最优投资方案数组 `best_investment`，所有值为 0。
3. 初始化最佳利润 `best_profit` 为 0。
4. 使用双重循环遍历所有可能的产品组合：
   - 外层循环遍历第一个产品
   - 内层循环遍历第二个产品（可与第一个相同，即单产品情况）
5. 首先考虑只投资一个产品的情况：
   - 计算该产品的投资额 `invest_i`，取 `min(max_investments[i], N)`
   - 检查风险 `risks[i]` 是否在可接受范围内 `X`
   - 如果利润超过当前最佳利润，更新 `best_investment` 和 `best_profit`
6. 接下来考虑投资两个产品的组合：
   - 对第一个产品进行投资额遍历，范围为 `1` 到 `min(max_investments[i], N)`
   - 计算剩余可投资额 `N - invest_i`，用于第二个产品的投资
   - 计算两个产品的总风险 `risk = risks[i] + risks[j]`
   - 计算总回报 `profit = invest_i * returns[i] / 100 + invest_j * returns[j] / 100`
   - 如果总风险 ≤ `X` 且利润 > 当前最佳利润，更新 `best_investment` 和 `best_profit`
7. 循环结束后，返回最优投资方案 `best_investment`
8. 主程序中：
   - 读取输入数据（产品数 `m`、总投资额 `N`、可接受风险 `X`、回报率序列 `returns`、风险值序列 `risks`、最大投资额序列 `max_investments`）
   - 调用 `find_best_investment` 函数
   - 输出结果（每个元素用空格连接）

---

### **代码结构（伪代码/框架）**

```python
def find_best_investment(m, N, X, returns, risks, max_investments):
    best_investment = [0] * m
    best_profit = 0.0

    # 单产品投资
    for i in range(m):
        invest_i = min(max_investments[i], N)
        if risks[i] <= X:
            profit = invest_i * returns[i] / 100
            if profit > best_profit:
                best_profit = profit
                best_investment = [0] * m
                best_investment[i] = invest_i

    # 两产品投资
    for i in range(m):
        for j in range(m):
            if i == j:  # 同一产品（已处理，可跳过或保留）
                continue
            for invest_i in range(1, min(max_investments[i], N) + 1):
                remaining = N - invest_i
                if remaining <= 0:
                    break
                invest_j = min(max_investments[j], remaining)
                total_risk = risks[i] + risks[j]
                if total_risk <= X:
                    profit = invest_i * returns[i] / 100 + invest_j * returns[j] / 100
                    if profit > best_profit:
                        best_profit = profit
                        best_investment = [0] * m
                        best_investment[i] = invest_i
                        best_investment[j] = invest_j

    return best_investment

# 主程序
m, N, X = map(int, input().split())
returns = list(map(int, input().split()))
risks = list(map(int, input().split()))
max_investments = list(map(int, input().split()))

result = find_best_investment(m, N, X, returns, risks, max_investments)
print(' '.join(map(str, result)))
```

---

> ⚠️ 注意：实际代码需根据输入输出格式和边界条件调整，例如是否允许投资0、是否允许同一产品投资两次等。建议结合题目样例验证逻辑。
"""

def find_best_investment(m, N, X, returns, risks, max_investments):
    # 初始化最优投资方案数组，所有值为0
    best_investment = [0] * m
    # 初始化最佳利润为0
    best_profit = 0

    # 遍历所有可能的产品组合
    for i in range(m):
        # 首先考虑只投资一个产品的情况
        invest_i = min(max_investments[i], N)  # 投资额不能超过该产品的最大投资额和总投资额N
        # 检查该产品的风险是否在可接受范围内
        if risks[i] <= X:
            profit = invest_i * returns[i] // 100  # 计算投资该产品的回报
            # 如果该方案的利润超过目前已知的最佳利润，更新最优投资方案和最佳利润
            if profit > best_profit:
                best_investment = [0] * m  # 重置最优投资方案为全0
                best_investment[i] = invest_i  # 更新最优投资方案，只投资第i个产品
                best_profit = profit

        # 接下来考虑投资两个产品的组合
        for j in range(i + 1, m):
            # 对第一个产品进行投资额的遍历
            for invest_i in range(1, min(max_investments[i], N) + 1):
                # 计算在投资了第一个产品后剩余的可投资额度，用于第二个产品
                invest_j = min(max_investments[j], N - invest_i)
                # 计算两个产品的总风险值
                risk = risks[i] + risks[j]
                # 计算投资这两个产品的总回报
                profit = invest_i * returns[i] // 100 + invest_j * returns[j] // 100

                # 如果当前组合的风险在可接受范围内且利润高于目前最佳利润，更新最优投资组合
                if risk <= X and profit > best_profit:
                    best_investment = [0] * m  # 重置最优投资方案为全0
                    best_investment[i] = invest_i  # 更新投资第i个产品的额度
                    best_investment[j] = invest_j  # 更新投资第j个产品的额度
                    best_profit = profit  # 更新最佳利润

    return best_investment


# 读取输入数据
m, N, X = map(int, input().split())  # 产品数，总投资额，可接受的总风险
returns = list(map(int, input().split()))  # 产品的投资回报率序列
risks = list(map(int, input().split()))  # 产品的风险值序列
max_investments = list(map(int, input().split()))  # 产品的最大投资额度序列

# 计算最优投资组合
best_investments = find_best_investment(m, N, X, returns, risks, max_investments)

# 输出每个产品的最优投资额序列
print(" ".join(map(str, best_investments)))
