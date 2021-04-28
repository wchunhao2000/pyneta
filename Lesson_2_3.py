from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show version", use_textfsm=True) 
output += net_connect.send_command("show lldp neighbors detail", use_textfsm=True)
print (output)

net_connect.disconnect()


