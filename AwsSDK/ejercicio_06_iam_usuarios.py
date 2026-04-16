import boto3

iam = boto3.client("iam")

USUARIOS = ["dev-usuario1", "dev-usuario2"]
POLITICA_ARN = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"


def crear_usuario(nombre):
    iam.create_user(UserName=nombre)
    print(f"Usuario creado: {nombre}")


def asignar_politica(nombre, politica_arn):
    iam.attach_user_policy(UserName=nombre, PolicyArn=politica_arn)
    print(f"Política asignada a {nombre}: {politica_arn}")


def generar_access_key(nombre):
    respuesta = iam.create_access_key(UserName=nombre)
    clave = respuesta["AccessKey"]
    print(f"Access Key ID: {clave['AccessKeyId']}")
    print(f"Secret Access Key: {clave['SecretAccessKey']}")


for usuario in USUARIOS:
    crear_usuario(usuario)
    asignar_politica(usuario, POLITICA_ARN)
    generar_access_key(usuario)
    print()
