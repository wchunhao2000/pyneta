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
command = 'delete  bootflash:/test_file1.txt'
output =  net_connect.send_command(command, expect_string=r'test_file1.txt')
output +=  net_connect.send_command('test_file1.txt', expect_string=r'confirm')
output +=  net_connect.send_command('y', expect_string=r'#') 
print (output)
