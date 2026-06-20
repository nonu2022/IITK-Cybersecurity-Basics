import socket

target_host = "localhost" # Scans your own machine safely
ports_to_scan = [21, 22, 80, 443] # FTP, SSH, HTTP, HTTPS ports

print(f"Scanning target: {target_host}")
for port in ports_to_scan:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0) # Move on quickly if no response
    result = s.connect_ex((target_host, port))
    if result == 0:
        print(f"🚪 Port {port}: OPEN")
    s.close()
