# try / except 基本用法
try:
    number = int(input("请输入一个数字："))
    print(f"你输入的是：{number}")
except ValueError:
    print("输入无效！请输入一个数字")

print("测试是否会继续往下执行")

# 捕获多种异常
def sage_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为0")
        return None
    except TypeError:
        print("错误：请传入数字")
        return None
print(sage_divide(4, 5))
print(sage_divide(4, 0))
print(sage_divide("jiuyu", 1))

# 捕获多种异常（合并写法）
try:
    # 可能出错的代码
    value = int(input("请输入数字："))
    result = 100 / value
    print(f"这是结果：{result}")
except (ValueError, ZeroDivisionError) as e:
    print(f"异常类型：{type(e).__name__}")
    print(f"异常信息：{e}")

# 捕获所有异常（谨慎使用）
try:
    # 业务代码
    result = risky_operation()
except Exception as e:
    print(f"错误{type(e).__name__}：{e}")


# try / except / else / finally
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
    # 不管有没有出错都执行（通常用来清理资源）
    print("操作完成")


# finally的典型用途
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

# 抛出异常
# raise语句
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

# 自定义异常
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