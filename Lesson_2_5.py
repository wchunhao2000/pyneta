from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": ' nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
}
device2 = {
       "host": ' nxos2.lasthop.io',
       "username": 'pyclass',
       "password": getpass(),
       "device_type": 'cisco_nxos',
  }
all_devices = [device1, device2]
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(config_file='config.txt')
    print (output)
    net_connect.disconnect()


