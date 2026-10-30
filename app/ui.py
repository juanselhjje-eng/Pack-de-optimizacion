import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from pathlib import Path
import json

from app import diagnostics
from app.network import run_ping_test
from app.cleanup import get_temp_cleanup_preview

APP_NAME = "Ultimate PC Optimizer"

class OptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("920x680")
        self.root.minsize(760, 560)
        self.last_report = None
        self._build()
        self.refresh()

    def _build(self):
        outer = ttk.Frame(self.root, padding=16)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text=APP_NAME, font=("Segoe UI", 20, "bold")).pack(anchor="w")
        ttk.Label(outer, text="Diagnóstico y mantenimiento responsable de Windows", foreground="#666").pack(anchor="w", pady=(0, 12))
        actions = ttk.Frame(outer)
        actions.pack(fill="x", pady=(0, 10))
        ttk.Button(actions, text="Analizar equipo", command=self.refresh).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Prueba de ping", command=self.ping).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Revisar temporales", command=self.temp_preview).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Exportar informe", command=self.export).pack(side="left")
        self.status = ttk.Label(outer, text="Listo", foreground="#555")
        self.status.pack(anchor="w", pady=(0, 8))
        self.output = tk.Text(outer, wrap="word", font=("Consolas", 10), height=25)
        self.output.pack(fill="both", expand=True)
        self.output.configure(state="disabled")
        ttk.Label(outer, text="Los cambios del sistema no se aplican automáticamente. Revisa cada acción antes de ejecutarla.", foreground="#8a4b08").pack(anchor="w", pady=(10, 0))

    def show(self, text):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.configure(state="disabled")

    def refresh(self):
        self.status.configure(text="Analizando...")
        self.root.update_idletasks()
        try:
            self.last_report = diagnostics.build_report()
            self.show(diagnostics.format_report(self.last_report))
            self.status.configure(text="Análisis completado: " + datetime.now().strftime("%H:%M:%S"))
        except Exception as exc:
            self.status.configure(text="No se pudo completar el análisis")
            messagebox.showerror(APP_NAME, str(exc))

    def ping(self):
        host = "1.1.1.1"
        result = run_ping_test(host, count=5)
        self.show("PRUEBA DE RED\n\n" + json.dumps(result, indent=2, ensure_ascii=False))
        self.status.configure(text="Prueba terminada")

    def temp_preview(self):
        result = get_temp_cleanup_preview()
        self.show("VISTA PREVIA DE ARCHIVOS TEMPORALES\n\n" + json.dumps(result, indent=2, ensure_ascii=False))
        self.status.configure(text="Vista previa; no se ha eliminado ningún archivo")

    def export(self):
        if not self.last_report:
            messagebox.showinfo(APP_NAME, "Primero analiza el equipo.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Informe JSON", "*.json")],
            initialfile="pc-report.json"
        )
        if not path:
            return
        Path(path).write_text(json.dumps(self.last_report, indent=2, ensure_ascii=False), encoding="utf-8")
        messagebox.showinfo(APP_NAME, "Informe guardado correctamente.")

def run():
    root = tk.Tk()
    OptimizerApp(root)
    root.mainloop()
