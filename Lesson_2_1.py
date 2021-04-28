from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_xe',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'ping'
output = net_connect.send_command(command, expect_string=r'ip',strip_prompt=False,strip_command=False)
output += net_connect.send_command('ip', expect_string=r'Target')
output += net_connect.send_command('8.8.8.8', expect_string=r'5',strip_prompt=False, strip_command=False)
output += net_connect.send_command('5', expect_string=r'100')
output += net_connect.send_command('100', expect_string=r'2')
output += net_connect.send_command('2', expect_string=r'n')
output += net_connect.send_command('n', expect_string=r'n')
output += net_connect.send_command('n', expect_string=r'#')

print (output)
