"""Simple script used for backups"""
import os
import re
import napalm


PASS = os.getenv("MY_PASS")

devices = [
    {
        "hostname": "pdx-rtr-vios-01",
        "device_type": "ios",
        "host": "192.168.10.122",
        "username": "admin",
        "password": PASS,
    },
    {
        "hostname": "pdx-rtr-veos-01",
        "device_type": "eos",
        "host": "192.168.10.151",
        "username": "admin",
        "password": PASS,
    },
]


for device in devices:
    driver = napalm.get_network_driver(device["device_type"])
    temp_device = driver(
        hostname=device["host"],
        username=device["username"],
        password=device["password"],
    )
    temp_device.open()
    config = temp_device.get_config(retrieve="running")
    run_conf = config["running"]

    ### create file with running config in backup_config folder
    with open(
        f"./snapshots/configs/{device['hostname']}.txt", "w", encoding="utf-8"
    ) as file:
        file.write(run_conf)
    temp_device.close()
