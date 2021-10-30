#!/usr/bin/env python
"""Script used to configure the network"""
import argparse
from rich import print as rprint
from rich import inspect
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result
from tools import nornir_set_creds


parser = argparse.ArgumentParser()
# Returns True if argument is set.
# If missing then will run on production.
parser.add_argument("--dry_run", type=bool, help="To be or not to be")
args = parser.parse_args()


def deploy_network(task):
    """Configures network with NAPALM and retrives backup for comparison"""
    task1_result = task.run(
        name=f"Configuring {task.host.name}!",
        task=napalm_configure,
        filename=f"./snapshots/configs/{task.host.name}.txt",
        dry_run=args.dry_run,
        replace=True,
    )


def main():
    """Used to run all the things"""
    norn = InitNornir(config_file="configs/config.yaml")
    nornir_set_creds(norn)
    result = norn.run(task=deploy_network)
    print_result(result)


if __name__ == "__main__":
    main()
