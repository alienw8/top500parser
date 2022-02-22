from enum import Enum, EnumMeta


class MyEnumMeta(EnumMeta):
    def __contains__(cls, item):
        return item in [v.value for v in cls.__members__.values()]


class Chain(str, Enum, metaclass=MyEnumMeta):
    all_chains: str = None
    ethereum: str = 'ETHEREUM'
    matic: str = 'MATIC'
    klaytn: str = 'KLAYTN'


class SortBy(str, Enum, metaclass=MyEnumMeta):
    last_day_hours: str = 'ONE_DAY_VOLUME'
    last_seven_days: str = 'SEVEN_DAY_VOLUME'
    last_thirty_days: str = 'THIRTY_DAY_VOLUME'
    all_time: str = 'TOTAL_VOLUME'


class Parents(str, Enum, metaclass=MyEnumMeta):
    all_categories: str = None
    new: str = None
    art: str = 'art'
    domain_names: str = 'domain-names'
    music: str = 'music'
    photography_category: str = 'photography-category'
    sports: str = 'sports'
    trading_cards: str = 'trading-cards'
    utility: str = 'utility'
    virtual_worlds: str = 'virtual-worlds'


class Variables:
    chain: Chain
    count: int
    cursor: str
    sortBy: SortBy
    parents: Parents
    createdAfter: str

    def __init__(self, chain: Chain, count: int, sort_by: SortBy, parents: Parents, created_after: str, cursor: str):
        self.chain = chain
        self.count = count
        self.cursor = cursor
        self.sortBy = sort_by
        self.parents = parents
        self.createdAfter = created_after


class RankingsPageQuery:
    id: str = "RankingsPageQuery"
    query: str = "query RankingsPageQuery(\n  $chain: [ChainScalar!]\n  $count: Int!\n  $cursor: String\n  $sortBy: CollectionSort\n  $parents: [CollectionSlug!]\n  $createdAfter: DateTime\n) {\n  ...RankingsPage_data\n}\n\nfragment PaymentAssetLogo_data on PaymentAssetType {\n  symbol\n  asset {\n    imageUrl\n    id\n  }\n}\n\nfragment RankingsPage_data on Query {\n  rankings(after: $cursor, chains: $chain, first: $count, sortBy: $sortBy, parents: $parents, createdAfter: $createdAfter) {\n    edges {\n      node {\n        createdDate\n        name\n        slug\n        logo\n        isVerified\n        nativePaymentAsset {\n          ...PaymentAssetLogo_data\n          id\n        }\n        statsV2 {\n          floorPrice {\n            unit\n            eth\n          }\n          numOwners\n          totalSupply\n          sevenDayChange\n          sevenDayVolume {\n            unit\n          }\n          oneDayChange\n          oneDayVolume {\n            unit\n          }\n          thirtyDayChange\n          thirtyDayVolume {\n            unit\n          }\n          totalVolume {\n            unit\n          }\n        }\n        id\n        __typename\n      }\n      cursor\n    }\n    pageInfo {\n      endCursor\n      hasNextPage\n    }\n  }\n}\n",
    variables: Variables

    def __init__(self, chain: Chain, limit: int, sort_by: SortBy, parents: Parents, cursor: str = None):
        self.id = self.id
        self.query = self.query
        self.variables = Variables(chain, limit, sort_by, parents, None, cursor)


def rankings_page_query(chain: Chain, limit: int, sort_by: SortBy, parents: Parents, cursor: str = None):
    return RankingsPageQuery(chain, limit, sort_by, parents, cursor)
