# import time
# # 不用装饰器的做法：每个函数都要加计时器
# def train_model():
#     start = time.time()
#     # 这里模拟一次训练循环，真实项目里可以替换成模型训练代码
#     epochs = 3
#     for epoch in range(epochs):
#         time.sleep(0.25)
#         print(f"第 {epoch + 1}/{epochs} 轮：训练中...")
#     time.sleep(1)
#     end = time.time()
#     print(f"train_model 耗时：{end - start:.2f}s")
# def process_data():
#     start = time.time()
#     # 这里模拟一次数据预处理流程
#     records = ["原始1", "原始2", "原始3"]
#     cleaned = [record.replace("原始", "清洗后") for record in records]
#     print("清洗结果:", cleaned)
#     time.sleep(0.5)
#     end = time.time()
#     print(f"process_data 耗时: {end - start:.2f}秒")
#


# 装饰器解决方案
import time
def timer(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱ {func.__name__} 耗时: {end - start:.2f}秒")
        return result
    return wrapper
# 用 @ 语法使用装饰器
@timer
def train_model():
    """训练模型"""
    time.sleep(1)
    print("训练完成")

@timer
def process_data(filename):
    """处理数据"""
    time.sleep(0.5)
    print(f"处理 {filename} 完成！")

train_model()

process_data("data.csv")


# @timer 等价于 train_model = timer(train_model)。


# 常用的装饰器模式

# 重试装饰器
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第 {attempt} 次尝试失败: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def risky_operation():
    import random
    if random.random() < 0.7:
        raise ConnectionError("连接失败")
    return "成功！"
risky_operation()


