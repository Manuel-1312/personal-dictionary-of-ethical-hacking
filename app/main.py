from __future__ import annotations

import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import messagebox, ttk

from services.paths import discover_repo_root
from services.registry import ScriptEntry, load_registry
from services.runner import run_script, script_full_path
from services.state import add_history, load_state, toggle_favorite


class ToolboxApp:
    def __init__(self, root: tk.Tk, repo_root: Path):
        self.root = root
        self.repo_root = repo_root
        self.root.title('Hacking Toolbox')
        self.root.geometry('1260x780')
        self.entries = load_registry(repo_root)
        self.filtered: list[ScriptEntry] = []
        self.state = load_state(repo_root)

        categories = sorted({entry.category for entry in self.entries})
        default_category = categories[0] if categories else ''
        self.category_var = tk.StringVar(value=default_category)
        self.search_var = tk.StringVar()
        self.args_var = tk.StringVar()
        self.status_var = tk.StringVar(value=f'Repo: {repo_root}')
        self.only_favorites_var = tk.BooleanVar(value=False)

        self.build_ui(categories)
        self.refresh_list()
        self.refresh_history()

    def build_ui(self, categories: list[str]):
        container = ttk.Frame(self.root, padding=10)
        container.pack(fill='both', expand=True)

        left = ttk.Frame(container)
        left.pack(side='left', fill='y', padx=(0, 10))

        ttk.Label(left, text='Categoría').pack(anchor='w')
        self.category_box = ttk.Combobox(left, textvariable=self.category_var, values=categories, state='readonly')
        self.category_box.pack(fill='x')
        self.category_box.bind('<<ComboboxSelected>>', lambda e: self.refresh_list())

        ttk.Label(left, text='Buscar').pack(anchor='w', pady=(10, 0))
        search = ttk.Entry(left, textvariable=self.search_var)
        search.pack(fill='x')
        search.bind('<KeyRelease>', lambda e: self.refresh_list())

        ttk.Checkbutton(left, text='Solo favoritos', variable=self.only_favorites_var, command=self.refresh_list).pack(anchor='w', pady=(8, 0))

        self.listbox = tk.Listbox(left, width=44, height=30)
        self.listbox.pack(fill='both', expand=True, pady=(10, 0))
        self.listbox.bind('<<ListboxSelect>>', lambda e: self.show_selected())
        self.listbox.bind('<Double-Button-1>', lambda e: self.run_selected())

        right = ttk.Frame(container)
        right.pack(side='left', fill='both', expand=True)

        self.title_label = ttk.Label(right, text='Selecciona un script', font=('Segoe UI', 14, 'bold'))
        self.title_label.pack(anchor='w')

        meta = ttk.Frame(right)
        meta.pack(fill='x', pady=(8, 6))
        ttk.Label(meta, text='Argumentos extra:').pack(anchor='w')
        ttk.Entry(meta, textvariable=self.args_var).pack(fill='x')

        self.desc = tk.Text(right, height=12, wrap='word')
        self.desc.pack(fill='x', pady=(8, 8))

        btns = ttk.Frame(right)
        btns.pack(fill='x')
        ttk.Button(btns, text='Ejecutar', command=self.run_selected).pack(side='left')
        ttk.Button(btns, text='Usar ejemplo', command=self.use_example_args).pack(side='left', padx=(8, 0))
        ttk.Button(btns, text='Copiar comando', command=self.copy_command).pack(side='left', padx=(8, 0))
        ttk.Button(btns, text='Favorito ★', command=self.toggle_selected_favorite).pack(side='left', padx=(8, 0))
        ttk.Button(btns, text='Refrescar', command=self.reload_registry).pack(side='left', padx=(8, 0))

        ttk.Label(right, text='Salida').pack(anchor='w', pady=(12, 0))
        self.output = tk.Text(right, wrap='word', height=18)
        self.output.pack(fill='both', expand=True)

        history_frame = ttk.Frame(container)
        history_frame.pack(side='left', fill='y', padx=(10, 0))
        ttk.Label(history_frame, text='Historial').pack(anchor='w')
        self.history_list = tk.Listbox(history_frame, width=36, height=30)
        self.history_list.pack(fill='both', expand=True)
        self.history_list.bind('<<ListboxSelect>>', lambda e: self.use_history_item())

        status = ttk.Label(self.root, textvariable=self.status_var, anchor='w')
        status.pack(fill='x', padx=10, pady=(0, 8))

    def refresh_list(self):
        category = self.category_var.get().strip()
        query = self.search_var.get().strip().lower()
        only_favorites = self.only_favorites_var.get()
        favorites = set(self.state.get('favorites', []))
        self.filtered = [
            entry for entry in self.entries
            if entry.category == category
            and (not query or query in entry.script.lower() or query in entry.description.lower())
            and (not only_favorites or entry.script in favorites)
        ]
        self.listbox.delete(0, tk.END)
        for entry in self.filtered:
            prefix = '★ ' if entry.script in favorites else ''
            self.listbox.insert(tk.END, prefix + entry.script)
        if self.filtered:
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(0)
            self.show_selected()
        else:
            self.title_label.config(text='Sin resultados')
            self.desc.delete('1.0', tk.END)
            self.desc.insert(tk.END, f'No se encontraron scripts para la categoría seleccionada.\n\nRepo detectado: {self.repo_root}')

    def refresh_history(self):
        self.history_list.delete(0, tk.END)
        for item in self.state.get('history', []):
            self.history_list.insert(tk.END, f"{item.get('time','')} | {item.get('script','')}")

    def selected_entry(self) -> ScriptEntry | None:
        sel = self.listbox.curselection()
        if not sel:
            return None
        return self.filtered[sel[0]]

    def show_selected(self):
        entry = self.selected_entry()
        if not entry:
            return
        full_path = script_full_path(self.repo_root, entry.relative_path)
        favorite_mark = '★ ' if entry.script in set(self.state.get('favorites', [])) else ''
        self.title_label.config(text=favorite_mark + entry.script)
        self.desc.delete('1.0', tk.END)
        self.desc.insert(tk.END, f'Categoría: {entry.category}\n')
        self.desc.insert(tk.END, f'Ruta: {entry.relative_path}\n')
        self.desc.insert(tk.END, f'Descripción: {entry.description}\n\n')
        self.desc.insert(tk.END, f'Ejemplo: {entry.example or "(sin ejemplo)"}\n')
        self.desc.insert(tk.END, f'Toolkit: {entry.source_toolkit}\n')
        self.desc.insert(tk.END, f'Archivo real: {full_path}\n')
        self.status_var.set(f'Repo: {self.repo_root} | Seleccionado: {entry.script}')

    def use_example_args(self):
        entry = self.selected_entry()
        if not entry or not entry.example:
            return
        example = entry.example.strip()
        rel = entry.relative_path.replace('\\', '/')
        if rel in example:
            args = example.split(rel, 1)[1].strip()
        else:
            parts = example.split(maxsplit=1)
            args = parts[1] if len(parts) > 1 else ''
        self.args_var.set(args)
        self.status_var.set('Argumentos copiados desde el ejemplo.')

    def copy_command(self):
        entry = self.selected_entry()
        if not entry:
            return
        command = entry.example or entry.relative_path
        if self.args_var.get().strip() and not entry.example:
            command = f'{command} {self.args_var.get().strip()}'
        self.root.clipboard_clear()
        self.root.clipboard_append(command)
        self.status_var.set('Comando copiado al portapapeles.')

    def toggle_selected_favorite(self):
        entry = self.selected_entry()
        if not entry:
            return
        self.state = toggle_favorite(self.repo_root, entry.script)
        self.refresh_list()
        self.show_selected()
        self.status_var.set('Favoritos actualizados.')

    def run_selected(self):
        entry = self.selected_entry()
        if not entry:
            messagebox.showinfo('Hacking Toolbox', 'Selecciona un script primero.')
            return
        self.status_var.set(f'Ejecutando: {entry.script}')
        self.root.update_idletasks()
        code, stdout, stderr, cmd = run_script(self.repo_root, entry.relative_path, self.args_var.get())
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, '$ ' + ' '.join(cmd) + '\n\n')
        if stdout:
            self.output.insert(tk.END, stdout + ('\n' if not stdout.endswith('\n') else ''))
        if stderr:
            self.output.insert(tk.END, '\n[stderr]\n' + stderr + ('\n' if not stderr.endswith('\n') else ''))
        self.output.insert(tk.END, f'\nExit code: {code}\n')
        self.state = add_history(self.repo_root, {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'script': entry.script,
            'args': self.args_var.get().strip(),
            'exit_code': code,
        })
        self.refresh_history()
        self.status_var.set(f'Ejecución terminada con código {code}.')

    def use_history_item(self):
        sel = self.history_list.curselection()
        if not sel:
            return
        item = self.state.get('history', [])[sel[0]]
        script_name = item.get('script', '')
        args = item.get('args', '')
        self.args_var.set(args)
        for idx, entry in enumerate(self.filtered):
            if entry.script == script_name:
                self.listbox.selection_clear(0, tk.END)
                self.listbox.selection_set(idx)
                self.show_selected()
                break
        self.status_var.set('Historial cargado en argumentos.')

    def reload_registry(self):
        self.entries = load_registry(self.repo_root)
        self.state = load_state(self.repo_root)
        categories = sorted({entry.category for entry in self.entries})
        self.category_box.configure(values=categories)
        if self.category_var.get() not in categories and categories:
            self.category_var.set(categories[0])
        self.refresh_list()
        self.refresh_history()
        self.status_var.set('Catálogo recargado.')


def main():
    repo_root = discover_repo_root()
    root = tk.Tk()
    ToolboxApp(root, repo_root)
    root.mainloop()


if __name__ == '__main__':
    main()
