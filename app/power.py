import subprocess

def get_power_status():
    try:
        p = subprocess.run(["powercfg", "/getactivescheme"], capture_output=True, text=True, timeout=8)
        active = p.stdout.strip() if p.returncode == 0 else p.stderr.strip()
        q = subprocess.run(["powercfg", "/list"], capture_output=True, text=True, timeout=8)
        plans = q.stdout.strip() if q.returncode == 0 else q.stderr.strip()
        return {"active_plan": active, "available_plans": plans, "changed": False}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"error": str(exc)}
