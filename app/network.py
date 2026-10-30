import platform
import re
import subprocess

def run_ping_test(host="1.1.1.1", count=5):
    if not re.fullmatch(r"[A-Za-z0-9.:-]+", host):
        raise ValueError("Host no válido")
    count = max(1, min(int(count), 20))
    flag = "-n" if platform.system() == "Windows" else "-c"
    try:
        p = subprocess.run(["ping", flag, str(count), host], capture_output=True, text=True, timeout=35)
        output = p.stdout + p.stderr
        times = [float(x.replace(",", ".")) for x in re.findall(r"time[=<]([0-9.,]+)\s*ms", output, re.I)]
        lost = re.search(r"\((\d+)%\s*loss\)", output, re.I)
        return {
            "host": host,
            "return_code": p.returncode,
            "latency_ms": times,
            "average_ms": round(sum(times) / len(times), 2) if times else None,
            "packet_loss_percent": int(lost.group(1)) if lost else None,
            "raw_output": output.strip(),
            "warning": "Una prueba ICMP no representa por sí sola el ping dentro de un juego."
        }
    except subprocess.TimeoutExpired:
        return {"host": host, "error": "La prueba superó el tiempo límite"}
