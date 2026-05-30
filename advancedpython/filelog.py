from datetime import datetime

def log(message, filename="app.log"):
    """写入日志"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

# 使用
log("程序启动")
log("加载数据集: train.csv")
log("开始训练模型")
log("训练完成，准确率: 92.5%")