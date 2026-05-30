import json

# 写入 JSON
config = {
    "model": "ResNet-50",
    "learning_rate": 0.001,
    "epochs": 100,
    "batch_size": 32,
    "classes": ["猫", "狗", "鸟"],
    "use_gpu": True
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, ensure_ascii=False, indent=2)

# 读取 JSON
with open("config.json", "r", encoding="utf-8") as file:
    loaded_config = json.load(file)

print(f"模型: {loaded_config['model']}")
print(f"学习率: {loaded_config['learning_rate']}")
print(f"类别: {loaded_config['classes']}")