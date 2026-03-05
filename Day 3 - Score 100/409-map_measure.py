"""
题目描述
给定一个二叉树,每个节点上站着一个人,节点数字表示父节点到该节点传递悄悄话需要花费的
时间。
初始时,根节点所在位置的人有一个悄悄话想要传递给其他人,求二叉树所有节点上的人都接收
到悄悄话花费的时间。
输入输出Q
输入
给定二叉树
输出
返回所有节点都接收到悄悄话花费的时间

代码思路参考做法1:
1.定义一个名为speak的函数,接受三个参数:nds表示二叉树节点的列表,index表示当前节点的
索引,current_sum表示当前路径的累积和。
2.首先判断当前节点索引是否超出范围或当前节点是否为空节点(价值为-1),如果是,则返回当前
路径的累积和。
3.如果当前节点不为空,则将当前节点的值累加到current_sum中。
4.递归处理当前节点的左子树,传递的参数为nds、index*2+1和current_sum,更新左子树路径
和为left_sum。
5.递归处理当前节点的右子树,传递的参数为nds、index*2+2和current_sum,更新右子树路径
和为right_sum。
6.返回左右子树路径和的最大值。
7.在main函数中,首先读取用户输入的二叉树节点列表,并将其转换为整数列表。
8.调用speak函数计算最大路径和,并将结果打印出来。
"""


def speak(nds, index=0, current_sum=0):
    # 如果节点索引超出范围或节点值为-1（表示空节点），则返回当前路径的累积和
    if index >= len(nds) or nds[index] == -1:
        return current_sum
    # 累加当前节点的值
    current_sum += nds[index]
    # 递归处理左子树，并更新路径和
    left_sum = speak(nds, index * 2 + 1, current_sum)
    # 递归处理右子树，并更新路径和
    right_sum = speak(nds, index * 2 + 2, current_sum)
    # 返回左右子树路径和的最大值
    return max(left_sum, right_sum)

def main():
    st = input()  # 从用户那里读取输入
    # 将输入字符串分割并转换成整数列表
    nodes = list(map(int, st.split()))
    # 计算最大路径和
    max_value = speak(nodes)
    print(max_value)  # 打印最大路径和

if __name__ == "__main__":
    main()
