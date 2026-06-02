# map()：对每个元素做同样的操作
# map(函数, 可迭代对象) 对序列中的每个元素应用函数，返回新的序列。

# 把列表中的每个数字平方
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

# 1 使用for循环
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)

# 2 使用map
squares = list(map(lambda x: x**2, numbers))
print(squares)

# 3 使用列表推导式
squares = [n**2 for n in numbers]
print(squares)


# map()实际应用

# 批量转换数据类型
str_numbers = [str(n) for n in numbers]
print(str_numbers)

num_numbers = list(map(int, str_numbers))
print(num_numbers)

# 批量处理字符串
names = ["  test   ", "   test1", "test2   "]
clean_names = list(map(str.strip, names))
print(clean_names)

# 使用已有函数
tem_c = [0,37,100]
def c_to_f(num):
    return num * 9/5 + 32
tem_f = list(map(c_to_f, tem_c))
print(tem_f)

