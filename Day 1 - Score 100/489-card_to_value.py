"""
### Question Translation:
In the game of **Dou Di Zhu** (a popular Chinese card game), a **straight** (顺子) is defined as a sequence of **at least 5 consecutive cards**, **excluding the 2**. The cards are ordered from smallest to largest: 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2. For example, {3, 4, 5, 6, 7} and {3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A} are valid straights, while {J, Q, K, A, 2}, {2, 3, 4, 5, 6}, {3, 4, 5, 6}, and {3, 4, 5, 6, 8} are not.

Given a list of **13 cards**, your task is to find all valid straights and output them in order of the **first card** in the straight (from smallest to largest). If no valid straight exists, output **"No"**.

---

### Python Solution Chain of Thoughts:

1. **Card Mapping**:
   - Map each card (e.g., '3', 'J', 'A') to a numerical value for easier comparison.
   - Example: {'3': 0, '4': 1, ..., 'A': 11, '2': 12}.

2. **Filtering**:
   - Remove all '2' cards from the list, as they are not allowed in a straight.

3. **Sorting**:
   - Sort the remaining cards by their numerical value.

4. **Finding Straights**:
   - Iterate through the sorted list and group consecutive cards.
   - A valid straight must have **at least 5 cards** and be **consecutive** in value.

5. **Output**:
   - If any valid straight is found, output them in order of their **first card**.
   - If no valid straight is found, output **"No"**.

---

### Example Walkthrough:

**Input**:  
`3 4 5 6 7 8 9 10 J Q K A 3`

**Step-by-Step**:

1. **Filter out '2'**:
   - No '2' in the input, so the list remains unchanged.

2. **Map cards to numerical values**:
   - '3' → 0, '4' → 1, ..., 'A' → 11.

3. **Sort the list**:
   - Sorted list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]

4. **Group consecutive cards**:
   - First group: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] (this is a valid straight of 12 cards).
   - Second group: [0] (only one card, not a valid straight).

5. **Output**:
   - Only the first group is valid. So, the output is:
     
     3 4 5 6 7 8 9 10 J Q K A
     
"""


def cardToValue(card):
    """将牌面映射到数值"""
    # 定义牌面到数值的映射表
    value_map = {'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                 '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    # 返回牌面的数值
    return value_map[card]

def findValidSequences(cards):
    """找到所有符合条件的顺子"""
    # 过滤掉 '2'
    filtered_cards = [card for card in cards if card != '2']
    # 按牌面的数值从小到大排序
    sorted_cards = sorted(filtered_cards, key=cardToValue)
    # 初始化存储顺子的列表
    sequences = []

    # 遍历排序后的牌面
    for card in sorted_cards:
        # 标记是否将牌添加到现有顺子中
        added_to_sequence = False
        # 遍历已找到的顺子
        for sequence in sequences:
            # 如果当前牌可以接在某个顺子后面
            if cardToValue(card) - cardToValue(sequence[-1]) == 1:
                # 将当前牌添加到这个顺子中
                sequence.append(card)
                # 标记已添加
                added_to_sequence = True
                break
        # 如果当前牌未能添加到任何顺子中
        if not added_to_sequence:
            # 新建一个顺子，包含当前牌
            sequences.append([card])
    
    # 过滤出长度大于等于5的顺子
    valid_sequences = [sequence for sequence in sequences if len(sequence) >= 5]
    
    # 返回所有符合条件的顺子
    return valid_sequences

def main():
    # 输入描述：从标准输入读取一行，并按空格分隔成牌面列表
    input_cards = input().strip().split()
    
    # 找到所有符合条件的顺子
    valid_sequences = findValidSequences(input_cards)
    
    # 如果没有找到符合条件的顺子
    if not valid_sequences:
        print("No")
    else:
        # 按照顺子的第一张牌的大小，从小到大排序
        valid_sequences.sort(key=lambda sequence: cardToValue(sequence[0]))
        # 依次输出每个顺子
        for sequence in valid_sequences:
            print(" ".join(sequence))

# 调用main函数
if __name__ == "__main__":
    main()



