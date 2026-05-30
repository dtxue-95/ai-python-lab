from pathlib import Path

# 创建路径对象
data_dir = Path("data")
train_file = data_dir / "train" / "data.csv"  # 用 / 拼接路径！
print(train_file)  # data/train/data.csv

# 检查路径
print(train_file.exists())    # 文件是否存在
print(train_file.is_file())   # 是否是文件
print(data_dir.is_dir())      # 是否是目录

# 获取文件信息
path = Path("model.pth")
print(path.name)       # model.pth（文件名）
print(path.stem)       # model（不带扩展名）
print(path.suffix)     # .pth（扩展名）
print(path.parent)     # .（父目录）

# 创建目录
Path("output/results").mkdir(parents=True, exist_ok=True)

# 列出目录中的文件
for file in Path(".").glob("*.py"):
    print(file)

# 递归查找所有 CSV 文件
for csv_file in Path("data").rglob("*.csv"):
    print(csv_file)

# 读写文件的便捷方法
Path("note.txt").write_text("Hello!", encoding="utf-8")
content = Path("note.txt").read_text(encoding="utf-8")
print(content)  # Hello!