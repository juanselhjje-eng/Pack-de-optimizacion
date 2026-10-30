import platform
import re
import subprocess

def run_ping_test(host="1.1.1.1", count=5):
    if not re.fullmatch(r"[A-Za-z0-9.-]+", host):
        raise ValueError("Escribe un dominio o una dirección IPv4 válida.")
    count = max(1, min(int(count), 20))
    flag = "-n" if platform.system() == "Windows" else "-c"
    try:
        p = subprocess.run(["ping", flag, str(count), host], capture_output=True, text=True, timeout=35)
        output = p.stdout + p.stderr
        times = [float(x.replace(",", ".")) for x in re.findall(r"time[=<]([0-9.,]+)\\s*ms", output, re.I)]
        loss = re.search(r"\\((\\d+)%\\s*loss\\)", output, re.I)
        if not loss:
            loss = re.search(r"perdidos\\s*=\\s*\\d+\\s*\\((\\d+)%", output, re.I)
        return {
            "host": host,
            "responses": len(times),
            "latency_ms": times,
            "minimum_ms": min(times) if times else None,
            "average_ms": round(sum(times) / len(times), 2) if times else None,
            "maximum_ms": max(times) if times else None,
            "packet_loss_percent": int(loss.group(1)) if loss else None,
            "raw_output": output.strip(),
            "warning": "El resultado depende de la ruta y del host. No garantiza el ping de un juego."
        }
    except subprocess.TimeoutExpired:
        return {"host": host, "error": "La prueba superó el tiempo límite."}
