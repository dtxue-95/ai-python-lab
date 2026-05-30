import pickle

# 保存 Python 对象
data = {
    "hours": [2, 5, 1, 3],
    "features": ["登录 API", "RAG 演示", "图表视图", "部署脚本"],
    "metadata": {"module": "portfolio backend", "year": 2026}
}

with open("data.pkl", "wb") as file:  # 注意是 "wb"（二进制写入）
    pickle.dump(data, file)

# 加载 Python 对象
with open("data.pkl", "rb") as file:  # 注意是 "rb"（二进制读取）
    loaded_data = pickle.load(file)

print(loaded_data["features"])  # ['登录 API', 'RAG 演示', '图表视图', '部署脚本']