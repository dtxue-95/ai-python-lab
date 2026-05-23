from __future__ import annotations

import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = PROJECT_ROOT / "reports"
NOTES_DIR = PROJECT_ROOT / "notes"
JSON_REPORT = REPORTS_DIR / "workstation-check.json"
MARKDOWN_REPORT = REPORTS_DIR / "workstation-report.md"
LEARNING_LOG = NOTES_DIR / "learning-log.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def run_command(command: list[str]) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        return {
            "command": " ".join(command),
            "returncode": 127,
            "stdout": "",
            "stderr": f"{command[0]} was not found",
        }
    return {
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def visible_project_files() -> list[str]:
    files: list[str] = []
    for path in sorted(PROJECT_ROOT.rglob("*")):
        if ".git" in path.parts or path.is_dir():
            continue
        files.append(str(path.relative_to(PROJECT_ROOT)))
    return files


def ensure_workspace_files() -> None:
    REPORTS_DIR.mkdir(exist_ok=True)
    NOTES_DIR.mkdir(exist_ok=True)
    if not LEARNING_LOG.exists():
        LEARNING_LOG.write_text(
            "# Learning Log\n\n| Time | Command or action | Result | Note |\n|---|---|---|---|\n",
            encoding="utf-8",
        )


def build_report() -> dict[str, Any]:
    return {
        "generated_at": utc_now(),
        "project_root": str(PROJECT_ROOT),
        "python_version": sys.version.split()[0],
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "git_branch": run_command(["git", "branch", "--show-current"]),
        "git_status": run_command(["git", "status", "--short"]),
        "project_files": visible_project_files(),
    }


def write_reports(report: dict[str, Any]) -> None:
    JSON_REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    branch = report["git_branch"]["stdout"] or "(no branch yet)"
    status = report["git_status"]["stdout"] or "working tree clean"
    lines = [
        "# Workstation Report",
        "",
        f"- Generated at: {report['generated_at']}",
        f"- Project root: `{report['project_root']}`",
        f"- Python version: `{report['python_version']}`",
        f"- Python executable: `{report['python_executable']}`",
        f"- Git branch: `{branch}`",
        "",
        "## Git status",
        "",
        "```text",
        status,
        "```",
        "",
        "## Project files",
        "",
    ]
    lines.extend(f"- `{file}`" for file in report["project_files"])
    MARKDOWN_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_learning_log(report: dict[str, Any]) -> None:
    branch = report["git_branch"]["stdout"] or "no branch"
    LEARNING_LOG.write_text(
        LEARNING_LOG.read_text(encoding="utf-8")
        + f"| {report['generated_at']} | python3 src/workstation_check.py | ok | branch: {branch} |\n",
        encoding="utf-8",
    )


def main() -> None:
    ensure_workspace_files()
    report = build_report()
    write_reports(report)
    append_learning_log(report)

    branch = report["git_branch"]["stdout"] or "(no branch yet)"
    print(f"[ok] project root: {PROJECT_ROOT}")
    print(f"[ok] python: {report['python_version']} at {report['python_executable']}")
    print(f"[ok] git branch: {branch}")
    print(f"[ok] wrote {JSON_REPORT.relative_to(PROJECT_ROOT)}")
    print(f"[ok] wrote {MARKDOWN_REPORT.relative_to(PROJECT_ROOT)}")
    print("[next] run git status, then commit the files when the output looks right")


if __name__ == "__main__":
    main()