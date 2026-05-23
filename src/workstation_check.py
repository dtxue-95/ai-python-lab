# 用于兼容未来的Python语法特性，提升代码兼容性
from __future__ import annotations

# 导入所需工具库
import json          # 处理JSON格式数据
import platform      # 获取操作系统信息
import subprocess    # 执行系统命令（如git）
import sys           # 获取Python运行环境信息
from datetime import datetime, timedelta  # 处理时间
from pathlib import Path                 # 处理文件路径
from typing import Any                   # 类型注解

# -------------------------- 路径配置 --------------------------
# 获取项目根目录（当前文件向上两级）
PROJECT_ROOT = Path(__file__).resolve().parents[1]
# 报告存放目录
REPORTS_DIR = PROJECT_ROOT / "reports"
# 学习日志存放目录
NOTES_DIR = PROJECT_ROOT / "notes"
# JSON格式报告保存路径
JSON_REPORT = REPORTS_DIR / "workstation-check.json"
# Markdown格式报告保存路径
MARKDOWN_REPORT = REPORTS_DIR / "workstation-report.md"
# 学习日志保存路径
LEARNING_LOG = NOTES_DIR / "learning-log.md"

# -------------------------- 工具函数 --------------------------
def get_beijing_time() -> str:
    """获取【北京时间】（UTC+8），替换原来的UTC时间"""
    utc_now = datetime.utcnow()
    beijing_now = utc_now + timedelta(hours=8)
    return beijing_now.replace(microsecond=0).isoformat()

def run_command(command: list[str]) -> dict[str, Any]:
    """
    执行系统命令（如git指令）
    :param command: 命令列表，例如 ["git", "status"]
    :return: 命令执行结果（命令、返回码、输出、错误）
    """
    try:
        completed = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        # 命令不存在时返回错误信息
        return {
            "command": " ".join(command),
            "returncode": 127,
            "stdout": "",
            "stderr": f"{command[0]} 命令未找到",
        }
    # 返回命令执行结果
    return {
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }

def visible_project_files() -> list[str]:
    """获取项目中所有可见文件（排除.git目录和文件夹本身）"""
    files: list[str] = []
    for path in sorted(PROJECT_ROOT.rglob("*")):
        if ".git" in path.parts or path.is_dir():
            continue
        files.append(str(path.relative_to(PROJECT_ROOT)))
    return files

def ensure_workspace_files() -> None:
    """确保目录存在，并初始化学习日志文件"""
    # 创建报告目录（不存在则创建）
    REPORTS_DIR.mkdir(exist_ok=True)
    # 创建日志目录
    NOTES_DIR.mkdir(exist_ok=True)
    # 学习日志不存在则创建并写入表头
    if not LEARNING_LOG.exists():
        LEARNING_LOG.write_text(
            "# 学习日志\n\n| 时间 | 执行命令 | 结果 | 备注 |\n|---|---|---|---|\n",
            encoding="utf-8",
        )

# -------------------------- 报告生成逻辑 --------------------------
def build_report() -> dict[str, Any]:
    """收集所有环境信息，生成完整报告数据"""
    return {
        "生成时间": get_beijing_time(),
        "项目根目录": str(PROJECT_ROOT),
        "Python版本": sys.version.split()[0],
        "Python执行路径": sys.executable,
        "操作系统": platform.platform(),
        "Git当前分支": run_command(["git", "branch", "--show-current"]),
        "Git文件状态": run_command(["git", "status", "--short"]),
        "项目文件列表": visible_project_files(),
    }

def write_reports(report: dict[str, Any]) -> None:
    """将报告写入JSON和Markdown文件（内容全汉化）"""
    # 写入JSON报告
    JSON_REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    # 准备Markdown内容
    branch = report["Git当前分支"]["stdout"] or "(尚未创建分支)"
    status = report["Git文件状态"]["stdout"] or "工作区干净，无修改"

    lines = [
        "# 开发环境检查报告",
        "",
        f"- 生成时间：{report['生成时间']}",
        f"- 项目根目录：`{report['项目根目录']}`",
        f"- Python 版本：`{report['Python版本']}`",
        f"- Python 路径：`{report['Python执行路径']}`",
        f"- Git 分支：`{branch}`",
        "",
        "## Git 状态",
        "",
        "```text",
        status,
        "```",
        "",
        "## 项目文件列表",
        "",
    ]
    lines.extend(f"- `{file}`" for file in report["项目文件列表"])
    MARKDOWN_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

def append_learning_log(report: dict[str, Any]) -> None:
    """向学习日志追加一条运行记录（中文）"""
    branch = report["Git当前分支"]["stdout"] or "无分支"
    log_content = LEARNING_LOG.read_text(encoding="utf-8")
    new_record = f"| {report['生成时间']} | python3 src/workstation_check.py | 执行成功 | 分支：{branch} |\n"
    LEARNING_LOG.write_text(log_content + new_record, encoding="utf-8")

# -------------------------- 主程序入口 --------------------------
def main():
    """主函数：执行检查、生成报告、记录日志"""
    # 初始化目录和日志文件
    ensure_workspace_files()
    # 生成环境检查报告
    report = build_report()
    # 写入JSON和Markdown报告
    write_reports(report)
    # 追加学习日志
    append_learning_log(report)

    # 终端输出（全中文）
    branch = report["Git当前分支"]["stdout"] or "(无分支)"
    print(f"[成功] 项目根目录：{PROJECT_ROOT}")
    print(f"[成功] Python 版本：{report['Python版本']}")
    print(f"[成功] Git 当前分支：{branch}")
    print(f"[成功] 已生成：{JSON_REPORT.name}")
    print(f"[成功] 已生成：{MARKDOWN_REPORT.name}")
    print("[提示] 可执行 git status 查看状态，确认无误后提交文件")

# 运行主程序
if __name__ == "__main__":
    main()