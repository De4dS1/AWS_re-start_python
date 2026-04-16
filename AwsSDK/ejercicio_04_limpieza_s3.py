import boto3
from datetime import datetime, timezone, timedelta

BUCKET = "mi-bucket"
DIAS_LIMITE = 30

s3 = boto3.client("s3")
limite = datetime.now(timezone.utc) - timedelta(days=DIAS_LIMITE)


def limpiar_archivos_antiguos():
    respuesta = s3.list_objects_v2(Bucket=BUCKET)
    objetos = respuesta.get("Contents", [])

    eliminados = 0
    for obj in objetos:
        if obj["LastModified"] < limite:
            s3.delete_object(Bucket=BUCKET, Key=obj["Key"])
            print(f"Eliminado: {obj['Key']} (modificado: {obj['LastModified'].date()})")
            eliminados += 1

    print(f"\nTotal eliminados: {eliminados}")


limpiar_archivos_antiguos()
