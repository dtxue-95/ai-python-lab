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

