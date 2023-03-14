This file tries to summarise what the group has been discussing so far, as I could not atttend much meetings, I went through the minutes and write some summary here. I hope it can help onboarding new people in the group.

# Electrophy data and BEP032  

The group has been discussing how to use the power of nwb and nix format, while having a BIDS format.

## Type of data

patch clamp data is included in bep032
`Microelectrode Recordings` ( BEP0206) may be a special case of electrophysiology ? BEP 026 and 032 to be merge.

##  Files combinations

- BIDS requires different data files for different modalities (electrophy data, behavior recording, ..., meaning different data collection equipment) , while nwb/nix combine them.
- Several sessions/run will be included in nix/nwb, BIDS should get session specific files

Proposed restrictions for NWB / NIX files as they would be used in BIDS:
- can not contain multiple modalities
- can not contain data from multiple (BIDS) sessions
- should be accompanied by one sidecar file (which can contain a hierarchical structure)

## Dealing with runs

One session may include different experimental "runs".

## links to minutes files

- https://docs.google.com/document/d/1LCsv8ADHjpcKekyOWN-GdK5UHLqfHU5zlfltF9GRy_E/edit#
- https://docs.google.com/document/d/1sMriiVU2krFXelqokvfm-pySPPZEN9JwUId9rdXYLdk/edit
- October 2021 missing
- https://docs.google.com/document/d/1jwY6TQuqQS6JUxSlATlZGKwMit6PdMSI4T783cioWOc/edit
- https://docs.google.com/document/d/1wO3sHujMj7TLCdX_Gyl8CpIv1huJ1TEyFumsNJFj3mE/edit
- https://docs.google.com/document/d/1U20ficIxX3Vo8sZmvkXX9UBePVf5LEpY5ss5U4WRGuM/edit#heading=h.o1scycxdhill
- https://docs.google.com/document/d/1XNxNnd3Mvk4wy9XyPEMJ589vwnVLCnQkWIA2cP2T7sI
- https://docs.google.com/document/d/102DKnNvS06ru8UoSzJtCUagkYv-y3u7HQwZ_POPDlq4/edit?usp=sharing
- https://docs.google.com/document/d/1O-Xun_2tDVjXw9BFH_w57L7jyeXPYqS0YxMubZMpIYk/edit?usp=sharing
- https://docs.google.com/document/d/1cZroLI9ySQGMxw9k8lMKBMYVoE7IQqnUVc18KDEZ6bU/edit
- https://docs.google.com/document/d/1RsFNrqPhkHwrzz4QOJWirqvDNsrqRZDqfgOg6RAi4yk/edit
- https://docs.google.com/document/d/1_HC4Yo7JkR9jhMSRCXhbyI19Cf4SVO5x0L6eZiaKTvg/edit
