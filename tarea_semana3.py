
# Ejercicio 1. ¿Es el protocolo seguro?
protocolo = "HTTPS"
if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP":
    print(f"El protocolo {protocolo} es SEGURO")
elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":
    print(f"El protocolo {protocolo} es INSEGURO")
else:
    print("Desconocido")