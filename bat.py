"""Script used for batfish testing and learning"""
import pandas as pd
from rich import print as rprint
from pybatfish.client.commands import *
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *
from pybatfish.question import *
from pybatfish.question import bfq

bf_session.host = "192.168.10.184"

NETWORK_NAME = "PDX_NET"
SNAPSHOT_NAME = "snapshot00"
SNAPSHOT_DIR = "./configs_compare"

bf_set_network(NETWORK_NAME)
bf_init_snapshot(SNAPSHOT_DIR, name=SNAPSHOT_NAME, overwrite=True)
load_questions()

bgp_sess_status = bfq.bgpSessionStatus().answer().frame()
rprint(bgp_sess_status)
