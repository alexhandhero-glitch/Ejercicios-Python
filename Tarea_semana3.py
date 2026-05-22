# Ejercicio 1. ¿Es el protocolo seguro?
protocolo = "HTTPS"
if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP":
    print(f"El protocolo {protocolo} es SEGURO")
elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":
    print(f"El protocolo {protocolo} es INSEGURO")
else:
    print("Desconocido")

# Ejercicio 2. Identificar el servicio según el puerto
puerto = 443
if puerto == 22: servicio = "SSH"
elif puerto == 80: servicio = "HTTP"
elif puerto == 443: servicio = "HTTPS"
elif puerto == 3306: servicio = "MySQL"
elif puerto == 3389: servicio = "RDP"
else: servicio = "Servicio desconocido"
print(f"Puerto {puerto}: {servicio}")

# Ejercicio 3. Listar IPs de una subred
for i in range(8):
    print(f"192.168.1.{i}")

# Ejercicio 4. Inventario numerado
dispositivos = ["Router Cisco", "Switch HP", "Firewall Fortinet", "Servidor Dell"]
for posicion, valor in enumerate(dispositivos, start=1):
    print(f"{posicion}. {valor}")

# Ejercicio 5. Cuenta regresiva de apagado
contador = 5
while contador >= 1:
    print(f"Apagado en: {contador}")
    contador -= 1
print("Apagando servidor...")

# Ejercicio 6. Reintento de conexión
intento = 1
conectado = False
while intento <= 5 and not conectado:
    print(f"Intento {intento}: sin respuesta")
    if intento == 3:
        conectado = True
        print("CONECTADO")
    intento += 1

# Ejercicio 7. Primer puerto cerrado
puertos = [21, 22, 23, 25, 80]
estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]
for p, e in zip(puertos, estados):
    print(f"Puerto {p}: {e}")
    if e == "cerrado":
        print(f"Primer puerto cerrado: {p}")
        break

# Ejercicio 8. Filtrar IPs de la lista negra
ips_log = ["10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156", "10.0.0.10"]
blacklist = ["200.0.0.1", "45.33.32.156"]
total = 0
for ip in ips_log:
    if ip in blacklist:
        continue
    print(f"Procesando: {ip}")
    total += 1
print(f"Total procesadas: {total}")

# Ejercicio 9. Buscar dispositivo en inventario
inventario = ["Router-01", "Switch-A", "Firewall-FW1", "Servidor-Web"]
buscar = "Firewall-FW1"
for d in inventario:
    if d == buscar:
        print("Encontrado")
        break
else:
    print("No encontrado en el inventario")

# Ejercicio 10. Validador de dirección IPv4
def validar_ip(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return "Invalida (faltan octetos)"
    for octeto in partes:
        if not octeto.isdigit():
            return "Invalida (no numerico)"
        if not (0 <= int(octeto) <= 255):
            return "Invalida (octeto fuera de rango)"
    return "Valida"

print(f"192.168.1.1: {validar_ip('192.168.1.1')}")