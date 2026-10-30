try:
    import psutil
except ImportError:
    psutil = None

def top_processes(limit=15):
    if psutil is None:
        return {"error": "Instala las dependencias con pip install -r requirements.txt"}
    rows = []
    for proc in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            info = proc.info
            mem = info.get("memory_info")
            rows.append({
                "pid": info["pid"],
                "name": info.get("name") or "Desconocido",
                "memory_mb": round(mem.rss / 1024**2, 1) if mem else None
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return sorted(rows, key=lambda item: item["memory_mb"] or 0, reverse=True)[:max(1, min(limit, 100))]
