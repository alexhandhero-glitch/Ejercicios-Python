def validar_ip(ip):
   
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:
            return False

    return True


class Dispositivo:
   
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip
        self.estado = "apagado"

    def encender(self):
        self.estado = "encendido"
        print(f"{self.nombre} ha sido encendido.")

    def mostrar_info(self):
        print("----- Informacion del dispositivo -----")
        print(f"Nombre : {self.nombre}")
        print(f"IP     : {self.ip}")
        print(f"Estado : {self.estado}")


router1 = Dispositivo("Router-Principal", "192.168.1.1")
router1.encender()
router1.mostrar_info()

ip_buena = "192.168.1.1"
ip_mala = "300.168.1.999"

print(f"\n¿'{ip_buena}' es valida? -> {validar_ip(ip_buena)}")
print(f"¿'{ip_mala}' es valida? -> {validar_ip(ip_mala)}")
