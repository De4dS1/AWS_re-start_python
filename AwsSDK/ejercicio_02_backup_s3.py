import boto3
import os
from datetime import datetime

BUCKET = "mi-bucket-backups"
CARPETA_LOCAL = "./datos"

s3 = boto3.client("s3")
fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
prefijo = f"backup_{fecha}/"


def hacer_backup(carpeta):
    for nombre_archivo in os.listdir(carpeta):
        ruta_local = os.path.join(carpeta, nombre_archivo)
        if os.path.isfile(ruta_local):
            clave_destino = prefijo + nombre_archivo
            s3.upload_file(ruta_local, BUCKET, clave_destino)
            print(f"Subido: {clave_destino}")


hacer_backup(CARPETA_LOCAL)
print(f"Backup completado en: s3://{BUCKET}/{prefijo}")
