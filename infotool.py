import sys
import socket
import requests
import json

def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        print("Error: Invalid domain.")
        sys.exit(1)

def get_location_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch location information.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python infotool.py <websiteurl>")
        sys.exit(1)

    domain = sys.argv[1]
    ip_address = get_ip_address(domain)
    print(f"IP Address: {ip_address}")

    location_info = get_location_info(ip_address)
    print(json.dumps(location_info, indent=4))

