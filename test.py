#!/usr/bin/env python
"""Script used to test the network with batfish"""

from pybatfish.client.commands import *
from pybatfish.question import load_questions
from pybatfish.question import bfq
from rich import print as rprint


def test_bgp_status():
    """Checking BGP status"""
    assert (
        bfq.bgpSessionStatus()
        .answer()
        .frame()
        .query("Established_Status != 'ESTABLISHED'")
        .empty
    )


def test_ospf_status():
    """Checking OSPF status"""
    assert (
        bfq.ospfSessionCompatibility()
        .answer()
        .frame()
        .query("Session_Status != 'ESTABLISHED'")
        .empty
    )


def init_bf():
    """init all the things"""
    NETWORK_NAME = "PDX_NET"
    SNAPSHOT_NAME = "snapshot00"
    SNAPSHOT_DIR = "./snapshots"

    bf_session.host = "192.168.10.184"
    bf_set_network(NETWORK_NAME)
    bf_init_snapshot(SNAPSHOT_DIR, name=SNAPSHOT_NAME, overwrite=True)
    load_questions()

init_bf()