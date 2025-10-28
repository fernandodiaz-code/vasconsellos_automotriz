import os
import sys
from pathlib import Path
import django
from django.db import connections
from django.db.utils import OperationalError

# --- AÑADIR raíz del proyecto al sys.path ---
BASE_DIR = Path(__file__).resolve().parent.parent  # carpeta donde está manage.py
sys.path.insert(0, str(BASE_DIR))

# --- Apuntar a settings de Django ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vasconsellos.settings")

# --- Inicializar Django ---
django.setup()

def probar_conexion():
    try:
        connections['default'].cursor()
        print("✅ Conexión exitosa a la base de datos Supabase.")
    except OperationalError as e:
        print("❌ Error al conectar con la base de datos:")
        print(e)

if __name__ == "__main__":
    probar_conexion()
