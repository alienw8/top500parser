import json
from sys import argv
import ParserRequests
from GraphQL import Chain, SortBy, Parents
from Logger import log
from Token import Token


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def validate_args():
    args = ['', '', '', '']
    for i in range(1, 5):
        if len(argv) <= i:
            raise Exception(f'Argument {i} is none!')
        else:
            args[i - 1] = argv[i] if args[i - 1] != 'None' else None

    if args[0] is not None and args[0] not in Chain:
        raise Exception('Chain argument(1) not correct!')
    if args[1] is not None and not is_integer(args[1]):
        raise Exception('limit argument(2) not correct!')
    if args[2] is not None and args[2] not in SortBy:
        raise Exception('sort_by argument(3) not correct!')
    if args[3] is not None and args[3] not in Parents:
        raise Exception('parents argument(4) not correct!')
    return args


# USE
# Command: python app param1(Chain) param2(Limit) param3(SortBy) param4(Parents)
# Example: python app ETHEREUM 100 ONE_DAY_VOLUME None
# Params:
#   Chain:
#       All Chains  = None
#       Ethereum    = ETHEREUM
#       Matic       = MATIC
#       Klaytn      = KLAYTN
#   Limit:
#       integer number
#   SortBy:
#       Last Day Hours      = ONE_DAY_VOLUME
#       Last Seven Days     = SEVEN_DAY_VOLUME
#       Last Thirty Days    = THIRTY_DAY_VOLUME
#       All Time            = TOTAL_VOLUME
#   Parents:
#       All Categories          = None
#       New                     = None
#       Art                     = art
#       Domain Names            = domain-names
#       Music                   = music
#       Photography Category    = photography-category
#       Sports                  = sports
#       Trading Cards           = trading-cards
#       Utility                 = utility
#       Virtual Worlds          = virtual-worlds
if __name__ == "__main__":
    log('Start')
    chain, limit, sort_by, parents = validate_args()

    tokens: list[Token] = ParserRequests.get_tokens(ParserRequests.get_cookies(), chain, limit, sort_by, parents)
    if tokens is None:
        log('Something wrong!')
        raise Exception('Something wrong!')

    try:
        with open('result.json', 'a') as file:
            file.write(json.dumps(tokens))
    except Exception as e:
        log('Error save result.json', str(e))
    print('Completed!')

