from __future__ import annotations

import json
from pathlib import Path


def state_file(repo_root: Path) -> Path:
    return repo_root / 'app' / 'state.json'


def load_state(repo_root: Path) -> dict:
    path = state_file(repo_root)
    if not path.exists():
        return {'favorites': [], 'history': []}
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return {'favorites': [], 'history': []}


def save_state(repo_root: Path, state: dict) -> None:
    path = state_file(repo_root)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding='utf-8')


def add_history(repo_root: Path, item: dict) -> dict:
    state = load_state(repo_root)
    history = state.setdefault('history', [])
    history.insert(0, item)
    state['history'] = history[:30]
    save_state(repo_root, state)
    return state


def toggle_favorite(repo_root: Path, script: str) -> dict:
    state = load_state(repo_root)
    favorites = set(state.setdefault('favorites', []))
    if script in favorites:
        favorites.remove(script)
    else:
        favorites.add(script)
    state['favorites'] = sorted(favorites)
    save_state(repo_root, state)
    return state
