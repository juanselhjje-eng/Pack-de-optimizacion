PROFILES = {
    "Equilibrado": {
        "description": "Uso diario con equilibrio entre rendimiento, consumo, ruido y temperatura.",
        "actions": [
            "Mantener controladores y Windows actualizados desde fuentes oficiales.",
            "Revisar procesos solo cuando se note lentitud.",
            "Dejar activos los mecanismos de seguridad y mantenimiento de Windows."
        ]
    },
    "Programacion": {
        "description": "Diagnóstico para IDE, terminales, contenedores, compilaciones y multitarea.",
        "actions": [
            "Revisar memoria disponible antes de abrir máquinas virtuales o proyectos grandes.",
            "Comprobar espacio libre para dependencias, cachés y compilaciones.",
            "Identificar procesos de alto consumo sin cerrarlos automáticamente.",
            "Evitar borrar cachés de Python, Node.js o IDE sin conocer su función."
        ]
    },
    "Gaming": {
        "description": "Diagnóstico para juegos, GPU, pantalla, energía y red.",
        "actions": [
            "Verificar que el juego use la GPU dedicada cuando corresponda.",
            "Comprobar la frecuencia real de la pantalla y el modo de energía.",
            "Medir temperatura y uso de GPU con herramientas compatibles.",
            "Comparar ping y pérdida hacia el servidor del juego; ICMP es solo una referencia."
        ]
    },
    "Maximo rendimiento": {
        "description": "Perfil de diagnóstico para cargas exigentes. No fuerza voltajes, ventiladores ni límites térmicos.",
        "actions": [
            "Conectar el portátil a la corriente y revisar la temperatura antes de cargas prolongadas.",
            "Medir CPU, GPU, RAM y almacenamiento durante la tarea real.",
            "Cerrar únicamente aplicaciones que el usuario haya identificado como innecesarias.",
            "No desactivar Defender, firewall, Windows Update ni servicios esenciales.",
            "Detener la carga si aparecen temperaturas anormales, apagados o inestabilidad."
        ]
    },
    "General": {
        "description": "Alias de compatibilidad para el perfil equilibrado.",
        "actions": [
            "Revisar aplicaciones de inicio.",
            "Comprobar espacio libre.",
            "Medir uso de CPU y RAM."
        ]
    }
}
