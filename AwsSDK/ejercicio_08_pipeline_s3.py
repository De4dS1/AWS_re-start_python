import boto3

BUCKET_ORIGEN = "bucket-entrada"
BUCKET_DESTINO = "bucket-salida"
ARCHIVO_ORIGEN = "datos/archivo.txt"
ARCHIVO_RESULTADO = "resultados/resultado.txt"

s3 = boto3.client("s3")


def subir_archivo(ruta_local, bucket, clave):
    s3.upload_file(ruta_local, bucket, clave)
    print(f"Archivo subido a s3://{bucket}/{clave}")


def leer_contenido(bucket, clave):
    respuesta = s3.get_object(Bucket=bucket, Key=clave)
    contenido = respuesta["Body"].read().decode("utf-8")
    return contenido


def procesar(contenido):
    lineas = contenido.splitlines()
    total_lineas = len(lineas)
    total_palabras = sum(len(l.split()) for l in lineas)
    return f"Líneas: {total_lineas}\nPalabras: {total_palabras}\n"


def guardar_resultado(bucket, clave, texto):
    s3.put_object(Bucket=bucket, Key=clave, Body=texto.encode("utf-8"))
    print(f"Resultado guardado en s3://{bucket}/{clave}")


subir_archivo("archivo.txt", BUCKET_ORIGEN, ARCHIVO_ORIGEN)
contenido = leer_contenido(BUCKET_ORIGEN, ARCHIVO_ORIGEN)
resultado = procesar(contenido)
print(resultado)
guardar_resultado(BUCKET_DESTINO, ARCHIVO_RESULTADO, resultado)
