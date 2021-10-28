"""Script used to configure the network"""
from rich import print as rprint
from rich import inspect
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result
from tools import nornir_set_creds


def deploy_network(task):
    """Configures network with NAPALM and retrives backup for comparison"""
    task1_result = task.run(
        name=f"Configuring {task.host.name}!",
        task=napalm_configure,
        filename=f"./snapshots/configs/{task.host.name}.txt",
        dry_run=True,
        replace=True,
    )


def main():
    """Used to run all the things"""
    norn = InitNornir(config_file="configs/config.yaml")
    nornir_set_creds(norn, username="admin", password="SomethingSuper123")
    result = norn.run(task=deploy_network)
    print_result(result)


if __name__ == "__main__":
    main()
