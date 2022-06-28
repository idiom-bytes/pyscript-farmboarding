from pprint import pprint

from examples.utils import networkutil, oceanutil
from examples.utils.graphutil import submitQuery

# TODO - embed/glue the logic here and just output a TVL value
CHAIN_IDS = [1, 56, 137, 246, 1285]
DEV_CHAIN_IDS = [3, 4, 1287, 80001]

def report():
    # TODO - Cycle through chains
    # TODO - Load all pools => SimplePool()
    # TODO - Sum all pool TVL => output

    # FROM test_thegraph.py
    # DataWhale ONDA - https://market.oceanprotocol.com/asset/did:op:ba8753de3a2715d05960092f35bc2c74a0d63bb4998a4fcb583bae60e335cf89
    DT = '0xF807cA842d8fB217FCF0a0DF8e84e447358C6e86'
    query = """
        {
          orders(where: {block_gte:0, block_lte:1000, datatoken:"%s"}, 
                 skip:0, first:5) {
            id,
            datatoken {
              id
            }
            lastPriceToken,
            lastPriceValue
            estimatedUSDValue,
            block
          }
        }
        """ % (
        DT
    )
    result = submitQuery(query, 137)
    pprint(result)