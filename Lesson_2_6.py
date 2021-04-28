from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host": ' cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "secret":getpass(),
    "device_type": 'cisco_ios',
    "session_log":"my_output.txt",
}
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
#output = net_connect.send_config_from_file(config_file='config.txt')
#print (output)
#net_connect.disconnect()


