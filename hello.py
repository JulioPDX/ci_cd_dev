"""Simple script used for testing deployments"""
import os
from rich import print as rprint

from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.10.122",
    "username": "admin",
    "password": os.getenv("MY_PASS"),
}

# Show command that we execute
COMMAND = "show ip int brief"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(COMMAND)

# Automatically cleans-up the output so that only the show output is returned
print()
rprint(output)
print()
