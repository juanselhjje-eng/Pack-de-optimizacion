def recommendations():
    return {
        "principle": "Usar los recursos necesarios para la tarea, sin forzar el 100% permanente.",
        "why_not_100_percent": [
            "CPU y GPU al 100% sin necesidad generan calor y consumo adicionales.",
            "La RAM debe conservar margen para Windows y las aplicaciones; llenarla no acelera el equipo.",
            "Con temperatura excesiva, el sistema reduce frecuencias para proteger el hardware."
        ],
        "avoid_unnecessary_limits": [
            "Conecta el cargador original para tareas exigentes.",
            "Selecciona el modo de energía y ventilación adecuado en Windows o Armoury Crate.",
            "Comprueba que una aplicación use la GPU dedicada cuando realmente la necesite.",
            "Mantén controladores actualizados desde ASUS o NVIDIA.",
            "Identifica el cuello de botella antes de cambiar ajustes."
        ],
        "safety": [
            "No desactiva protecciones térmicas, Defender, firewall ni Windows Update.",
            "No recomienda desactivar servicios esenciales ni fijar CPU/GPU al 100% permanentemente.",
            "El máximo rendimiento puede elevar temperatura, ruido y consumo."
        ]
    }
