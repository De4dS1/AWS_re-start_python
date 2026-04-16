import boto3
import json

ec2 = boto3.client("ec2")
s3 = boto3.client("s3")
lambda_client = boto3.client("lambda")

inventario = {"ec2": [], "s3": [], "lambda": []}


def obtener_instancias_ec2():
    respuesta = ec2.describe_instances()
    for reserva in respuesta["Reservations"]:
        for inst in reserva["Instances"]:
            inventario["ec2"].append({
                "id": inst["InstanceId"],
                "tipo": inst["InstanceType"],
                "estado": inst["State"]["Name"],
            })


def obtener_buckets_s3():
    respuesta = s3.list_buckets()
    for bucket in respuesta["Buckets"]:
        inventario["s3"].append({
            "nombre": bucket["Name"],
            "creado": bucket["CreationDate"].isoformat(),
        })


def obtener_funciones_lambda():
    respuesta = lambda_client.list_functions()
    for func in respuesta["Functions"]:
        inventario["lambda"].append({
            "nombre": func["FunctionName"],
            "runtime": func["Runtime"],
            "memoria": func["MemorySize"],
        })


obtener_instancias_ec2()
obtener_buckets_s3()
obtener_funciones_lambda()

with open("aws_inventory.json", "w") as archivo:
    json.dump(inventario, archivo, indent=2)

print("Inventario guardado en aws_inventory.json")
