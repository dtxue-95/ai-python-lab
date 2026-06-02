# 闭包（Closure）
# 闭包是一个函数，它记住了外层函数的变量，即使外层函数已经执行完毕。
from advancedpython.fc匿名函数lambda import double


def mk_mul(factor):
    """创建一个乘法器"""
    def mul(n):
        return n * factor
    return mul
double = mk_mul(2)
print(double(3))

triple = mk_mul(3)
print(triple(5))


# 闭包的实际应用

# 创建计数器
def mk_count(start=0):
    count = [start]
    def counter():
        count[0] += 1
        return count[0]
    return counter

counter = mk_count()
print(counter())
print(counter())
print(counter())


# 创建带前缀的日志函数
def make_logger(prefix):
    def log(message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{prefix}] {timestamp} {message}")
    return log

info = make_logger("INFO")
error = make_logger("ERROR")

info("程序启动")      # [INFO] 14:30:01 程序启动
error("文件未找到")   # [ERROR] 14:30:01 文件未找到