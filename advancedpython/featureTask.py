# 面向对象编程的思路是：把数据和操作打包在一起，形成一个”对象”。

class FeatureTask:
    def __init__(self,name,owner,hours):
        self.name = name
        self.owner = owner
        self.hours = hours

    def total_hours(self):
        return sum(self.hours)

# 创建功能任务对象
task1 = FeatureTask("login API","九余",[1,2,3])
task2 = FeatureTask("RAG action", 'jiuyu',[4,5,6])
# 数据和操作绑在一起，使用起来更自然
print(f"{task1.name}, 总工时：{task1.total_hours():.1f}")
print(f"{task2.name},总工时：{task2.total_hours():.1f}")