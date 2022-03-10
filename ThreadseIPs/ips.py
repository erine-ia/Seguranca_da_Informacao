import ipaddress
#ip = '192.168.0.1' # ->ip

ip = '192.168.0.0/24' # -> Além do ip o endereço de rede(24)

rede = ipaddress.ip_network(ip, strict = False)
#imprimir todos os ips da rede:
for ip in rede:
    print(ip)