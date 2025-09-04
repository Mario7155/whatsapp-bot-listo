import pandas as pd
import requests
import time
import os

# 🔹 API Key desde variable de entorno (evita ponerla fija en el código)
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("⚠️ No se encontró API_KEY en las variables de entorno.")

# 🔹 Leer el Excel (debes ponerlo en la misma carpeta que el script)
EXCEL_FILE = "mensajes.xlsx"
if not os.path.exists(EXCEL_FILE):
    raise FileNotFoundError(f"⚠️ No se encontró el archivo {EXCEL_FILE}. Colócalo en la misma carpeta que este script.")

df = pd.read_excel(EXCEL_FILE)

# ⚡ Evitar enviar a números repetidos
df = df.drop_duplicates(subset=["numero"])

# 🔹 Configuración de API
url = "https://wasenderapi.com/api/send-message"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# 🔹 Enviar mensajes
enviados = set()
for index, row in df.iterrows():
    numero = str(row["numero"])
    mensaje = str(row["mensaje"])

    if numero in enviados:
        continue  # 🚫 evita duplicados dentro del Excel

    payload = {"to": numero, "text": mensaje}
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"✅ Enviado a {numero}: {response.text}")
    except Exception as e:
        print(f"❌ Error al enviar a {numero}: {e}")

    enviados.add(numero)
    
    # ⏳ Espera de 60 segundos por restricción de
