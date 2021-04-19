from netmiko import ConnectHandler
from getpass import getpass

device_1= {
    "host":'cisco3.lasthop.io',
    "username":'pyclass',
    "password":getpass(),
    "device_type":'cisco_xe',
    "session_log":'my_session.txt'
}
net_connect = ConnectHandler(**device_1)
print(net_connect.find_prompt())

