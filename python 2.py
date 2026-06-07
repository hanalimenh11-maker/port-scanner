import nmap

target_host = input("Enter target IP: ")
port_range = input("Enter port range (e.g., 20-80 or 80,443): ")

print(f"\n[*] Starting Nmap scan on: {target_host}")
print("-" * 50)

try:
    
    nm = nmap.PortScanner()
    
  
    nm.scan(target_host, port_range, arguments='-v')
    
    
    for host in nm.all_hosts():
        print(f"[+] Host: {host} ({nm[host].hostname()})")
        print(f"[+] State: {nm[host].state()}")
        
     
        for protocol in nm[host].all_protocols():
            print(f"[*] Protocol: {protocol}")
            
            ports = nm[host][protocol].keys()
            for port in sorted(ports):
                state = nm[host][protocol][port]['state']
                service = nm[host][protocol][port]['name']
                print(f"  -> Port: {port}\tState: {state}\tService: {service}")


except Exception as e:
    print(f"\n[!] Error occurred: {e}")
    sys.exit()

print("-" * 50)
print("[*] Nmap Scan Completed.")
