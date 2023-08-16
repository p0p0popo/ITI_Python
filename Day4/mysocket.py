import socket

def check_host(host, port):
    try:
        # Create object form socket module
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        sock.settimeout(5)
        
        # Connect to the host by specific port
        sock.connect((host, port))
        
        # terminiate  the socket
        sock.close()
        
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False


host = "google.com"
port = 80

if check_host(host, port):
    print(f"{host}:{port} is reachable.")
else:
    print(f"{host}:{port} is not reachable.")

