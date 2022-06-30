import json

from enforce_typing import enforce_types

import networkutil
from constants import CONTRACTS

@enforce_types
def _contracts(chainID: int, key: str) -> str:
    """Returns the contract object at the currently connected network"""
    return CONTRACTS[chainID][key]

@enforce_types
def recordDevDeployedContracts(chainID: int):
    address_file = networkutil.getAddressFile()
    initContractAddresses(chainID, address_file)

# TODO - Not using brownie. Init to addresses if required for GQL
@enforce_types
def initContractAddresses(chainID: int, address_file: str):
    if chainID in CONTRACTS:  # already filled
        return

    network = networkutil.chainIdToNetwork(chainID)
    with open(address_file, "r") as json_file:
        a = json.load(json_file)[network]  # dict of contract_name: address

    C = {}
    C["Ocean"] = a["Ocean"]
    C["ERC721Template"] = a["ERC721Template"]["1"]
    C["ERC20Template"] = a["ERC20Template"]["1"]
    C["PoolTemplate"] = a["poolTemplate"]
    C["Router"] = a["Router"]
    C["Staking"] = a["Staking"]
    C["ERC721Factory"] = a["ERC721Factory"]
    C["FixedPrice"] = a["FixedPrice"]

    CONTRACTS[chainID] = C


def OCEANtoken(chainID: int):
    return _contracts(chainID, "Ocean")


def OCEAN_address(chainID: int) -> str:
    return OCEANtoken(chainID)


def ERC721Template(chainID: int):
    return _contracts(chainID, "ERC721Template")


def ERC20Template(chainID: int):
    return _contracts(chainID, "ERC20Template")


def PoolTemplate(chainID: int):
    return _contracts(chainID, "PoolTemplate")


def factoryRouter(chainID: int):
    return _contracts(chainID, "Router")


def Staking(chainID: int):
    return _contracts(chainID, "Staking")


def ERC721Factory(chainID: int):
    return _contracts(chainID, "ERC721Factory")

# TODO - Used in purgatory. Reliant on Brownie. NFT addy from poolShares is already checksummed
@enforce_types
def calcDID(nft_addr: str, chainID: int) -> str:
#     nft_addr2 = brownie.web3.toChecksumAddress(nft_addr)
#
#     # adapted from ocean.py/ocean_lib/ocean/ocean_assets.py
#     did = f"did:op:{create_checksum(nft_addr2 + str(chainID))}"
    return "did"
#
#
# # from ocean.py/ocean_lib/utils/utilities.py
# @enforce_types
# def create_checksum(text: str) -> str:
#     """
#     :return: str
#     """
#     return hashlib.sha256(text.encode("utf-8")).hexdigest()
