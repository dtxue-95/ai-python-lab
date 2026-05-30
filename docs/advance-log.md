# 面向对象编程
## 类和对象的基本概念
```markdown
类：FeatureTask（功能任务的模板）
    └── 属性：name, owner, hours
    └── 方法：total_hours(), is_over_budget()

对象（实例）：
    └── task1 = FeatureTask("登录 API", "Mina", [2, 5, 1])
    └── task2 = FeatureTask("RAG 演示", "Kai", [3, 4, 2])
```

## 定义类
```python
class Dog:
    """一只狗"""

    def __init__(self, name, breed):
        """初始化方法，创建对象时自动调用"""
        self.name = name      # 实例属性
        self.breed = breed    # 实例属性

    def bark(self):
        """方法：狗叫"""
        print(f"{self.name} 说: 汪汪汪！")

    def info(self):
        """方法：显示信息"""
        print(f"名字: {self.name}, 品种: {self.breed}")

# 创建对象（实例化）
my_dog = Dog("旺财", "金毛")
your_dog = Dog("小黑", "拉布拉多")

# 访问属性
print(my_dog.name)     # 旺财
print(your_dog.breed)  # 拉布拉多

# 调用方法
my_dog.bark()      # 旺财 说: 汪汪汪！
your_dog.info()    # 名字: 小黑, 品种: 拉布拉多
```
## 关键点解读

- `__init__`方法（构造方法)
`__init__`在你创建对象时自动调用，用来初始化对象的属性
```markdown
my_dog = Dog("旺财", "金毛")
# Python 自动做了这些事：
# 1. 创建一个新的 Dog 对象
# 2. 调用 __init__(self, "旺财", "金毛")
# 3. self.name = "旺财"
# 4. self.breed = "金毛"
# 5. 返回这个对象给 my_dog
```
- `self`是什么？
`self`代表对象自己。当你调用 my_dog.bark() 时，Python 会自动把 my_dog 作为 self 传给 bark 方法
```markdown
my_dog.bark()
# 等价于
Dog.bark(my_dog)
```
## 属性和方法
### 实例属性vs类属性
```python
class FeatureTask:
    # 类属性：所有实例共享
    project = "AI 作品集"
    task_count = 0

    def __init__(self, name, owner):
        # 实例属性：每个实例独有
        self.name = name
        self.owner = owner
        FeatureTask.task_count += 1  # 每创建一个任务，计数加 1

t1 = FeatureTask("登录 API", "Mina")
t2 = FeatureTask("RAG 演示", "Kai")

# 类属性通过类名或实例都能访问
print(FeatureTask.project)     # AI 作品集
print(t1.project)              # AI 作品集
print(FeatureTask.task_count)  # 2

# 实例属性只属于各自的实例
print(t1.name)   # 登录 API
print(t2.owner)  # Kai
```
### 方法
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """计算面积"""
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        """计算周长"""
        return 2 * 3.14159 * self.radius

    def scale(self, factor):
        """缩放半径"""
        self.radius *= factor  # 修改属性

c = Circle(5)
print(f"面积: {c.area():.2f}")       # 78.54
print(f"周长: {c.perimeter():.2f}")   # 31.42

c.scale(2)  # 半径变为 10
print(f"缩放后面积: {c.area():.2f}") # 314.16
```
### 魔术方法（双下划线方法）
Python 中以 __ 开头和结尾的方法叫魔术方法（Magic Methods），它们让你的类可以像内置类型一样使用。
#### `__str__`定义 print 的输出
```python
class FeatureTask:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def __str__(self):
        return f"FeatureTask({self.name}, owner={self.owner})"

task = FeatureTask("登录 API", "Mina")
print(task)  # FeatureTask(登录 API, owner=Mina)
# 如果没有 __str__，print 会输出 <__main__.FeatureTask object at 0x...>
```
#### `__repr__`定义开发者看到的表示
```python
class FeatureTask:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def __repr__(self):
        return f"FeatureTask('{self.name}', '{self.owner}')"

task = FeatureTask("登录 API", "Mina")
print(repr(task))   # FeatureTask('登录 API', 'Mina')
# 在交互模式中直接输入 task 也会显示这个
```
#### `__len__`定义len()的行为
```python
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __len__(self):
        return len(self.songs)

my_playlist = Playlist("学习音乐", ["歌曲A", "歌曲B", "歌曲C"])
print(len(my_playlist))  # 3
```
#### `__eq__`定义==的行为
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)

print(p1 == p2)  # True
print(p1 == p3)  # False
```
## 继承
继承让你可以基于已有的类创建新类，复用代码。

### 基本继承
```python
# 父类（基类）
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} 发出了声音")

    def info(self):
        print(f"{self.name}, {self.age}岁")

# 子类（派生类）
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类的 __init__
        self.breed = breed

    def speak(self):  # 重写父类的方法
        print(f"{self.name} 说: 汪汪汪！")

    def fetch(self):  # 子类独有的方法
        print(f"{self.name} 把球捡回来了！")

class Cat(Animal):
    def speak(self):  # 重写父类的方法
        print(f"{self.name} 说: 喵喵喵～")

# 使用
dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2)

dog.info()     # 旺财, 3岁（继承自 Animal）
dog.speak()    # 旺财 说: 汪汪汪！（Dog 自己的实现）
dog.fetch()    # 旺财 把球捡回来了！（Dog 独有的）

cat.info()     # 咪咪, 2岁
cat.speak()    # 咪咪 说: 喵喵喵～
```
#### super()的作用
`super()`用来调用父类的方法，最常见的用法是在`__init__`中：
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # 让父类帮我初始化 name
        self.breed = breed       # 自己初始化 breed
```
#### isinstance()检查类型
```markdown
dog = Dog("旺财", 3, "金毛")

print(isinstance(dog, Dog))     # True —— 是 Dog
print(isinstance(dog, Animal))  # True —— 也是 Animal（因为继承）
print(isinstance(dog, Cat))     # False —— 不是 Cat
```
## 封装
封装的思想是：隐藏内部细节，只暴露必要的接口。

### 私有属性(约定)
Python 没有真正的私有属性，但有命名约定：

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # 单下划线：约定为"内部使用"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"存入 {amount} 元，余额: {self._balance}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"取出 {amount} 元，余额: {self._balance}")
        else:
            print("余额不足！")

    def get_balance(self):
        return self._balance

account = BankAccount("作品集账户", 1000)
account.deposit(500)     # 存入 500 元，余额: 1500
account.withdraw(200)    # 取出 200 元，余额: 1300
print(account.get_balance())  # 1300

# 虽然技术上可以直接访问 _balance，但这不是推荐的做法
# print(account._balance)  # 能用，但不应该这么做
```
| 命名约定   | 含义         | 示例            |
|--------|------------|---------------|
| name   | 公开属性       | self.name     |
| _name  | 内部使用（约定）   | self._balance |
| __name | 名称改写（强制隐藏） | self.__secret |
# 异常处理
## 常见的异常类型
| 异常类型                | 触发场景    | 示例                   |
|---------------------|---------|----------------------|
| `ZeroDivisonError`  | 除以0     | `1/0`                | 
| `TypeError`         | 类型操作不匹配 | `"test" + 9`         | 
| `ValueErro`         | 值不合法    | `int("hello")`       | 
| `IndexError`        | 列表索引越界  | `[1,2][5]`           | 
| `KeyError`          | 字典键不存在  | `{"a":1} ["b"]`      | 
| `FileNotFoundError` | 文件不存在   | `open("不存在的文件.txt")` | 
| `AttributeError`    | 属性不存在   | `"hello".foo()`      | 
| `NameError`         | 变量未定义   | `print(xyz)`         | 
| `ImportError`       | 导入失败    | `import 不存在的模块`      | 
## try/except 基本用法
- 关键点：有了 try/except，程序不会因为错误而崩溃。

`try/except` 的逻辑是：尝试执行代码，如果出错了，执行备选方案。
```markdown
try:
    number = int(input("请输入一个数字: "))
    print(f"你输入的是: {number}")
except ValueError:
    print("输入无效！请输入一个数字。")

print("程序继续运行...")  # 不管有没有异常，这行都会执行
```
## 捕获不同类型的异常
### 捕获多种异常
```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：不能除以零！")
        return None
    except TypeError:
        print("错误：请传入数字！")
        return None

print(safe_divide(10, 3))    # 3.333...
print(safe_divide(10, 0))    # 错误：不能除以零！ → None
print(safe_divide("10", 3))  # 错误：请传入数字！ → None
```
### 捕获多种异常的合并写法
```python
try:
    # 可能出错的代码
    value = int(input("请输入数字: "))
    result = 100 / value
    print(f"结果: {result}")
except (ValueError, ZeroDivisionError) as e:
    print(f"出错了: {e}")
```
### 获取异常信息
```python
try:
    number = int("abc")
except ValueError as e:
    print(f"异常类型: {type(e).__name__}")  # ValueError
    print(f"异常信息: {e}")                 # invalid literal for int() with base 10: 'abc'
```
### 捕获所有异常（谨慎使用）
```python
try:
    # 一些代码
    result = risky_operation()
except Exception as e:
    print(f"发生了意外错误: {type(e).__name__}: {e}")
```

```tips
不要滥用 except Exception

捕获所有异常听起来很方便，但会掩盖真正的 bug。你应该尽量捕获具体的异常类型，只在最外层使用 except Exception 作为兜底。
 
 # 不好的做法 ❌
try:
    do_something()
except:  # 捕获所有异常，包括 KeyboardInterrupt
    pass   # 而且还什么都不做！

# 好的做法 ✅
try:
    do_something()
except ValueError:
    handle_value_error()
except FileNotFoundError:
    handle_file_not_found()
except Exception as e:
    logging.error(f"未预期的错误: {e}")
```
## try / except / else / finally
完整的异常处理结构有四个部分:
```python
try:
    # 尝试执行的代码
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    # 出错时执行
    print("文件不存在！")
else:
    # 没有出错时执行
    print(f"文件内容: {content}")
finally:
    # 不管有没有出错都执行（清理资源（关闭文件、断开连接））
    print("操作完成")
```
## finally的典型用途
```python
file = None
try:
    file = open("data.txt", "r")
    data = file.read()
    # 处理数据...
except FileNotFoundError:
    print("文件不存在")
finally:
    if file:
        file.close()   # 不管有没有出错，都要关闭文件
        print("文件已关闭")
```
## 抛出异常
主动抛出异常——当你发现一个不合理的状态时，告诉调用者”出问题了”。
### raise 语句
```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0 or age > 150:
        raise ValueError(f"年龄 {age} 不合理，应该在 0-150 之间")
    return age

# 正常使用
print(set_age(25))      # 25

# 触发异常
try:
    set_age(-5)
except ValueError as e:
    print(f"错误: {e}")  # 错误: 年龄 -5 不合理，应该在 0-150 之间

try:
    set_age("二十")
except TypeError as e:
    print(f"错误: {e}")  # 错误: 年龄必须是整数
```
### 自定义异常
当内置异常类型不够用时，可以自定义：

```python
class InsufficientFundsError(Exception):
    """余额不足异常"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足：当前余额 {balance}，尝试取出 {amount}")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# 使用
account = BankAccount(1000)
try:
    account.withdraw(1500)
except InsufficientFundsError as e:
    print(f"交易失败: {e}")
    print(f"当前余额: {e.balance}, 请求金额: {e.amount}")
```
# 文件操作与序列化
## 为什么需要文件操作
到目前为止，你的程序中的数据都在内存中——程序一关，数据就没了。但在真实场景中：

训练好的 AI 模型需要保存到文件，下次直接加载
数据集存在 CSV 文件里，需要读取到程序中
训练日志需要写入文件，方便后续分析
配置参数存在 JSON 文件里，启动时需要加载
文件操作就是让你的程序能持久化保存数据。
## 文件读写基础
### 打开文件：open()
```python
file = open("文件路径", "模式", encoding="编码")
```
常用模式：

| 模式   | 含义          | 文件不存在时 |
|------|-------------|--------|
| `r`  | 读取 | 报错     |
| `w`  | 写入（覆盖） | 自动创建   |
| `a`  | 追加(在末尾添加)   | 自动创建   |
| `x`  | 创建(文件已存在则报错) | 自动创建   |
| `rb` | 读取二进制文件     | 报错     |
| `wb` | 写入二进制文件     | 自动创建   |

### 写入文件
```python
# 方式 1：手动打开和关闭（不推荐）
file = open("hello.txt", "w", encoding="utf-8")
file.write("你好，世界！\n")
file.write("我正在学习 Python 文件操作。\n")
file.close()  # 别忘了关闭文件！

# 方式 2：使用 with 语句（推荐！）
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("你好，世界！\n")
    file.write("我正在学习 Python 文件操作。\n")
# 离开 with 块时，文件自动关闭，不需要手动 close()
```
```
with 语句有两个好处：

自动关闭文件——不用担心忘记 close()
异常安全——即使代码出错，文件也会被正确关闭
以后写文件操作，永远用 with。
```
### 读取文件
```python
# 读取全部内容
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 逐行读取
with open("hello.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip() 去掉行尾的换行符

# 读取所有行到列表
with open("hello.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)  # ['你好，世界！\n', '我正在学习 Python 文件操作。\n']
```
### 追加内容
```python
# "a" 模式：在文件末尾追加，不会覆盖原有内容
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("2026-02-09: 开始学习\n")
    file.write("2026-02-09: 完成第一章\n")
```
### 写入多行
```python
lines = ["第一行\n", "第二行\n", "第三行\n"]

with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)  # 写入一个字符串列表

# 或者用 print 写入文件
with open("output.txt", "w", encoding="utf-8") as file:
    print("第一行", file=file)  # print 可以指定输出到文件
    print("第二行", file=file)
    print("第三行", file=file)
```
## 处理不同文件格式
### csv文件
```python
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
```
### Json文件
```python
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
```
### 文本日志文件
```python
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
```

### 路径处理：pathlib
pathlib 是 Python 3 推荐的路径处理方式，比 os.path 更现代、更好用：

```python
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
```
## 序列化：保存Python对象
### 什么是序列化？
序列化就是把 Python 对象（列表、字典、类实例等）转换成可以保存到文件的格式。反序列化就是反过来，从文件恢复成 Python 对象。

根据要保存的内容选择格式：

| 需求                     | 推荐格式                |
|------------------------|---------------------|
| 配置、API响应、小型结构化数据       | 用`json`模块保存JSON     |
| 行列形式的数据，需要能用表格软件打开     | 用`csv`模块保存CSV       |
| 只在Python内部使用、来源完全可信的对象 | 用`pickle`模块保存pickle |

这里最重要的取舍是安全性。JSON 和 CSV 可读、适合普通学习项目；pickle 很方便也很快，但它是二进制格式，而且不能加载来源不可信的文件。

### pickle:保存任意Python对象
```python
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
```