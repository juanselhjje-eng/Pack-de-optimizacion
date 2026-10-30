try:
    import psutil
except ImportError:
    psutil = None

def top_processes(limit=20):
    if psutil is None:
        return {"error": "Instala las dependencias con pip install -r requirements.txt"}
    rows = []
    for proc in psutil.process_iter(["pid", "name", "memory_info", "status", "num_threads"]):
        try:
            info = proc.info
            mem = info.get("memory_info")
            rows.append({
                "pid": info["pid"],
                "name": info.get("name") or "Desconocido",
                "memory_mb": round(mem.rss / 1024**2, 1) if mem else None,
                "status": info.get("status"),
                "threads": info.get("num_threads")
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    rows.sort(key=lambda item: item["memory_mb"] or 0, reverse=True)
    return rows[:max(1, min(int(limit), 100))]
