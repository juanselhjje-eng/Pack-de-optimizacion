import time
import hashlib
import tempfile
from pathlib import Path

def run_quick_benchmark():
    # Micropruebas breves, locales y no destructivas. No equivalen a un benchmark profesional.
    started = time.perf_counter()
    data = b"UltimatePCOptimizer" * 25000
    digest = hashlib.sha256()
    for _ in range(100):
        digest.update(data)
    cpu_seconds = time.perf_counter() - started

    write_seconds = None
    read_seconds = None
    size_mb = 16
    try:
        with tempfile.TemporaryDirectory(prefix="upo_bench_") as folder:
            path = Path(folder) / "test.bin"
            payload = b"0" * (size_mb * 1024 * 1024)
            t0 = time.perf_counter()
            path.write_bytes(payload)
            write_seconds = round(time.perf_counter() - t0, 4)
            t0 = time.perf_counter()
            _ = path.read_bytes()
            read_seconds = round(time.perf_counter() - t0, 4)
    except OSError as exc:
        return {"cpu_test_seconds": round(cpu_seconds, 4), "storage_error": str(exc)}

    return {
        "cpu_hash_test_seconds": round(cpu_seconds, 4),
        "temporary_file_size_mb": size_mb,
        "temporary_write_seconds": write_seconds,
        "temporary_read_seconds": read_seconds,
        "note": "Prueba corta orientativa. El resultado depende de temperatura, energía, procesos y caché; no comparar equipos distintos con esta única cifra."
    }
