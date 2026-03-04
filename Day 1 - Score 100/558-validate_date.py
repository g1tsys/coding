"""
I'll translate the problem description and Python approach, then provide an example walkthrough.
## Problem Translation

**Free Order Statistics**

Huawei Mall is running a promotion where customers who place orders at the earliest moment within any given second (there may be multiple such customers) receive a free order. Calculate how many customers can get free orders.

**Input:**
- n lines of data, each representing a customer's order time
- Format: `yyyy-MM-dd HH:mm:ss:fff` (year-month-day hour:minute:second:millisecond)
- Constraints: 0 < n < 50000, valid date ranges provided

**Output:**
- An integer representing how many customers can get free orders

## Python Approach (Translated)

1. Read all customer order timestamps and store them in a list
2. Create a dictionary to store the minimum millisecond value for each second. The key is the timestamp prefix (everything before milliseconds), and the value is the minimum millisecond number
3. Iterate through the order times, split each timestamp to get the prefix part and millisecond part
4. If the prefix doesn't exist in the dictionary, add it with the current millisecond value
5. If the prefix already exists, compare the current millisecond with the stored value and update if the current one is smaller
6. Iterate through the order times again, split each timestamp
7. If the dictionary contains the prefix and its value equals the current millisecond, this customer ordered earliest in that second, so increment the counter
8. Return the counter value (number of customers who get free orders)

## Example Walkthrough

**Input:**
```
2019-01-01 08:59:00:123
2019-01-01 08:59:00:123
2019-01-01 08:59:00:456
2019-01-01 08:59:01:123
```

**Step-by-step:**

1. **First pass** - Find minimum millisecond for each second:
   - `2019-01-01 08:59:00` → min = 123
   - `2019-01-01 08:59:01` → min = 123

2. **Second pass** - Count customers with minimum millisecond:
   - `2019-01-01 08:59:00:123` → matches min (123) ✓
   - `2019-01-01 08:59:00:123` → matches min (123) ✓
   - `2019-01-01 08:59:00:456` → doesn't match min ✗
   - `2019-01-01 08:59:01:123` → matches min (123) ✓

**Output:** 3 customers get free orders
"""


from datetime import datetime

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        return True
    except ValueError:
        return False

def put_min_value_to_map(date_prefix, date_suffix, date_map):
    # 如果日期前缀不在date_map中，则将日期前缀和日期后缀添加到date_map中
    if date_prefix not in date_map:
        date_map[date_prefix] = date_suffix
    else:
        # 如果日期前缀已存在于date_map中，则比较日期后缀的大小，保留较小的日期后缀
        if int(date_map[date_prefix]) > int(date_suffix):
            date_map[date_prefix] = date_suffix

def get_top_user_num(top_dates):
    top_user = 0
    date_map = {}

    # 遍历top_dates列表中的每个日期
    for top_date in top_dates:
        date_parts = top_date.split('.')
        date_prefix = date_parts[0]
        date_suffix = date_parts[1]
        put_min_value_to_map(date_prefix, date_suffix, date_map)

    # 再次遍历top_dates列表中的每个日期
    for date in top_dates:
        date_parts = date.split('.')
        date_prefix = date_parts[0]
        date_suffix = date_parts[1]
        # 如果日期前缀在date_map中，并且日期后缀与date_map中对应的日期后缀相等，则top_user加1
        if date_prefix in date_map and date_map[date_prefix] == date_suffix:
            top_user += 1

    return top_user

n = 3
top_dates = [
    '2019-01-01 00:00:00.001',
    '2019-01-01 00:00:00.002',
    '2019-01-01 00:00:00.003'
]

top_user_num = get_top_user_num(top_dates)
print(top_user_num)


