import json
import os
from GraphQL import Chain, SortBy, Parents
from Logger import log
from ToJson import make_json

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)


class Config:
    limit: int
    chain: Chain
    sort_by: SortBy
    parents: Parents
    proxies: dict[str]

    def __init__(self, limit: int = 100, chain: Chain = Chain.all_chains,
                 sort_by: SortBy = SortBy.all_time,
                 parents: Parents = Parents.all_categories,
                 proxies: dict[str] = None):
        self.limit = limit
        self.chain = chain
        self.sort_by = sort_by
        self.parents = parents
        self.proxies = proxies


cfg = Config()


def save():
    try:
        with open(parent + "/config.json", "w", encoding='utf-8') as jsonfile:
            global cfg
            jsonfile.write(make_json(cfg))
    except Exception as e:
        log('Error config save', str(e))


def load():
    try:
        with open(parent + "/config.json", "r", encoding='utf-8') as jsonfile:
            global cfg
            params = json.load(jsonfile)
            for key, value in params.items():
                setattr(cfg, key, value)
    except Exception as e:
        log('Error config load', str(e))


load()
