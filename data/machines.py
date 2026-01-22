"""Machine data and utilities"""

MACHINES = [
    {
        "name": "Tascam Portastudio", 
        "seed": "tascam1",
        "description": "Cuatro pistas de cinta que capturan el tiempo de manera física. El hiss como textura, no como error. Cada grabación es un acto irreversible que obliga a decidir."
    },
    {
        "name": "Akai MPC 2000XL", 
        "seed": "akai2",
        "description": "Pads sensibles a la presión que responden al tacto humano. Secuenciador que piensa en loops, no en barras infinitas. La memoria limitada como restricción creativa."
    },
    {
        "name": "Roland SP-404", 
        "seed": "roland3",
        "description": "Sampler portátil que cabe en una mochila. Efectos lo-fi que abrazan la degradación. Diseñado para ser tocado en vivo, no programado en silencio."
    },
    {
        "name": "Technics SL-1200", 
        "seed": "technics4",
        "description": "Tornamesa de tracción directa construida como tanque. El vinilo como formato físico irremplazable. Scratchear es tocar un instrumento, no reproducir audio."
    },
    {
        "name": "Korg Volca Keys", 
        "seed": "korg5",
        "description": "Sintetizador análogo que cabe en la palma de la mano. Perillas físicas para cada parámetro esencial. Lo pequeño no es limitación, es enfoque."
    },
    {
        "name": "Teenage Engineering OP-1", 
        "seed": "teenage6",
        "description": "Estudio completo con batería incorporada. Limitaciones de grabación que fuerzan creatividad. Diseño que invita a explorar, no a optimizar."
    },
]


def get_machines():
    """Get all machines"""
    return MACHINES
