"""
题目描述
有N块二手市场收集的银饰,每块银饰的重量都是正整数,收女集到的银饰会被熔化用于打造新的
饰品。
每一回合,从中选出三块最重的银饰,然后一起熔掉。假设银饰的重量分别为x、y和z,且x
<=у<=z。那么熔掉的可能结果如下:
如果x==y==z,那么三块银饰都会被完全熔掉;
如果x==у且y!=z,会剩余重量为z-y的银块无法被熔掉;
如果x!=y且y==z,会剩余重量为y-x的银块无法被熔掉;
如果x!=y且y!=z,会剩余重量为z-y与y-x差值的银块无法皮膚
最后,如果剩余两块,返回较大的重量(若两块重量相同,返回任意一块皆可);如果只剩下一
块,返回该块的重量;如果没有剩下,就返回0
输入输出Q
输入
输入数据为两行
第一行为银饰数组长度n,1sn≤40,
第二行为n块银饰的重量,重量的取值范围为[1,2000],重量之间使用空格隔开
输出
如果剩余两块,返回较大的重量(若两块重量相同,返回任意一块皆可);如果只剩下一块,返
回该块的重量;如果没有剩下,就返回0。


1.首先,读取输入数据,包括银饰的数量和每个银饰的重量。
2.将银饰重量列表进行排序,以便每次选择最重的三块银饰进行熔化。
3.使用一个循环来不断选择最重的三块银饰进行熔化,直到剩余的银饰数量不足三块为止。
4.在每次循环中,从银饰重量列表中选择最重的三块银饰,并将其分别赋值给变量Z、y、X。
5.根据题目描述,我们需要移除这三块银饰。可以通过使用列表切片的方式将这三块银饰从银饰重
量列表中移除。切片操作将返回一个新的列表,其中包含从索引3开开始到列表末尾的所有元素。
6.然后,我们需要根据题目的规则判断这三块银饰是否需要重新添加到银饰重量列表中。
7.首先,判断x、y、z是否完全相等。如果相等,说明这三块银饰者都可以被熔化掉,不需要重新添加
到列表中。
8.如果x、y、z不完全相等,我们需要根据题目的规则选择要添加回回列表的银饰。
。如果x和y相等,则z-y无法被熔化掉,所以我们将z-y添加回银饰重重量列表中。
如果y和z相等,则y-x无法被熔化掉,所以我们将y-x添加回银饰重重量列表中。
。如果x、y、z三者都不相等,则z-y和y-x的差值无法被熔化掉,所以我们将|z-y-(y-x)」的结果添
加回银饰重量列表中。
9.完成一次循环后,重新对银饰重量列表进行排序,以便下次循环时选择最重的三块银饰。
10.当剩余的银饰数量不足三块时,跳出循环。
11.最后,根据剩余的银饰数量返回结果。如果剩余两块银饰,返回最大值;如果只剩一块银饰,返
回该值;如果没有剩余银饰,返回
"""


import java.util.*;

public class Main {

    public static void main(String[] args) {
        // 读取输入数据
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // 银饰的数量
        List<Integer> silverWeights = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            silverWeights.add(scanner.nextInt()); // 读取每个银饰的重量
        }
        scanner.close();

        // 调用函数并打印结果
        int result = meltSilver(silverWeights);
        System.out.println(result);
    }

    public static int meltSilver(List<Integer> silverWeights) {
        // 排序银饰数组，使得我们可以每次选择最重的三块
        Collections.sort(silverWeights, Collections.reverseOrder());

        while (silverWeights.size() > 2) {
            // 选出最重的三块
            int z = silverWeights.get(0);
            int y = silverWeights.get(1);
            int x = silverWeights.get(2);
            // 根据题目描述，移除这三块银饰
            silverWeights = silverWeights.subList(3, silverWeights.size());

            // 如果x、y、z不完全相等，我们需要将剩余的银块按照题目的规则添加回数组
            if (x != y || y != z) {
                if (x == y) {  // 如果 x 和 y 相等，则 z - y 无法被熔掉
                    silverWeights.add(z - y);
                } else if (y == z) {  // 如果 y 和 z 相等，则 y - x 无法被熔掉
                    silverWeights.add(y - x);
                } else {  // 如果三者都不相等，z - y 与 y - x 的差无法被熔掉
                    silverWeights.add(Math.abs((z - y) - (y - x)));
                }
            }

            // 重新排序银饰数组，以便下次迭代选择最重的三块
            Collections.sort(silverWeights, Collections.reverseOrder());
        }

        // 按照题目的要求返回剩余的银饰
        if (silverWeights.size() == 2) {
            return Math.max(silverWeights.get(0), silverWeights.get(1));
        } else if (silverWeights.size() == 1) {
            return silverWeights.get(0);
        } else {
            return 0;
        }
    }
}
