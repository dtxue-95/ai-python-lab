# Lambda 匿名函数
# lambda 是一种一次性的小函数，不需要用 def 定义，也不需要名字。
# 基本语法

# 普通函数
def square(num):
    return num ** 2
# 等价写法
square = lambda num: num ** 2
print(square(3))

# 语法：`lambda 参数: 表达式`

# 一个参数的
double = lambda num: num * 2
print(double(3))

# 多个参数
add = lambda num1, num2: num1 + num2
print(add(1, 2))

# 带条件的
size_label = lambda hours:"大型任务" if hours >=  8 else "小型任务"
print(size_label(8))
print(size_label(3))


# lambda 的主要用途


# 场景：按特定规则排序
# lambda 最常见的用法是作为参数传给其他函数
# lambda 只能写一个表达式，不能写多行代码
tasks = [
    {"name":"小明","age":18},
    {"name": "小亮", "age": 20},
    {"name": "小红", "age": 19},
    {"name": "小白", "age": 5},
]

# 按年龄排序
tasks.sort(key=lambda x: x["age"])
print(tasks)
print([task["name"] for task in tasks])

# 按年龄降序
tasks.sort(key=lambda x: x["age"], reverse=True)
print(tasks)
print([task["age"] for task in tasks])
