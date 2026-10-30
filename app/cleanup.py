import os
import tempfile
from pathlib import Path

def get_temp_cleanup_preview():
    root = Path(tempfile.gettempdir())
    files = 0
    dirs = 0
    total = 0
    errors = 0
    try:
        for item in root.iterdir():
            try:
                if item.is_file():
                    files += 1
                    total += item.stat().st_size
                elif item.is_dir():
                    dirs += 1
            except OSError:
                errors += 1
    except OSError:
        errors += 1
    return {
        "directory": str(root),
        "files_at_root": files,
        "directories_at_root": dirs,
        "total_file_size_gb": round(total / 1024**3, 3),
        "unavailable_items": errors,
        "deleted": False,
        "message": "Solo se muestra una vista previa. No se elimina nada."
    }
