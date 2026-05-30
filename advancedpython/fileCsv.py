# csv文件
import csv

# 写入 CSV
tasks = [
    ["功能", "负责人", "工时"],
    ["登录 API", "Mina", 8],
    ["RAG 演示", "Kai", 12],
    ["图表视图", "Noah", 5],
]

with open("tasks.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(tasks)

# 读取 CSV
with open("tasks.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # 读取表头
    print(f"列名: {header}")

    for row in reader:
        feature, owner, hours = row
        print(f"{feature}, 负责人: {owner}, 估算: {hours} 小时")

# 用字典方式读取（更方便）
with open("tasks.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['功能']} 由 {row['负责人']} 负责")