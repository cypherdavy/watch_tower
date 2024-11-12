import shodan
import re
import sys
import time

def display_logo():
    logo = """
    -=Watchtower=-
    
                 ℃ↂ_ↂↃ 
              _   _               
           [_]_[_]_[_]_[_]_[_]
           [__j__j__j__j__j__]
             [_j__j__j__j__]
             [__j__j__j__j_]
             [_j__j/V\\_j__j]
             [__j_// \\\\__j_]
             [_j__|   |_j__]
             [__j_|___|__j_]
             [_j__j__j__j__]
             [__j__j__j__j_]
     _   _   _  [_j__j__j__j__]  _   _   _   _
    [_]_[_]_[_]_[__j__j__j__j_]_[_]_[_]_[_]_[_]_
      _j__j__j__j[_j__j__j__j__]j__j__j__j__j_
         j  j  j [  j  j  j  j ] j  j  j  j    hjw

    =============================================
        🌐 Welcome to the WATCHTOWER Tool 🌐
    =============================================
    
    This tool allows you to check details on authorized CCTV IPs using Shodan.
    ** Use responsibly on devices/IPs you have permission to scan **
    """
    print(logo)
    print("\nLet's get started!\n")

def get_api_key():
    api_key = input("🔑 Enter your Shodan API key: ").strip()
    if not api_key:
        print("❌ API Key cannot be empty!")
        sys.exit(1)
    return api_key

def get_authorized_ips():
    ips = input("📡 Enter authorized IP addresses separated by commas: ").split(',')
    validated_ips = [ip.strip() for ip in ips if validate_ip(ip.strip())]
    if not validated_ips:
        print("❌ No valid IP addresses were entered!")
        sys.exit(1)
    return validated_ips

def validate_ip(ip):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if ip_pattern.match(ip):
        return True
    else:
        print(f"❌ Invalid IP format detected: {ip}")
        return False

def display_device_info(result):
    print(f"\n[+] Device IP: {result['ip_str']}")
    print(f"    Organization: {result.get('org', 'N/A')}")
    print(f"    Operating System: {result.get('os', 'N/A')}")
    print(f"    Country: {result.get('country_name', 'N/A')}")
    print(f"    ISP: {result.get('isp', 'N/A')}")
    
    for item in result['data']:
        print(f"\n    [Port: {item['port']}]")
        print(f"    - Banner: {item['data'][:100]}")
        print(f"    - Service: {item.get('product', 'Unknown')}")
        
        if 'web' in item.get('product', '').lower():
            print(f"    - Access Link (if authorized): http://{result['ip_str']}:{item['port']}/")

def search_shodan(api_key, authorized_ips):
    try:
        api = shodan.Shodan(api_key)
        print("\n🔍 Starting WatchTower CCTV Scan...")

        for ip in authorized_ips:
            print(f"\n🌐 Searching Shodan for IP: {ip}")
            result = api.host(ip)
            display_device_info(result)
            print("✔️ Scan complete for this IP.")
            
    except shodan.APIError as e:
        print(f"❌ Shodan API Error: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def main():
    display_logo()
    api_key = get_api_key()
    authorized_ips = get_authorized_ips()

    if not api_key or not authorized_ips:
        print("❌ Error: Shodan API key and at least one authorized IP address are required.")
        return

    search_shodan(api_key, authorized_ips)

if __name__ == "__main__":
    main()
