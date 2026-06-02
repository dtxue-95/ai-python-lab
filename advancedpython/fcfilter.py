# filter(函数, 可迭代对象) 保留函数返回 True 的元素。
numbers = [1,2,3,4,5,6,7,8,9,10]

# 筛选偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
# 筛选奇数
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)

# 等价的列表推导式
evenseq = [x for x in numbers if x % 2 == 0]
print(evenseq)

# filter()实际应用

# 筛选较慢的响应
lat_ms = [45, 78, 55, 920, 880, 30, 67, 1000]
slow = list(filter(lambda ms:ms >= 800, lat_ms))
print(slow)

# 筛选非空字符串
data = ["hello", "", "world", "", "python", ""]
non_empty = list(filter(None, data))
print(non_empty)

# 筛选特定类型的文件
files = ["data.csv", "model.py", "readme.md", "train.py", "config.json"]
py_files = list(filter(lambda f: f.endswith(".py"), files))
print(py_files)