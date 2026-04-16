import boto3

BUCKET = "mi-bucket"
ARCHIVO_LOCAL = "archivo.txt"
ARCHIVO_DESTINO = "uploads/archivo.txt"

s3 = boto3.client("s3")


def subir_archivo(ruta_local, nombre_destino):
    s3.upload_file(ruta_local, BUCKET, nombre_destino)
    print(f"Archivo subido: {nombre_destino}")


def listar_archivos():
    respuesta = s3.list_objects_v2(Bucket=BUCKET)
    objetos = respuesta.get("Contents", [])
    for obj in objetos:
        print(f"  {obj['Key']}  ({obj['Size']} bytes)")


def descargar_archivo(nombre_origen, ruta_local):
    s3.download_file(BUCKET, nombre_origen, ruta_local)
    print(f"Archivo descargado: {ruta_local}")


subir_archivo(ARCHIVO_LOCAL, ARCHIVO_DESTINO)
listar_archivos()
descargar_archivo(ARCHIVO_DESTINO, "descargado.txt")
