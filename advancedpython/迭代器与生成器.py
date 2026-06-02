# 手动迭代
nums = [1, 2, 3]

# for 循环写法
for num in nums:
    print(num)

# 等价手动写法
# 1 获取迭代器
# iterator = iter(nums)
# # 2 获取下一个元素
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # 没有更多元素了 → 抛出 StopIteration
# print(next(iterator))

# 迭代器协议：
#
# iter(对象) → 获取迭代器
# next(迭代器) → 获取下一个元素
# 元素用完时抛出 StopIteration 异常


# 自定义迭代器
class Countdown:
    """倒计时迭代器"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self # 返回自身作为迭代器

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# 使用
for num in Countdown(10):
    print(num, end=" ")


# 生成器函数 generator
# 生成器是一种特殊的迭代器，用 yield 关键字代替 return。

# 基本用法
def testCount(n):
    while n > 0:
        yield n # 暂停， 返回n, 下次从这里继续
        n -= 1
for n in testCount(6):
    print(n, end=" ")


# return：函数执行完毕，一次性返回所有结果
def get_squares_return(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# yield：每次返回一个结果，暂停等待下次调用
def get_squares_yield(n):
    for i in range(n):
        yield i ** 2

# 使用效果一样
print(list(get_squares_return(5)))  # [0, 1, 4, 9, 16]
print(list(get_squares_yield(5)))   # [0, 1, 4, 9, 16]


# 生成器执行过程

def simple_gen():
    print("第一步")
    yield 1
    print("第二步")
    yield 2
    print("第三步")
    yield 3
    print("结束")

gen = simple_gen()   # 创建生成器，但不执行任何代码

print(next(gen))     # 执行到第一个 yield，打印"第一步"，返回 1
print(next(gen))     # 从上次暂停处继续，打印"第二步"，返回 2
print(next(gen))     # 打印"第三步"，返回 3
# next(gen)          # 打印"结束"，然后抛出 StopIteration