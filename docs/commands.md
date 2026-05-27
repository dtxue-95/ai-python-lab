# 打印当前工作目录
- pwd
# 绝对路径和相对路径
## 路径中的特殊符号

| 符号 | 含义 | 例子   |
|----|----|------|
| /  | 根目录（所有文件的起点）   | cd/  |
| ～  | 当前用户的主目录（Home）   | cd ~ 等于 cd /Users/zhangsan   |
| .  | 当前目录   | ./run.py 表示当前目录下的 run.py | 
| .. | 上一级目录   | cd .. 回到上一层 |
# 核心命令
## 导航命令
- cd - 切换目录

    `cd projects` 进入 projects 文件夹

    `cd ..` 回到上级一

    `cd ~` 回到 Home 目录

    `cd ~/Desktop` 去桌面

    `cd -` 回到上一次所在的目录
- ls - 列出文件

    `ls` 列出当前目录下的文件和文件夹

    `ls -l` 详细列表（显示大小、日期、权限）

    `ls -a` 显示隐藏文件（以. 开头的文件）

    `ls -la` 两者结合

    `ls ai-learning-lab` 列出 ai-learning-lab 文件夹里的内容


## 文件和文件夹操作
- mkdir - 创建文件夹
    
    `mkdir test` 创建一个test文件夹

    `mkdir -p a/b/c` 一次性创建多层嵌套的文件夹
- touch - 创建空文件

    `touch test.py` 创建一个空的python文件
    
    `touch README.md` 创建一个空的markdown文件

- cp - 复制
    
    `cp file.txt file_backup.txt` 复制文件

    `cp file.txt ~/Desktop/` 复制到桌面

    `cp -r my-folder/my-folder-backup/` 复制整个文件夹（-r 表示递归）
- mv - 移动/重命名
    
    `mv old_name.py new_name.py` 重命名文件

    `mv file.txt ~/Desktop/` 移动到桌面

    `mv project/ ~/projects/` 移动文件夹
- rm - 删除

    `rm file.txt` 删除文件

    `rm -r my-folder/` 删除文件及其所有内容
## 查看文件内容
- `cat file.txt` 显示整个文件内容（适合小文件）
- `head file.txt` 显示文件前10行
- `head -20 file.txt` 显示前20行
- `tail file.txt` 显示文件最后10行
- `tail -f log.txt` 实时跟踪文件更新（看日志时很有用）
## 搜索

`grep "error" log.txt` 在文件中搜索包含 “error”的行

`grep -r "import torch" ./` 在当前目录下所有文件中搜索

`grep -n "def train" model.py` 搜索并显示行号

## 其他命令
`clear`  清屏（或按 Ctrl + L）

`history` 查看你之前执行过的所有命令

`which python ` 查看 python 命令的路径（排查环境问题常用）

`echo "hello" ` 输出一段文字
# 管道与重定向
## 管道 ｜
`ls -la | grep ".py"` 列出所有文件，从中找到 .py 文件

`history | grep "git"` 查看历史命令中用过的 git 命令

`ls *.py | wc -l` 统计当前目录下有多少个 Python 文件
## 重定向 > 和 >> (主要的作用是把命令的输出保存到文件里)
` > 是覆盖，>> 是追加`

`ls -la > filelist.txt` 把 ls 的结果保存到 filelist.txt（覆盖写入）

`echo "新的一行" >> notes.txt`  把结果追加到文件末尾（不覆盖）

`python train.py > training_log.txt` 把 Python 脚本的输出保存到文件

`python train.py > log.txt 2>&1` 运行脚本，把正常输出和错误输出都保存到日志文件

`cat model.py | wc -l` 统计一个 Python 文件有多少行代码

`grep -r "TODO" ./ | wc -l`  找到所有包含 "TODO" 的文件，并统计数量
# 环境变量
##  查看环境变量
`env` 查看所有环境变量
查看某一个环境变量的值
`echo $PATH`
`echo $HOME`
## 最重要的环境变量：PATH
- PATH 决定了你在终端里输入一个命令时，系统去哪些目录里找这个命令
- 这些路径用 : 分隔。当你输入 python 时，系统会依次在这些目录里找 python 这个文件，找到第一个就执行。
- 如果你遇到 command not found（命令找不到），通常就是因为这个程序没在 PATH 的任何目录里。

## 设置环境变量

临时设置（只在当前终端窗口有效）
`export MY_API_KEY="your_api_key_here"`
`echo $MY_API_KEY`    # 输出: your_api_key_here

验证：关闭终端重新打开，MY_API_KEY 就没了

- 永久设置（写入配置文件） macOS/Linux 用 zsh：
echo 'export MY_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc    # 立即生效

- 如果用 bash：
echo 'export MY_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc