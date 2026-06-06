# 简单项目练习——命令行任务管理器


# 基础版
from datetime import datetime
import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks() -> list[dict]:
    """从文件加载任务"""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                tasks = json.load(f)
            print(f"📂 已加载 {len(tasks)} 个任务")
            return tasks
        except (json.JSONDecodeError, IOError) as e:
            print(f"⚠️ 加载数据失败: {e}，将使用空列表")
    return []


def save_tasks(tasks: list[dict]) -> None:
    """保存任务到文件"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"⚠️ 保存数据失败: {e}")


def show_menu():
    """显示菜单"""
    print("\n===== 任务管理器 =====")
    print("1. 查看所有任务")
    print("2. 添加任务")
    print("3. 完成任务")
    print("4. 删除任务")
    print("5. 退出")
    print()


def show_tasks(tasks:list[dict]) -> None:
    """显示所有任务"""
    if not tasks:
        print("📭 暂无任务，快去添加一个吧！")
        return


    print("\n📋 任务列表")
    for i, task in enumerate(tasks,1):
        status = "✅" if task["done"] else " "
        print(f' {i}. [{status}] {task["title"]} '
              f'(创建于:{task["created_at"][:10]})')

    done_count = sum(1 for t in tasks if t["done"])
    print(f"\n共 {len(tasks)} 个任务，已完成 {done_count} 个")


def add_task(tasks: list[dict]) -> None:
    """添加新任务"""
    title = input("请输入任务标题: ").strip()
    if not title:
        print("❌ 任务标题不能为空！")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    print(f"✅ 任务「{title}」已添加！")


def complete_task(tasks: list[dict]) -> None:
    """标记任务为完成"""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("请输入要完成的任务编号: "))
        if 1 <= num <= len(tasks):
            task = tasks[num - 1]
            if task["done"]:
                print(f"⚠️ 任务「{task['title']}」已经完成过了")
            else:
                task["done"] = True
                print(f"✅ 任务「{task['title']}」已标记为完成！")
        else:
            print("❌ 无效的任务编号！")
    except ValueError:
        print("❌ 请输入数字！")


def delete_task(tasks: list[dict]) -> None:
    """删除任务"""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("请输入要删除的任务编号: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ 任务「{removed['title']}」已删除！")
        else:
            print("❌ 无效的任务编号！")
    except ValueError:
        print("❌ 请输入数字！")


# def main():
#     """主函数"""
#     tasks = []
#
#     print("欢迎使用任务管理器！")
#
#     while True:
#         show_menu()
#         choice = input("请选择操作 (1-5): ").strip()
#
#         if choice == "1":
#             show_tasks(tasks)
#         elif choice == "2":
#             add_task(tasks)
#         elif choice == "3":
#             complete_task(tasks)
#         elif choice == "4":
#             delete_task(tasks)
#         elif choice == "5":
#             print("👋 再见！")
#             break
#         else:
#             print("❌ 无效的选择，请输入 1-5")

def main():
    tasks = load_tasks()  # 启动时加载

    print("欢迎使用任务管理器！")

    while True:
        show_menu()
        choice = input("请选择操作 (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)  # 添加后保存
        elif choice == "3":
            complete_task(tasks)
            save_tasks(tasks)  # 修改后保存
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)  # 删除后保存
        elif choice == "5":
            save_tasks(tasks)  # 退出前保存
            print("👋 再见！")
            break
        else:
            print("❌ 无效的选择，请输入 1-5")


if __name__ == "__main__":
    main()