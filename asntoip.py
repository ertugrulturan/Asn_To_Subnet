import requests
import ipaddress

def get_ipv4_addresses(asn):
    url = f"https://api.bgpview.io/asn/{asn}/prefixes"
    response = requests.get(url)
    data = response.json()

    prefixes = data['data']['ipv4_prefixes']
    ipv4_addresses = []

    for prefix in prefixes:
        network = ipaddress.IPv4Network(prefix['prefix'])
        for ip in network:
            ipv4_addresses.append(str(ip))

    return ipv4_addresses

def write_to_file(ip_addresses, filename):
    with open(filename, 'w') as file:
        for ip in ip_addresses:
            file.write(ip + '\n')

def main():
    asn = input("ASN adresini girin: ")
    ip_addresses = get_ipv4_addresses(asn)
    write_to_file(ip_addresses, 'out.txt')
    print(f"{len(ip_addresses)} IPv4 adresi out.txt dosyasına yazıldı.")

if __name__ == '__main__':
    main()
