
"""
# Translation and Analysis

## Problem Translation

**Texas Hold'em Poker Hand Classification**

You are given 5 cards, each with a rank and suit. Ranks are: 2-10, J, Q, K, A. Suits are: Hearts (H), Spades (S), Clubs (C), Diamonds (D).

**Classify the poker hand into these types (in order of strength):**

1. **Straight Flush**: Five consecutive cards of the same suit (e.g., 2♥ 3♥ 4♥ 5♥ 6♥)
2. **Four of a Kind**: Four cards of the same rank + one other card (e.g., A♥ A♠ A♣ A♦ K♠)
3. **Full House**: Three cards of one rank + two cards of another rank (e.g., 5♥ 5♠ 5♣ 9♦ 9♣)
4. **Flush**: Five cards of the same suit (e.g., 3♦ 7♦ 10♦ J♦ Q♦)
5. **Straight**: Five consecutive cards of different suits (e.g., 2♥ 3♠ 4♥ 5♥ 6♦)
6. **Three of a Kind**: Three cards of the same rank + two other cards

**Important Notes:**
- No duplicate cards
- Lower numbers indicate stronger hands
- Valid straights with A: `10-J-Q-K-A` and `A-2-3-4-5` only (not `K-A-2-3-4`)
- Output the strongest hand type number

---

## Python Thought Process

**Step 1: Card Value Mapping**
- Convert face cards to numbers: J=11, Q=12, K=13, A=14
- Store card values and suits separately

**Step 2: Check Each Hand Type (from strongest to weakest)**
- **Straight Flush**: Check if both straight AND flush
- **Four of a Kind**: Count card frequencies, look for 4 of same rank
- **Full House**: Look for 3 of one rank + 2 of another
- **Flush**: All 5 cards have same suit
- **Straight**: Check consecutive values (handle A-2-3-4-5 special case)
- **Three of a Kind**: Look for 3 of same rank

**Step 3: Return the Best Match**
- Return the smallest number (strongest hand)

---

## Example Walkthrough

**Input:**
```
2 H
3 H
4 H
5 H
6 H
```

**Process:**

1. **Parse cards:**
   - Values: [2, 3, 4, 5, 6]
   - Suits: ['H', 'H', 'H', 'H', 'H']

2. **Check Straight Flush:**
   - Is Flush? → All suits are 'H' ✓
   - Is Straight? → Sorted values [2,3,4,5,6] are consecutive ✓
   - **Result: Type 1 (Straight Flush)**

3. **Output:** `1`

---

**Another Example:**

**Input:**
```
A H
A S
A C
A D
K S
```

**Process:**

1. **Parse cards:**
   - Values: [14, 14, 14, 14, 13]
   - Suits: ['H', 'S', 'C', 'D', 'S']

2. **Check hands:**
   - Straight Flush? → Not all same suit ✗
   - Four of a Kind? → Four A's (value 14) ✓
   - **Result: Type 2 (Four of a Kind)**

3. **Output:** `2`

"""





def get_card_value(card):
    # 将牌大小转换为对应的数值
    if card[0] == 'A':
        return 14
    elif card[0] == 'K':
        return 13
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'J':
        return 11
    else:
        return int(card[0])


def get_card_suit(card):
    # 获取牌的花色
    return card[1]


def is_straight(cards):
    # 判断是否为顺子
    values = [get_card_value(card) for card in cards]
    values.sort()

    # 特殊情况：A 2 3 4 5
    if values == [2, 3, 4, 5, 14]:
        return True

    # 判断是否为连续的数值
    for i in range(1, len(values)):
        if values[i] - values[i-1] != 1:
            return False

    return True


def is_flush(cards):
    # 判断是否为同花
    suits = [get_card_suit(card) for card in cards]

    # 判断所有牌的花色是否相同
    return all(suit == suits[0] for suit in suits)


def is_full_house(cards):
    # 判断是否为葫芦
    values = [get_card_value(card) for card in cards]
    value_counts = [values.count(value) for value in set(values)]

    return sorted(value_counts) == [2, 3]


def is_four_of_a_kind(cards):
    # 判断是否为四条
    values = [get_card_value(card) for card in cards]
    value_counts = [values.count(value) for value in set(values)]

    return sorted(value_counts) == [1, 4]


def classify_poker_hand(cards):
    if is_straight(cards) and is_flush(cards):
        return 1  # 同花顺
    elif is_four_of_a_kind(cards):
        return 2  # 四条
    elif is_full_house(cards):
        return 3  # 葫芦
    elif is_flush(cards):
        return 4  # 同花
    elif is_straight(cards):
        return 5  # 顺子
    else:
        return 6  # 三条


# 读取输入
cards = [input().split() for _ in range(5)]

# 调用函数进行分类
result = classify_poker_hand(cards)

# 输出结果
print(result)

