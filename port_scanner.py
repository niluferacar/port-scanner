# port_scanner.py
import socket
import time

print("🔍 Welcome to Simple Port Scanner")

# Kullanıcıdan hedef IP al
target = input("Enter the destination IP address: ").strip()
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\n🎯 {target} Initiating port scanning on target...\n")
time.sleep(1)

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # yarım saniye timeout
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} open")
    else:
        print(f"❌ Port {port} close")
    s.close()

print("\n📋 Scanning completed.")
