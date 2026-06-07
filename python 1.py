import socket
import sys

target = input("Enter Target IP: ")

print("-" * 50)
print(f"Scanning Target: {target}")
print("-" * 50)

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program...")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved...")
    sys.exit()
except socket.error:
    print("\n Server not responding...")
    sys.exit()

print("-" * 50)
print("Scan Completed.")
