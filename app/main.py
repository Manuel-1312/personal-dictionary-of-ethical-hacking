from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from services.registry import ScriptEntry, load_registry
from services.runner import run_script


class ToolboxApp:
    def __init__(self, root: tk.Tk, repo_root: Path):
        self.root = root
        self.repo_root = repo_root
        self.root.title('Hacking Toolbox')
        self.root.geometry('1100x700')
        self.entries = load_registry(repo_root)
        self.filtered: list[ScriptEntry] = []

        self.category_var = tk.StringVar(value='Python')
        self.search_var = tk.StringVar()

        self.build_ui()
        self.refresh_list()

    def build_ui(self):
        container = ttk.Frame(self.root, padding=10)
        container.pack(fill='both', expand=True)

        left = ttk.Frame(container)
        left.pack(side='left', fill='y', padx=(0, 10))

        ttk.Label(left, text='Categoría').pack(anchor='w')
        categories = sorted({entry.category for entry in self.entries})
        self.category_box = ttk.Combobox(left, textvariable=self.category_var, values=categories, state='readonly')
        self.category_box.pack(fill='x')
        self.category_box.bind('<<ComboboxSelected>>', lambda e: self.refresh_list())

        ttk.Label(left, text='Buscar').pack(anchor='w', pady=(10, 0))
        search = ttk.Entry(left, textvariable=self.search_var)
        search.pack(fill='x')
        search.bind('<KeyRelease>', lambda e: self.refresh_list())

        self.listbox = tk.Listbox(left, width=40, height=30)
        self.listbox.pack(fill='both', expand=True, pady=(10, 0))
        self.listbox.bind('<<ListboxSelect>>', lambda e: self.show_selected())

        right = ttk.Frame(container)
        right.pack(side='left', fill='both', expand=True)

        self.title_label = ttk.Label(right, text='Selecciona un script', font=('Segoe UI', 14, 'bold'))
        self.title_label.pack(anchor='w')

        self.desc = tk.Text(right, height=8, wrap='word')
        self.desc.pack(fill='x', pady=(8, 8))

        btns = ttk.Frame(right)
        btns.pack(fill='x')
        ttk.Button(btns, text='Ejecutar', command=self.run_selected).pack(side='left')
        ttk.Button(btns, text='Refrescar', command=self.reload_registry).pack(side='left', padx=(8, 0))

        ttk.Label(right, text='Salida').pack(anchor='w', pady=(12, 0))
        self.output = tk.Text(right, wrap='word')
        self.output.pack(fill='both', expand=True)

    def refresh_list(self):
        category = self.category_var.get().strip()
        query = self.search_var.get().strip().lower()
        self.filtered = [
            entry for entry in self.entries
            if entry.category == category and (not query or query in entry.script.lower() or query in entry.description.lower())
        ]
        self.listbox.delete(0, tk.END)
        for entry in self.filtered:
            self.listbox.insert(tk.END, entry.script)
        if self.filtered:
            self.listbox.selection_set(0)
            self.show_selected()

    def selected_entry(self) -> ScriptEntry | None:
        sel = self.listbox.curselection()
        if not sel:
            return None
        return self.filtered[sel[0]]

    def show_selected(self):
        entry = self.selected_entry()
        if not entry:
            return
        self.title_label.config(text=entry.script)
        self.desc.delete('1.0', tk.END)
        self.desc.insert(tk.END, f'Categoría: {entry.category}\n')
        self.desc.insert(tk.END, f'Descripción: {entry.description}\n\n')
        self.desc.insert(tk.END, f'Ejemplo: {entry.example}\n')
        self.desc.insert(tk.END, f'Toolkit: {entry.source_toolkit}\n')

    def run_selected(self):
        entry = self.selected_entry()
        if not entry:
            messagebox.showinfo('Hacking Toolbox', 'Selecciona un script primero.')
            return
        code, stdout, stderr = run_script(self.repo_root, entry.relative_path)
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, f'$ {entry.example or entry.relative_path}\n\n')
        if stdout:
            self.output.insert(tk.END, stdout + '\n')
        if stderr:
            self.output.insert(tk.END, '[stderr]\n' + stderr + '\n')
        self.output.insert(tk.END, f'\nExit code: {code}\n')

    def reload_registry(self):
        self.entries = load_registry(self.repo_root)
        self.refresh_list()


def main():
    repo_root = Path(__file__).resolve().parents[1]
    root = tk.Tk()
    ToolboxApp(root, repo_root)
    root.mainloop()


if __name__ == '__main__':
    main()
