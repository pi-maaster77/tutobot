import os

def cargar_eventos():
    dir = "events"
    if not os.path.exists(dir):
        return
    
    archivos = [
        archivo for archivo in os.listdir(dir)
        if archivo != "__pycache__"
        ]
    librerias = ""
    for libreria in archivos:
        librerias += f"    {libreria[:-3]}.exportacion(bot) \n"
    
    crudo = str(archivos)\
        .replace("[", "")\
        .replace("'", "")\
        .replace("]", "")\
        .replace(".py", "")

    return\
f"""
from {dir} import {crudo}
def eventos(bot):
{librerias}
"""
print(cargar_eventos())