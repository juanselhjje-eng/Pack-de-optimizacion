import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from pathlib import Path

from app import diagnostics, network, cleanup, processes, dev_environment, startup, gpu, power, benchmark, recommendations, profiles

APP_NAME = "Ultimate PC Optimizer"

class OptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("1120x760")
        self.root.minsize(900, 620)
        self.report = None
        self._build()
        self.refresh()

    def _build(self):
        shell = ttk.Frame(self.root, padding=14)
        shell.pack(fill="both", expand=True)
        header = ttk.Frame(shell)
        header.pack(fill="x", pady=(0, 12))
        ttk.Label(header, text=APP_NAME, font=("Segoe UI", 21, "bold")).pack(anchor="w")
        ttk.Label(header, text="Diagnóstico, mantenimiento y rendimiento con cambios controlados").pack(anchor="w")
        toolbar = ttk.Frame(shell)
        toolbar.pack(fill="x", pady=(0, 10))
        ttk.Button(toolbar, text="Analizar equipo", command=self.refresh).pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Exportar informe", command=self.export).pack(side="left", padx=6)
        ttk.Button(toolbar, text="Seguridad", command=self.security_info).pack(side="left", padx=6)
        self.status = ttk.Label(shell, text="Preparado")
        self.status.pack(anchor="w", pady=(0, 8))
        self.tabs = ttk.Notebook(shell)
        self.tabs.pack(fill="both", expand=True)
        self.dashboard = self._text_tab("Resumen")
        self.process_tab = self._text_tab("Procesos")
        self.dev_tab = self._text_tab("Programación")
        self.network_tab = self._network_tab()
        self.maintenance_tab = self._maintenance_tab()
        self.startup_tab = self._startup_tab()
        self.performance_tab = self._performance_tab()
        self.profile_tab = self._profile_tab()

    def _text_tab(self, name):
        frame = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(frame, text=name)
        text = tk.Text(frame, wrap="word", font=("Consolas", 10), undo=False)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=text.yview)
        text.configure(yscrollcommand=scroll.set, state="disabled")
        text.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        return text

    def _set(self, widget, content):
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", content)
        widget.configure(state="disabled")

    def _network_tab(self):
        frame = ttk.Frame(self.tabs, padding=12)
        self.tabs.add(frame, text="Red")
        ttk.Label(frame, text="Host para prueba ICMP (por defecto Cloudflare DNS):").pack(anchor="w")
        self.host = tk.StringVar(value="1.1.1.1")
        ttk.Entry(frame, textvariable=self.host, width=32).pack(anchor="w", pady=6)
        ttk.Button(frame, text="Ejecutar prueba de ping", command=self.run_ping).pack(anchor="w")
        self.network_output = tk.Text(frame, wrap="word", font=("Consolas", 10), height=22)
        self.network_output.pack(fill="both", expand=True, pady=(10, 0))
        self.network_output.configure(state="disabled")
        return frame

    def _maintenance_tab(self):
        frame = ttk.Frame(self.tabs, padding=12)
        self.tabs.add(frame, text="Mantenimiento")
        ttk.Label(frame, text="La primera versión solo analiza. No elimina archivos.").pack(anchor="w")
        ttk.Button(frame, text="Analizar archivos temporales", command=self.preview_temp).pack(anchor="w", pady=8)
        self.maintenance_output = tk.Text(frame, wrap="word", font=("Consolas", 10))
        self.maintenance_output.pack(fill="both", expand=True)
        self.maintenance_output.configure(state="disabled")
        return frame

    def _startup_tab(self):
        frame = ttk.Frame(self.tabs, padding=12)
        self.tabs.add(frame, text="Inicio de Windows")
        ttk.Label(frame, text="Consulta de solo lectura. No desactiva aplicaciones.").pack(anchor="w")
        ttk.Button(frame, text="Analizar ubicaciones de inicio", command=self.scan_startup).pack(anchor="w", pady=8)
        self.startup_output = tk.Text(frame, wrap="word", font=("Consolas", 10))
        self.startup_output.pack(fill="both", expand=True)
        self.startup_output.configure(state="disabled")
        return frame

    def _performance_tab(self):
        frame = ttk.Frame(self.tabs, padding=12)
        self.tabs.add(frame, text="Rendimiento")
        ttk.Label(frame, text="Consultas de GPU, energía y una microprueba local.").pack(anchor="w")
        buttons = ttk.Frame(frame)
        buttons.pack(anchor="w", pady=8)
        ttk.Button(buttons, text="Consultar GPU NVIDIA", command=self.show_gpu).pack(side="left", padx=(0, 6))
        ttk.Button(buttons, text="Consultar energía", command=self.show_power).pack(side="left", padx=6)
        ttk.Button(buttons, text="Ejecutar microprueba", command=self.run_benchmark).pack(side="left", padx=6)
        self.performance_output = tk.Text(frame, wrap="word", font=("Consolas", 10))
        self.performance_output.pack(fill="both", expand=True)
        self.performance_output.configure(state="disabled")
        return frame


    def _profile_tab(self):
        frame = ttk.Frame(self.tabs, padding=12)
        self.tabs.add(frame, text="Perfiles")
        ttk.Label(frame, text="Selecciona el tipo de carga para ver recomendaciones. No se aplican cambios automáticamente.").pack(anchor="w")
        self.profile_name = tk.StringVar(value="Equilibrado")
        selector = ttk.Combobox(frame, textvariable=self.profile_name, values=list(profiles.PROFILES.keys()), state="readonly", width=28)
        selector.pack(anchor="w", pady=8)
        selector.bind("<<ComboboxSelected>>", lambda event: self.show_profile())
        self.profile_output = tk.Text(frame, wrap="word", font=("Consolas", 10))
        self.profile_output.pack(fill="both", expand=True)
        self.profile_output.configure(state="disabled")
        self.show_profile()
        return frame

    def show_profile(self):
        selected = profiles.PROFILES.get(self.profile_name.get(), {})
        content = selected.get("description", "") + "\n\nRECOMENDACIONES\n\n"
        content += "\n".join("- " + item for item in selected.get("actions", []))
        self._set(self.profile_output, content)

    def refresh(self):
        self.status.configure(text="Analizando hardware y sistema...")
        self.root.update_idletasks()
        try:
            self.report = diagnostics.build_report()
            self.report["recommendations"] = recommendations.analyze(self.report)
            self._set(self.dashboard, diagnostics.format_report(self.report) + "\n\nRECOMENDACIONES\n\n" + json.dumps(self.report["recommendations"], indent=2, ensure_ascii=False))
            self._set(self.process_tab, json.dumps(processes.top_processes(), indent=2, ensure_ascii=False))
            self._set(self.dev_tab, json.dumps(dev_environment.scan_development_tools(), indent=2, ensure_ascii=False))
            self.status.configure(text="Análisis completado: " + datetime.now().strftime("%H:%M:%S"))
        except Exception as exc:
            self.status.configure(text="Error durante el análisis")
            messagebox.showerror(APP_NAME, str(exc))

    def run_ping(self):
        try:
            result = network.run_ping_test(self.host.get().strip(), count=10)
            self._set(self.network_output, json.dumps(result, indent=2, ensure_ascii=False))
            self.tabs.select(3)
        except Exception as exc:
            messagebox.showerror(APP_NAME, str(exc))

    def preview_temp(self):
        self._set(self.maintenance_output, json.dumps(cleanup.get_temp_cleanup_preview(), indent=2, ensure_ascii=False))
        self.tabs.select(4)

    def scan_startup(self):
        self._set(self.startup_output, json.dumps(startup.scan_startup_entries(), indent=2, ensure_ascii=False))
        self.tabs.select(5)

    def show_gpu(self):
        self._set(self.performance_output, json.dumps(gpu.nvidia_status(), indent=2, ensure_ascii=False))
        self.tabs.select(6)

    def show_power(self):
        self._set(self.performance_output, json.dumps(power.get_power_status(), indent=2, ensure_ascii=False))
        self.tabs.select(6)

    def run_benchmark(self):
        if not messagebox.askyesno("Microprueba", "Se ejecutará una prueba corta de CPU y lectura/escritura de un archivo temporal de 16 MB. ¿Continuar?"):
            return
        self._set(self.performance_output, json.dumps(benchmark.run_quick_benchmark(), indent=2, ensure_ascii=False))
        self.tabs.select(6)

    def export(self):
        if self.report is None:
            messagebox.showinfo(APP_NAME, "Primero analiza el equipo.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Informe JSON", "*.json")],
            initialfile="ultimate-pc-report.json"
        )
        if not path:
            return
        full_report = dict(self.report)
        full_report["processes"] = processes.top_processes()
        full_report["development_tools"] = dev_environment.scan_development_tools()
        full_report["nvidia"] = gpu.nvidia_status()
        full_report["power"] = power.get_power_status()
        Path(path).write_text(json.dumps(full_report, indent=2, ensure_ascii=False), encoding="utf-8")
        messagebox.showinfo(APP_NAME, "Informe exportado.")

    def security_info(self):
        messagebox.showinfo(
            "Seguridad",
            "Esta versión es de diagnóstico. No desactiva Defender, firewall, Windows Update ni servicios. "
            "No elimina temporales ni cambia el registro. Los ajustes automáticos se añadirán solo con "
            "confirmación, respaldo y método de reversión."
        )

def run():
    root = tk.Tk()
    OptimizerApp(root)
    root.mainloop()
