import boto3

ec2 = boto3.client("ec2")


def listar_instancias():
    respuesta = ec2.describe_instances()
    for reserva in respuesta["Reservations"]:
        for instancia in reserva["Instances"]:
            instance_id = instancia["InstanceId"]
            estado = instancia["State"]["Name"]
            tipo = instancia["InstanceType"]
            ip_publica = instancia.get("PublicIpAddress", "Sin IP pública")
            print(f"ID: {instance_id} | Estado: {estado} | Tipo: {tipo} | IP: {ip_publica}")


listar_instancias()
