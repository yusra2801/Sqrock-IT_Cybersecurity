

import whois
import socket
import requests
def osint_scan(domain):
    print("=" * 50)
    print("OSINT Scanner")
    print("=" * 50)
    print("\n[+] WHOIS Information")
try:
     whois_data = whois.whois(domain)
     print("Registrar:" , whois_data.register)
     print("Creation Date:" , whois_data.creation_date)
     print("Expiration Date:" , whois_data.expiration_date)
except Exception as e:
    print("WHOIS Lookup failed:" , e)
    print("\n[+] IP Address")
    try:
        ip_address = socket.gethostbyname(domain)
        print("IP Address:" , ip_address)
    except Exception as e:
        print("IP Lookup failed: " , e)
    print("\n[+] IP Geolocation")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        geo_data = response.json()
        print("Country:" ,geo_data.get("country"))
        print("city:" , geo_data.get("city"))
        print("ISP:" , geo_data.get("isp"))
    except Exception as e:
        print("GeoLocation lookup failed:" , e)
        print("\n[+] DNS Information")
    try:
       hostname = socket.gethostbyaddr(ip_address)
       print("Hostname:" , hostname[0])
       print("Aliases:" , hostname[1])
    except Exception as e:
        print("DNS Lookup failed:" , e)
    print("\n[+] HTTP/HTTPS Information")
    try:
        response = requests.get(f"https://{domain}", timeout=10)
        print("HTTP Status Code:" , response.status_code)
        print("Server:" , response.headers.get("Server"))
        print("Content-type:" , response.headers.get("Content-type"))
    
    except Exception as e:
        print("HTTP/HTTPS Lookup failed:" , e)

domain = input("Enter Domain:")
osint_scan(domain)
