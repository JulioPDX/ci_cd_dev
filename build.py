#!/usr/bin/env python

"""Script used to configure the network"""

import argparse
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result
from tools import nornir_set_creds


parser = argparse.ArgumentParser()
parser.add_argument(
    "--dry_run", dest="dry", action="store_true", help="Will not run on devices"
)
parser.add_argument(
    "--no_dry_run", dest="dry", action="store_false", help="Will run on devices"
)
parser.set_defaults(dry=True)
args = parser.parse_args()


def deploy_network(task):
    """Configures network with NAPALM"""
    task1_result = task.run(
        name=f"Configuring {task.host.name}!",
        task=napalm_configure,
        filename=f"./snapshots/configs/{task.host.name}.txt",
        dry_run=args.dry,
        replace=True,
    )


def main():
    """Used to run all the things"""
    norn = InitNornir(config_file="configs/config.yaml", core={"raise_on_error": True})
    nornir_set_creds(norn)
    result = norn.run(task=deploy_network)
    print_result(result)


if __name__ == "__main__":
    main()
