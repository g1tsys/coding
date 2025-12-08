"""
### Question Translation:

Implement a software to simulate directory management functionality. Given a sequence of commands, output the result of the last command executed.

**Supported Commands:**

1. **mkdir directory_name**: Creates a directory with the given name in the current directory. If the directory already exists, no action is taken. This command has no output.
2. **cd directory_name**: Changes the current directory to the specified directory. If `cd ..` is used, it returns to the parent directory. If the directory does not exist, no action is taken. This command has no output.
3. **pwd**: Outputs the current directory path as a string.

**Constraints:**

- Directory names only support lowercase letters.
- No nested or absolute paths are supported.
- The directory separator is `/`, and the root directory is `/`.
- Any invalid command is ignored and has no output.

**Input/Output:**

- **Input:** The first line is an integer `N`, followed by `N` lines of command strings.
- **Output:** Output the result of the last command executed.

---

### Python Solution Chain of Thoughts

1. **Define a Class `DirectoryManager`:**
   - This class will manage the directory structure and current path.
   - Members:
     - `root`: The root directory path (`/`).
     - `current_path`: The current working directory path.
     - `dirs`: A dictionary to store the directory structure. Keys are full paths, and values are sets of subdirectories.

2. **Implement `mkdir` Method:**
   - Takes a directory name as input.
   - Concatenates the current path and the new directory name to form the full path.
   - If the full path is not in the `dirs` dictionary, add it and create an entry in the dictionary.

3. **Implement `cd` Method:**
   - Takes a directory name as input.
   - If the input is `..`, move up one level by removing the last directory from the `current_path`.
   - Otherwise, concatenate the current path with the new directory name and check if it exists in `dirs`. If it does, update `current_path`.

4. **Implement `pwd` Method:**
   - Simply returns the `current_path`.

5. **Implement `run_command` Method:**
   - Parses the command and executes the appropriate method (`mkdir`, `cd`, or `pwd`).
   - Returns the output of the command (only `pwd` returns a value).

6. **Main Function:**
   - Read the number of commands `N`.
   - Read each command and execute it using `run_command`.
   - Keep track of the last output.
   - Finally, print the last output.

---

### Example Walkthrough

**Input:**

4
mkdir a
cd a
pwd
cd ..


**Step-by-Step Execution:**

1. **`mkdir a`**:
   - Current path is `/`.
   - New directory path is `/a`.
   - Since it doesn't exist, it is created.

2. **`cd a`**:
   - Current path is now `/a`.

3. **`pwd`**:
   - Output is `/a`.

4. **`cd ..`**:
   - Current path is now `/`.

**Final Output:**

/a


This is the result of the last command (`pwd`).

"""

class DirectoryManager:
    def __init__(self):
        # 初始化根目录
        self.root = '/'
        # 当前目录，默认是根目录
        self.current_path = self.root
        # 维护一个字典，用于存储每个目录下的子目录集合
        self.dirs = {self.root: set()}

    def mkdir(self, dir_name):
        """
        创建目录
        :param dir_name: 要创建的目录名称
        """
        # 拼接当前路径和新目录名称，作为新目录的完整路径
        new_path = self.current_path + dir_name + '/'
        # 如果目录不存在，则在当前路径下创建新目录
        if new_path not in self.dirs:
            # 在当前目录下添加新目录
            self.dirs[self.current_path].add(dir_name)
            # 初始化新目录的子目录集合
            self.dirs[new_path] = set()

    def cd(self, dir_name):
        """
        进入目录
        :param dir_name: 要进入的目录名称
        """
        if dir_name == '..':
            # 返回上级目录，如果当前已经是根目录，则保持不变
            if self.current_path != self.root:
                # 去掉最后的一个目录名称和斜杠，返回上级目录
                self.current_path = '/'.join(self.current_path.rstrip('/').split('/')[:-1]) + '/'
        else:
            # 拼接当前路径和目录名称，进入下一级目录
            new_path = self.current_path + dir_name + '/'
            # 如果目录存在，则进入目录
            if new_path in self.dirs:
                self.current_path = new_path

    def pwd(self):
        """
        输出当前路径
        :return: 当前路径字符串
        """
        return self.current_path

    def run_command(self, command):
        """
        执行命令
        :param command: 输入的命令字符串
        """
        # 切分命令和参数
        parts = command.split()
        if not parts:
            return None
        cmd = parts[0]
        # 根据不同的命令执行相应的操作
        if cmd == 'mkdir' and len(parts) == 2:
            self.mkdir(parts[1])
        elif cmd == 'cd' and len(parts) == 2:
            self.cd(parts[1])
        elif cmd == 'pwd':
            return self.pwd()
        else:
            # 无效命令，不执行任何操作
            return None

# 主函数
def main():
    # 实例化目录管理器
    manager = DirectoryManager()
    # 读取命令行数N
    N = int(input())
    # 用于存储最后的输出结果
    last_output = None
    # 读取并执行N行命令
    for _ in range(N):
        # 读取一行命令
        command = input().strip()
        # 执行命令，并获取可能的输出
        output = manager.run_command(command)
        # 如果有输出，则记录最后一条命令的输出
        if output is not None:
            last_output = output

    # 输出最后一条命令的结果
    print(last_output)

# 调用主函数
if __name__ == '__main__':
    main()

