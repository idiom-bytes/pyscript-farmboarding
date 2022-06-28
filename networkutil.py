import os
from enforce_typing import enforce_types

_BARGE_ADDRESS_FILE = "~/.ocean/ocean-contracts/artifacts/address.json"

# Development chainid is from brownie, rest are from chainlist.org
# Chain values to fit Ocean subgraph urls as given in
# https://v3.docs.oceanprotocol.com/concepts/networks/
_CHAINID_TO_NETWORK = {
    8996: "development",  # ganache
    1: "mainnet",
    3: "ropsten",
    4: "rinkeby",
    56: "bsc",
    137: "polygon",
    246: "energyweb",
    1287: "moonbase",
    1285: "moonriver",
    80001: "mumbai",
}
_NETWORK_TO_CHAINID = {
    network: chainID for chainID, network in _CHAINID_TO_NETWORK.items()
}

DEV_CHAINID = _NETWORK_TO_CHAINID["development"]

@enforce_types
def getAddressFile() -> str:  # pylint: disable=unused-argument
    """Returns the address file for a given chainID"""
    return os.path.expanduser(_BARGE_ADDRESS_FILE)

@enforce_types
def chainIdToSubgraphUri(chainID: int) -> str:
    """Returns the subgraph URI for a given chainID"""
    sg = "/subgraphs/name/oceanprotocol/ocean-subgraph"
    if chainID == DEV_CHAINID:
        return "http://127.0.0.1:9000" + sg

    network_str = chainIdToNetwork(chainID)
    return f"https://v4.subgraph.{network_str}.oceanprotocol.com" + sg

@enforce_types
def chainIdToNetwork(chainID: int) -> str:
    """Returns the network name for a given chainID"""
    return _CHAINID_TO_NETWORK[chainID]

@enforce_types
def networkToChainId(network: str) -> int:
    """Returns the chainID for a given network name"""
    return _NETWORK_TO_CHAINID[network]