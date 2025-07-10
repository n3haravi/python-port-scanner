import socket
import threading
from datetime import datetime

# Ask user for input
target = input("Enter target IP or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# Resolve hostname to IP
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    exit()

print(f"\nStarting scan on {target} ({ip}) from port {start_port} to {end_port}...")
print("Time started:", datetime.now().strftime("%H:%M:%S"))
print("-" * 40)

# Open ports list
open_ports = []

# Define the scanning function
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
        open_ports.append(port)
    s.close()

# Launch threads
threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Save to file
filename = f"scan_results_{ip.replace('.', '_')}.txt"
with open(filename, "w") as f:
    f.write(f"Open ports on {target} ({ip}):\n")
    for port in open_ports:
        f.write(f"Port {port} is OPEN\n")

print("-" * 40)
print("Scan complete.")
print("Time ended:", datetime.now().strftime("%H:%M:%S"))
print(f"\nResults saved to {filename}")
