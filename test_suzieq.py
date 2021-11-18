#!/usr/bin/env python

"""Script used to interact with Suzieq Poller"""

import sys
import pandas as pd
from suzieq.sqobjects import get_sqobject
from rich.console import Console


console = Console(color_system="truecolor")

# OSPF Testing
ospf_tbl = get_sqobject("ospf")
ospf_df = pd.DataFrame(ospf_tbl().aver())
ospf_fail = 0
for index, row in ospf_df.iterrows():
    if row["assert"] != "pass":
        console.print(
            f":triangular_flag_on_post: OSPF, {row['hostname']} {row['ifname']} {row['assertReason']} :triangular_flag_on_post:"
        )
        ospf_fail += 1

# BGP testing
bgp_tbl = get_sqobject("bgp")
bgp_df = pd.DataFrame(bgp_tbl().get())
bgp_fail = 0
for index, row in bgp_df.iterrows():
    if row["state"] != "Established":
        console.print(
            f":triangular_flag_on_post: {row['hostname']}(AS {row['asn']}) to {row['peer']}(AS {row['peerAsn']}) is in {row['state']} state :triangular_flag_on_post:"
        )
        bgp_fail += 1

if bgp_fail == 0:
    console.print(
        ":white_heavy_check_mark: All BGP checks passed :white_heavy_check_mark:"
    )
if ospf_fail == 0:
    console.print(
        ":white_heavy_check_mark: All OSPF checks passed :white_heavy_check_mark:"
    )
if bgp_fail or ospf_fail != 0:
    sys.exit(1)
