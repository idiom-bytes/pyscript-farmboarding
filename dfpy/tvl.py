# from pprint import pprint
#
# import networkutil, oceanutil, csvs, query
from dfpy.graphutil import submitQuery

# TODO - embed/glue the logic here and just output a TVL value
# CHAIN_IDS = [1, 56, 137, 246, 1285]
CHAIN_IDS = [1]
DEV_CHAIN_IDS = [3, 4, 1287, 80001]

"""
@description
Query all required data as part of dftools into a pandas df
Serve pandas df into frontend
"""

# TODO - Cycle through chains
# TODO - Load all pools => SimplePool()
# TODO - Sum all pool TVL => output
# @enforce_types
# def report():
#     HELP = f"""Query chain, output stakes & vols csvs
#
# Usage: dftool query ST FIN NSAMP CSV_DIR CHAINID
#   ST -- first block # to calc on | YYYY-MM-DD | YYYY-MM-DD_HH:MM
#   FIN -- last block # to calc on | YYYY-MM-DD | YYYY-MM-DD_HH:MM | latest
#   NSAMP -- # blocks to sample liquidity from, from blocks [ST, ST+1, .., FIN]
#   CSV_DIR -- output dir for stakes-CHAINID.csv and poolvols-CHAINID.csv
#   CHAINID -- {CHAINID_EXAMPLES}
#
# Uses these envvars:
# ADDRESS_FILE -- eg for barge: export ADDRESS_FILE={networkutil.chainIdToAddressFile(chainID=DEV_CHAINID)}
# """
#     if len(sys.argv) not in [2 + 5]:
#         print(HELP)
#         sys.exit(0)
#
#     # extract inputs
#     assert sys.argv[1] == "query"
#     ST, FIN, NSAMP = sys.argv[2], sys.argv[3], int(sys.argv[4])
#     CSV_DIR = sys.argv[5]
#     CHAINID = int(sys.argv[6])
#     print("dftool query: Begin")
#     print(
#         f"Arguments:\n "
#         f"\n ST={ST}\n FIN={FIN}\n NSAMP={NSAMP}"
#         f"\n CSV_DIR={CSV_DIR}"
#         f"\n CHAINID={CHAINID}"
#     )
#
#     # extract envvars
#     ADDRESS_FILE = _getAddressEnvvarOrExit()
#
#     if "-" in ST:
#         st_block = blocktime.timestrToBlock(chain, ST)
#     else:
#         st_block = int(ST)
#
#     if FIN == "latest":
#         fin_block = len(chain)
#     elif "-" in FIN:
#         fin_block = blocktime.timestrToBlock(chain, FIN)
#     else:
#         fin_block = int(FIN)
#
#     # main work
#     recordDeployedContracts(ADDRESS_FILE)
#     seed = fin_block
#     rng = blockrange.BlockRange(st_block, fin_block, NSAMP, seed)
#     (Pi, Si, Vi) = query.query_all(rng, CHAINID)
#     # csvs.savePoolinfoCsv(Pi, Si, Vi, CSV_DIR, CHAINID)
#     # csvs.saveStakesCsv(Si, CSV_DIR, CHAINID)
#     # csvs.savePoolvolsCsv(Vi, CSV_DIR, CHAINID)
#
#     print(f"Pi: {Pi}")
#     print(f"Si: {Si}")
#     print(f"Vi: {Vi}")

def report():
    for chainID in CHAIN_IDS :
        query = """
            {
              orders(first:1000) {
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
            """
        result = submitQuery(query, chainID)
        print(f"Number of orders onchainID {chainID} is: {len(result)}")