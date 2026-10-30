def analyze(report):
    findings = []
    cpu = report.get("cpu", {})
    memory = report.get("memory", {})
    disks = report.get("disks", {})

    cpu_load = cpu.get("usage_percent")
    if isinstance(cpu_load, (int, float)) and cpu_load >= 90:
        findings.append({
            "level": "warning",
            "area": "CPU",
            "finding": "Uso de CPU muy alto durante la medición.",
            "suggestion": "Revisa la pestaña Procesos y repite la medición cuando el equipo esté en reposo."
        })
    elif isinstance(cpu_load, (int, float)) and cpu_load >= 75:
        findings.append({
            "level": "info",
            "area": "CPU",
            "finding": "Uso de CPU elevado durante la medición.",
            "suggestion": "Comprueba si hay compilaciones, actualizaciones o aplicaciones exigentes en segundo plano."
        })

    ram_load = memory.get("used_percent")
    if isinstance(ram_load, (int, float)) and ram_load >= 90:
        findings.append({
            "level": "warning",
            "area": "RAM",
            "finding": "La memoria está casi llena.",
            "suggestion": "Identifica procesos con alto consumo antes de cerrar aplicaciones. No uses limpiadores de RAM."
        })
    elif isinstance(ram_load, (int, float)) and ram_load >= 80:
        findings.append({
            "level": "info",
            "area": "RAM",
            "finding": "El uso de memoria es alto.",
            "suggestion": "Revisa navegadores, IDE y máquinas virtuales abiertas."
        })

    for drive, values in disks.items():
        free = values.get("free_gb")
        total = values.get("total_gb")
        if isinstance(free, (int, float)) and isinstance(total, (int, float)) and total > 0:
            free_percent = free / total * 100
            if free_percent < 10:
                findings.append({
                    "level": "warning",
                    "area": "Almacenamiento",
                    "finding": f"{drive} tiene menos del 10% de espacio libre.",
                    "suggestion": "Revisa archivos grandes, descargas y copias antiguas. No borres carpetas del sistema."
                })
            elif free_percent < 20:
                findings.append({
                    "level": "info",
                    "area": "Almacenamiento",
                    "finding": f"{drive} tiene menos del 20% de espacio libre.",
                    "suggestion": "Planifica liberar espacio y conserva margen para actualizaciones y proyectos."
                })

    if not findings:
        findings.append({
            "level": "ok",
            "area": "Sistema",
            "finding": "No se detectaron alertas en las métricas básicas disponibles.",
            "suggestion": "Esto no sustituye una revisión de temperaturas, controladores ni pruebas prolongadas."
        })
    return findings
