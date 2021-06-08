from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}

net_connect = ConnectHandler(**device1)
#print(net_connect.find_prompt())

arp = net_connect.send_command("show ip arp", use_textfsm=True) 
#print (arp)

for arp_entry in arp:
    print('#'*15)
    print('mac_addr:',arp_entry['mac'])
    print('ip_addr',arp_entry['address'])
    print('interface',arp_entry['interface'])
    print('#'*15)
    print()
net_connect.disconnect()


