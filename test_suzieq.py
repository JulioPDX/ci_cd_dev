#!/usr/bin/env python

import sys
import pandas as pd
from suzieq.sqobjects import get_sqobject
from rich import print, inspect


# OSPF Testing
ospf_tbl = get_sqobject("ospf")
ospf_df = pd.DataFrame(ospf_tbl().get())
ospf_fail = 0
for index, row in ospf_df.iterrows():
    if row["adjState"] != "passive":
        if row["adjState"] != "full":
            print(
                f"{row['hostname']} to area {row['area']} peer is in {row['adjState']} state"
            )
            ospf_fail += 1

# BGP testing
bgp_tbl = get_sqobject("bgp")
bgp_df = pd.DataFrame(bgp_tbl().get())
bgp_fail = 0
for index, row in bgp_df.iterrows():
    if row["state"] != "Established":
        print(
            f"{row['hostname']}(AS {row['asn']}) to {row['peer']}(AS {row['peerAsn']}) is in {row['state']} state"
        )
        bgp_fail += 1

if bgp_fail == 0:
    print("All BGP checks passed")
if ospf_fail == 0:
    print("All OSPF checks passed")
if bgp_fail or ospf_fail != 0:
    sys.exit(1)
