"""
Based on the provided text and image, here is the extracted information about the problem:

### **Problem: Rock-Paper-Scissors Game (OD Exam)**

**Description:**
- Three possible moves: Rock (A), Scissors (B), Paper (C).
- Rules: A > B, B > C, C > A (left side is stronger).
- A player wins if their move is strictly stronger than all others.
- If no single move is stronger, or multiple moves are equally strong, it's a tie.
- Output the winner(s) or "NULL" if there's no winner.a

**Input:**
- Each line contains a player's ID (string of letters and digits) and their move (A, B, or C).
- Number of players ≤ 1000.

**Output:**
- List of winning player IDs in ascending order.
- If no winner, output "NULL".

**Image Content (Step-by-Step Solution):**
1.  **Initialize:** Create a dictionary `players_by_shape` to store players for each move (A, B, C).
2.  **Read Input:** Read each line, split into ID and move, and add the ID to the corresponding list in the dictionary.
3.  **Determine Winner:**
    - If only one move has players, or all three moves are present, return "NULL" (tie).
    - Otherwise, determine the winning move (the one with the most players).
    - Return the list of players who made the winning move.
4.  **Output:** Sort the winning player IDs and print them, or print "NULL".
"""
# 初始化一个字典，用于存储每种出拳形状的玩家列表
# 出拳形状作为字典的键，玩家ID的列表作为值
players_by_shape = {'A': [], 'B': [], 'C': []}

# 读取输入并填充字典
while True:
    try:
        line = input()  # 读取一行输入
        if not line:
            break  # 如果输入为空，跳出循环
        player_id, shape = line.split()  # 将输入的一行以空格分开，得到玩家ID和出拳形状
        players_by_shape[shape].append(player_id)  # 将玩家ID加入对应出拳形状的列表中
    except EOFError:  # 读取到文件末尾时，EOFError将被抛出
        break


# 定义函数来判断谁是赢家
def determine_winner(players_by_shape):
    # 如果只有一种出拳形状，或者三种出拳形状都有玩家，那么判定为平局
    if len([shape for shape, players in players_by_shape.items() if players]) != 2:
        return "NULL"

    # 确定哪种出拳形状是优胜的
    # 因为不是平局，所以必定有两种出拳形状
    # 优胜的出拳形状必定是人数多的那个
    shapes = [shape for shape in players_by_shape if players_by_shape[shape]]
    winning_shape = 'A' if ('A' in shapes and 'B' in shapes) else 'B' if 'B' in shapes else 'C'

    # 返回优胜出拳形状的所有玩家ID列表
    return sorted(players_by_shape[winning_shape])


# 调用函数并输出结果
winners = determine_winner(players_by_shape)
if winners == "NULL":
    print(winners)
else:
    for winner in winners:
        print(winner)

