# 综合案例：任务日志持久化系统
import json
from pathlib import Path

class TaskLog:
    """任务工作日志，支持文件持久化"""

    def __init__(self, filename="task_log.json"):
        self.filename = Path(filename)
        self.tasks = {}
        self.load()  # 启动时加载数据

    def load(self):
        """从文件加载数据"""
        if self.filename.exists():
            with open(self.filename, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
            print(f"✅ 已加载 {len(self.tasks)} 个任务的数据")
        else:
            print("📝 创建新的任务日志")

    def save(self):
        """保存数据到文件"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def add_work(self, task_name, stage, hours):
        """添加工作时长"""
        if task_name not in self.tasks:
            self.tasks[task_name] = {}
        self.tasks[task_name][stage] = hours
        self.save()
        print(f"✅ {task_name} 的 {stage} 工时（{hours} 小时）已保存")

    def get_report(self, task_name):
        """获取任务报告"""
        if task_name not in self.tasks:
            print(f"❌ 找不到任务: {task_name}")
            return

        stages = self.tasks[task_name]
        print(f"\n{'='*30}")
        print(f"  {task_name} 的工作报告")
        print(f"{'='*30}")
        for stage, hours in stages.items():
            print(f"  {stage}: {hours} 小时")
        total = sum(stages.values())
        print(f"{'─'*30}")
        print(f"  总工时: {total:.1f}")
        print(f"{'='*30}")

    def export_csv(self, filename="task_hours.csv"):
        """导出为 CSV"""
        import csv
        stages = set()
        for task_stages in self.tasks.values():
            stages.update(task_stages.keys())
        stages = sorted(stages)

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["任务"] + stages)
            for task_name, task_stages in self.tasks.items():
                row = [task_name] + [task_stages.get(s, "") for s in stages]
                writer.writerow(row)
        print(f"✅ 已导出到 {filename}")

# 使用
log = TaskLog()
log.add_work("登录 API", "设计", 2)
log.add_work("登录 API", "实现", 5)
log.add_work("登录 API", "测试", 1)
log.add_work("RAG 演示", "实现", 7)
log.add_work("RAG 演示", "文档", 2)
log.get_report("登录 API")
log.export_csv()