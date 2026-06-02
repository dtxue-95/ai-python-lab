# 函数可以赋值给变量
def greet(name):
    return f"你好，{name}！"

say_hi = greet   # 把函数赋值给变量（注意没有括号）
print(say_hi("小明"))  # 你好，小明！

# 函数可以放进列表
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

operations = [add, sub, mul]
for op in operations:
    print(op(10, 3))  # 13, 7, 30