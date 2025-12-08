"""
Based on the web page content, here's a translation and explanation of this IGMP protocol problem:

## Problem Translation

**Description:**
In the IGMP protocol, there's a field called Max Response Time. When a HOST receives a query message, it parses the MaxResponseTime field and must respond within a random time in the range (0, MaxResponseTime) seconds. If a new query message is received during this random time period, the HOST compares both times and selects the smaller one to refresh the response time.

**Max Response Time Calculation:**
- When `MaxRespCode < 128`: `MaxRespTime = MaxRespCode`
- When `MaxRespCode >= 128`: `MaxRespTime = (mant | 0x10) << (exp + 3)`

Where the MaxRespCode bit structure is:
```
Bit:  0 | 1 2 3 | 4 5 6 7
      1 | exp   | mant
```
- `exp`: bits 4-6 (exponent)
- `mant`: bits 0-3 (mantissa)

**Assumption:** The HOST always selects the maximum random time.

**Input:**
- First line: Number of query messages `C`
- Following lines: Each contains `T` (receive time) and `M` (MaxRespCode), space-separated

**Output:**
- The time when HOST sends the response message

## Example Walkthrough

Let's say we have this input:
```
3
0 100
50 200
80 150
```

**Step-by-step:**

1. **Message 1** (T=0, M=100):
   - M=100 < 128, so MaxRespTime = 100
   - Response time = 0 + 100 = **100**

2. **Message 2** (T=50, M=200):
   - M=200 >= 128, need to calculate:
   - Binary: 200 = 11001000
   - exp = bits 4-6 = 100 (binary) = 4
   - mant = bits 0-3 = 1000 (binary) = 8
   - MaxRespTime = (8 | 0x10) << (4 + 3) = (8 | 16) << 7 = 24 << 7 = 3072
   - Response time = 50 + 3072 = 3122
   - Compare with previous: min(100, 3122) = **100**

3. **Message 3** (T=80, M=150):
   - M=150 >= 128, calculate:
   - Binary: 150 = 10010110
   - exp = 001 (binary) = 1
   - mant = 0110 (binary) = 6
   - MaxRespTime = (6 | 16) << (1 + 3) = 22 << 4 = 352
   - Response time = 80 + 352 = 432
   - Compare with previous: min(100, 432) = **100**

**Final Output:** 100

The key insight is that each new message can only reduce (never increase) the response deadline, and you always take the minimum response time across all messages.
"""


import sys

def calculate_response_time(packet_count, packet_info):
    response_time = float('inf')  # 初始化响应时间为正无穷大，便于后续取最小值

    for i in range(packet_count):
        received_time = packet_info[i][0]  # 数据包接收时间
        max_resp_code = packet_info[i][1]  # 数据包最大响应码
        
        if max_resp_code < 128:
            # 如果最大响应码小于128，则响应时间直接为最大响应码
            current_resp_time = received_time + max_resp_code
        else:
            # 如果最大响应码大于等于128，则需要按照公式计算
            exp = (max_resp_code >> 4) & 0x07  # 响应码的指数部分（高3位）
            mant = max_resp_code & 0x0F        # 响应码的尾数部分（低4位）
            current_resp_time = received_time + ((mant | 0x10) << (exp + 3))  # 计算响应时间
        
        # 更新最小的响应时间
        response_time = min(response_time, current_resp_time)

    return response_time

# 从标准输入读取所有输入
input_data = sys.stdin.read().split()

# 解析输入数据
packet_count = int(input_data[0])  # 数据包数量
packet_info = []  # 存储数据包信息的列表

index = 1
for i in range(packet_count):
    received_time = int(input_data[index])  # 读取数据包接收时间
    max_resp_code = int(input_data[index + 1])  # 读取数据包最大响应码
    packet_info.append([received_time, max_resp_code])  # 将接收时间和最大响应码添加到列表中
    index += 2  # 更新索引以读取下一个数据包的信息

# 计算HOST发送响应报文的时间
response_time = calculate_response_time(packet_count, packet_info)
print(response_time)  # 输出结果

