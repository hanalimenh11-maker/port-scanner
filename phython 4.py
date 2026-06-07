import netifaces

def get_gateway_ip():
    try:
       
        gws = netifaces.gateways()
        
        gateway_ip = gws['default'][netifaces.AF_INET][0]
        return gateway_ip
    except Exception as e:
        print(f"[-] Error retrieving gateway: {e}")
        return None

def determine_ip_class(ip_address):
    
    first_octet = int(ip_address.split('.')[0])
    
    if 1 <= first_octet <= 126:
        return "Class A"
    elif first_octet == 127:
        return "Loopback Address (Class A Range)"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental/Reserved)"
    else:
        return "Invalid IP range"

if __name__ == "__main__":
    print("[*] Discovering network gateway details...")
    gateway = get_gateway_ip()
    
    if gateway:
        print(f"[+] Gateway IP Address: {gateway}")
        ip_class = determine_ip_class(gateway)
        print(f"[+] IP Class: {ip_class}")
    else:
        print("[-] Could not find the default gateway.")
