# sorted() 的 key 参数
# sorted() 的 key 参数让你自定义排序规则：
#


# 按绝对值排序
nums = [-5, 3, -1, 4, -2]
res = sorted(nums,key=abs)
print(res)

# 按字符串长度排序
words = ["one", "two", "three", "four", "five"]
res = sorted(words,key=len)
print(res)

# 按字典的某个键排序
tasks = [
    {"name": "登录 API", "owner_count": 2, "hours": 8},
    {"name": "RAG 演示", "owner_count": 1, "hours": 12},
    {"name": "图表视图", "owner_count": 1, "hours": 5},
]

# 按预估小时排序
by_hours = sorted(tasks, key=lambda x: x["hours"], reverse=True)
for x in by_hours:
        print(x["name"], x["owner_count"], x["hours"])

# 按多个条件排序
tasks2 = [
    {"name": "A", "priority": 2, "hours": 8},
    {"name": "B", "priority": 2, "hours": 5},
    {"name": "C", "priority": 3, "hours": 12},
]

res = sorted(tasks2, key=lambda task:(-task["hours"], task["name"], task["priority"]))
for task in res:
    print(task["name"], task["priority"], task["hours"])