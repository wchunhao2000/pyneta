from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_xe',
    "global_delay_factor":2
}

start_time = datetime.now()
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show lldp neighbors detail") #, delay_factor=8)

print (output)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
