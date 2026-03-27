from __future__ import annotations

import shlex
import subprocess
from pathlib import Path


def script_full_path(repo_root: Path, script_path: str) -> Path:
    return repo_root / Path(script_path.replace('\\', '/'))


def build_command(repo_root: Path, script_path: str, extra_args: str = "") -> list[str]:
    full = script_full_path(repo_root, script_path)
    suffix = full.suffix.lower()
    user_args = shlex.split(extra_args, posix=False) if extra_args.strip() else []
    if suffix == '.py':
        return ['python', str(full), *user_args]
    if suffix == '.ps1':
        return ['pwsh', '-ExecutionPolicy', 'Bypass', '-File', str(full), *user_args]
    raise ValueError(f'Unsupported script type: {full}')


def run_script(repo_root: Path, script_path: str, extra_args: str = "") -> tuple[int, str, str, list[str]]:
    cmd = build_command(repo_root, script_path, extra_args)
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=repo_root)
    return proc.returncode, proc.stdout, proc.stderr, cmd
