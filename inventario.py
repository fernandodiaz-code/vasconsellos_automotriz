import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar las variables del archivo .env
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# Prueba: obtener los datos de una tabla existente (por ejemplo, "users")
try:
    response = supabase.table("articulo").select("*").limit(1).execute()
    print("✅ Conexión exitosa a Supabase")
    print("Datos de ejemplo:", response.data)
except Exception as e:
    print("❌ Error al conectar con Supabase:")
    print(e)
