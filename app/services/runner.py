from __future__ import annotations

import subprocess
from pathlib import Path


def build_command(repo_root: Path, script_path: str) -> list[str]:
    full = repo_root / script_path.replace('/', '\\')
    suffix = full.suffix.lower()
    if suffix == '.py':
        return ['python', str(full)]
    if suffix == '.ps1':
        return ['pwsh', '-File', str(full)]
    raise ValueError(f'Unsupported script type: {full}')


def run_script(repo_root: Path, script_path: str) -> tuple[int, str, str]:
    cmd = build_command(repo_root, script_path)
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=repo_root)
    return proc.returncode, proc.stdout, proc.stderr
