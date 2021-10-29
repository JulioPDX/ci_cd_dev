#!/usr/bin/env python
"""Script used to test the network with batfish"""

from pybatfish.client.commands import *
from pybatfish.question import load_questions
from pybatfish.client.asserts import (
    assert_no_duplicate_router_ids,
    assert_no_incompatible_bgp_sessions,
    assert_no_incompatible_ospf_sessions,
    assert_no_unestablished_bgp_sessions,
    assert_no_undefined_references,
)
from rich import print as rprint


def test_duplicate_rtr_ids(snap):
    """Testing for duplicate router IDs"""
    rprint("[bold yellow]Testing for duplicate router IDs")
    assert_no_duplicate_router_ids(
        snapshot=snap,
        protocols={"ospf", "bgp"},
    )
    rprint("[bold green]No duplicate router IDs found")


def test_bgp_compatibility(snap):
    """Testing for incompatible BGP sessions"""
    rprint("[bold yellow]Testing for incompatible BGP sessions")
    assert_no_incompatible_bgp_sessions(
        snapshot=snap,
    )
    rprint("[bold green]All BGP sessions compatible!")


def test_ospf_compatibility(snap):
    """Testing for incompatible OSPF sessions"""
    rprint("[bold yellow]Testing for incompatible OSPF sessions")
    assert_no_incompatible_ospf_sessions(
        snapshot=snap,
    )
    rprint("[bold green]All OSPF sessions compatible!")


def test_bgp_unestablished(snap):
    """Testing for BGP sessions that are not established"""
    rprint("[bold yellow]Testing for unestablished BGP sessions")
    assert_no_unestablished_bgp_sessions(
        snapshot=snap,
    )
    rprint("[bold green]All BGP sessions are established!")


def test_undefined_references(snap):
    """Testing for any undefined references"""
    rprint("[bold yellow]Testing for undefined references")
    assert_no_undefined_references(
        snapshot=snap,
    )
    rprint("[bold green]No undefined refences found!")


def main():
    """init all the things"""
    NETWORK_NAME = "PDX_NET"
    SNAPSHOT_NAME = "snapshot00"
    SNAPSHOT_DIR = "./snapshots"
    bf_session.host = "192.168.10.184"
    bf_set_network(NETWORK_NAME)
    init_snap = bf_init_snapshot(SNAPSHOT_DIR, name=SNAPSHOT_NAME, overwrite=True)
    load_questions()
    test_duplicate_rtr_ids(init_snap)
    test_bgp_compatibility(init_snap)
    test_ospf_compatibility(init_snap)
    test_bgp_unestablished(init_snap)
    test_undefined_references(init_snap)


if __name__ == "__main__":
    main()
