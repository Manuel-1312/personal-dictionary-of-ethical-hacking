from __future__ import annotations

import shlex
import shutil
import subprocess
from pathlib import Path


def script_full_path(repo_root: Path, script_path: str) -> Path:
    return repo_root / Path(script_path.replace('\\', '/'))


def _find_python_command() -> list[str] | None:
    if shutil.which('python'):
        return ['python']
    if shutil.which('py'):
        return ['py', '-3']
    return None


def _find_powershell_command() -> list[str] | None:
    if shutil.which('pwsh'):
        return ['pwsh']
    if shutil.which('powershell'):
        return ['powershell']
    return None


def build_command(repo_root: Path, script_path: str, extra_args: str = '') -> list[str]:
    full = script_full_path(repo_root, script_path)
    suffix = full.suffix.lower()
    user_args = shlex.split(extra_args, posix=False) if extra_args.strip() else []

    if suffix == '.py':
        py = _find_python_command()
        if not py:
            raise RuntimeError('No se encontró Python en PATH (python ni py).')
        return [*py, str(full), *user_args]

    if suffix == '.ps1':
        ps = _find_powershell_command()
        if not ps:
            raise RuntimeError('No se encontró PowerShell en PATH (pwsh ni powershell).')
        if ps[0].lower() == 'pwsh':
            return [*ps, '-ExecutionPolicy', 'Bypass', '-File', str(full), *user_args]
        return [*ps, '-ExecutionPolicy', 'Bypass', '-File', str(full), *user_args]

    raise ValueError(f'Unsupported script type: {full}')


def run_script(repo_root: Path, script_path: str, extra_args: str = '') -> tuple[int, str, str, list[str]]:
    full = script_full_path(repo_root, script_path)
    if not full.exists():
        return 1, '', f'El script no existe en la ruta esperada: {full}', [str(full)]

    try:
        cmd = build_command(repo_root, script_path, extra_args)
    except Exception as exc:
        return 1, '', str(exc), [str(full)]

    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=repo_root)
    return proc.returncode, proc.stdout, proc.stderr, cmd
