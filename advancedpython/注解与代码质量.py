# 变量注解

# 基本类型
name:str = "九余"
count:int = 99
count_float: float = 3.14
is_self:bool = False
print(type(name),name)
print(type(count),count)
print(type(count_float),count_float)

# Python 不会强制检查类型注解
# 以下代码不会报错，但静态检查工具会警告
retry_count: int = "三次"  # 类型注解说是 int，实际赋了 str


# 函数注解

def greet(name: str) -> str:
    """
    name: str  → 参数 name 的类型是 str
    -> str     → 返回值的类型是 str
    """
    return f"你好，{name}！"

def calculate_bmi(weight: float, height: float) -> float:
    """计算 BMI"""
    return weight / (height ** 2)

def train_model(epochs: int = 10, lr: float = 0.001) -> None:
    """返回 None 的函数"""
    print(f"训练 {epochs} 轮，学习率 {lr}")

# 复合类型注释
# 列表和字段
# Python 3.9+：直接用内置类型
estimated_hours: list[int] = [8, 12, 5]
task_hours: dict[str, int] = {"登录 API": 8, "RAG 演示": 12}
coordinates: tuple[float, float] = (3.14, 2.71)
unique_ids: set[int] = {1, 2, 3}

# Python 3.8 及更早：需要从 typing 导入
from typing import List, Dict, Tuple, Set

estimated_hours: List[int] = [8, 12, 5]
task_hours: Dict[str, int] = {"登录 API": 8, "RAG 演示": 12}

# Optional：可能为 None 的值

from typing import Optional

def find_task(name: str) -> Optional[dict]:
    """查找任务，找不到返回 None"""
    tasks = {"登录 API": {"hours": 8}, "RAG 演示": {"hours": 12}}
    return tasks.get(name)

# Python 3.10+ 可以用更简洁的写法
def find_task(name: str) -> dict | None:
    tasks = {"登录 API": {"hours": 8}, "RAG 演示": {"hours": 12}}
    return tasks.get(name)


# Union：多种可能的类型
from typing import Union

def process(data: Union[str, list]) -> str:
    """接受字符串或列表"""
    if isinstance(data, list):
        return ", ".join(str(item) for item in data)
    return data

# Python 3.10+ 的简洁写法
def process(data: str | list) -> str:
    if isinstance(data, list):
        return ", ".join(str(item) for item in data)
    return data


# Callable：函数类型
from typing import Callable

def apply_func(func: Callable[[int, int], int], a: int, b: int) -> int:
    """接受一个函数作为参数"""
    return func(a, b)

result = apply_func(lambda x, y: x + y, 3, 5)  # 8


# 更多类型的注解
from typing import Any, Literal

# Any：任意类型
def log(message: Any) -> None:
    print(message)

# Literal：只接受特定的值
def set_mode(mode: Literal["train", "eval", "test"]) -> None:
    print(f"模式: {mode}")

set_mode("train")   # ✅
set_mode("play")    # 静态检查会警告