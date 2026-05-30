# 方式 1：手动打开和关闭（不推荐）
# file = open("hello.txt", "w", encoding="utf-8")
# file.write("你好，世界！\n")
# file.write("测试写入文件内容\n")
# file.close()  # 别忘了关闭文件！

# 方式 2：使用 with 语句（推荐！）
# with open("autoClose.txt", "w", encoding="utf-8") as file:
#     file.write("你好，世界！\n")
#     file.write("我正在学习 Python 文件操作。\n")
# # 离开 with 块时，文件自动关闭，不需要手动 close()

# 读取文件
# 读取全部内容
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 逐行读取
with open("hello.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip() 去掉行尾的换行符

# 读取所有行到列表
with open("hello.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)  # ['你好，世界！\n', '我正在学习 Python 文件操作。\n']

# 追加内容

# "a" 模式：在文件末尾追加，不会覆盖原有内容
with open("hello.txt", "a", encoding="utf-8") as file:
    file.write("2026-02-09: 开始学习\n")
    file.write("2026-02-09: 完成第一章\n")

# 写入多行
lines = ["第一行\n", "第二行\n", "第三行\n"]

with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)  # 写入一个字符串列表

# 或者用 print 写入文件
with open("output.txt", "w", encoding="utf-8") as file:
    print("第一行", file=file)  # print 可以指定输出到文件
    print("第二行", file=file)
    print("第三行", file=file)