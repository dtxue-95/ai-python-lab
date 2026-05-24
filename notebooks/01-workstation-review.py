import json
from pathlib import Path

report = json.loads(Path("../reports/workstation-check.json").read_text(encoding="utf-8"))
print(report)
print(report["Python版本"])
print(report["Git当前分支"]["stdout"])
print(len(report["项目文件列表"]))