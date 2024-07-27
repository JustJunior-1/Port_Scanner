import socket

def scan_ports(ip):
    open_ports = []
    for port in range(1, 1025):  # Scanning ports from 1 to 1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    open_ports = scan_ports(target_ip)
    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}.")
