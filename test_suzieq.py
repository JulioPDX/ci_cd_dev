#!/usr/bin/env python

import sys
import pandas as pd
from suzieq.sqobjects import get_sqobject
from rich import print, inspect


# OSPF Testing
ospf_tbl = get_sqobject("ospf")
ospf_df = pd.DataFrame(ospf_tbl().get())
for row_label, row in ospf_df.iterrows():
    if row["adjState"] != "passive":
        if row["adjState"] != "full":
            print(ospf_tbl().aver())
            print(ospf_df.to_string())
            sys.exit(1)
        else:
            print(f"{row['hostname']} to {row['peerHostname']} is in state: {row['adjState']}")

# BGP testing
bgp_tbl = get_sqobject("bgp")
bgp_df = pd.DataFrame(bgp_tbl().get())
bgp_fail = 0
for row_label, row in bgp_df.iterrows():
    if row["state"] != "Established":
        print(
            f"{row['hostname']}(AS {row['asn']}) to {row['peer']}(AS {row['peerAsn']}) is in {row['state']} state"
        )
        bgp_fail += 1
if bgp_fail != 0:
    sys.exit(1)
else:
    print("All BGP checks passed")
