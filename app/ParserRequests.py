import httpx
from httpx import Cookies
from GraphQL import rankings_page_query, Chain, SortBy, Parents
from Logger import log
from Token import Token
from ToJson import make_json
import brotli  # NEED
import Config

cfg = Config.cfg

client = httpx.Client(
    verify=False,
    http2=True,
    proxies=cfg.proxies)


def get_cookies() -> Cookies:
    try:
        response = client.get(f"https://opensea.io/rankings?sortBy=total_volume&category=new&chain=klaytn",
                              headers={
                                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                  "Accept-Encoding": "gzip, deflate, br",
                                  "Accept-Language": "en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7",
                                  "Cache-Control": "max-age=0",
                                  "Connection": "keep-alive",
                                  "Host": "opensea.io",
                                  "Upgrade-Insecure-Requests": "1",
                                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
                              })
        if response.status_code == 200:
            return response.cookies
        else:
            raise Exception(response.status_code, response.json(), response.text)
    except httpx.HTTPError as e:
        raise Exception(e)
    except Exception as e:
        log('Error get_cookies', str(e))


# USE
# tokens = get_tokens(get_cookies(), Chain, int, SortBy, Parents)
# Example: tokens = get_tokens(get_cookies(), Chain.all_chains, 100, SortBy.all_time, Parents.all_categories)
# Params:
#   Chain:
#       All Chains  = Chain.all_chains
#       Ethereum    = Chain.ethereum
#       Matic       = Chain.matic
#       Klaytn      = Chain.klaytn
#   Limit:
#       integer number
#   SortBy:
#       Last Day Hours      = SortBy.last_day_hours
#       Last Seven Days     = SortBy.last_seven_days
#       Last Thirty Days    = SortBy.last_thirty_days
#       All Time            = SortBy.all_time
#   Parents:
#       All Categories          = Parents.all_categories
#       New                     = Parents.new
#       Art                     = Parents.art
#       Domain Names            = Parents.domain_names
#       Music                   = Parents.music
#       Photography Category    = Parents.photography_category
#       Sports                  = Parents.sports
#       Trading Cards           = Parents.trading_cards
#       Utility                 = Parents.utility
#       Virtual Worlds          = Parents.virtual_worlds
def get_tokens(cookies: Cookies, chain: Chain = cfg.chain, limit: int = cfg.limit, sort_by: SortBy = cfg.sort_by,
               parents: Parents = cfg.parents) -> list[Token]:
    try:
        response = client.post(f"https://api.opensea.io/graphql/",
                               cookies=cookies,
                               headers={
                                   "accept": "*/*",
                                   "accept-encoding": "gzip, deflate, br",
                                   "accept-language": "en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7",
                                   "content-type": "application/json; charset=utf-8",
                                   "host": "api.opensea.io",
                                   "origin": "https://opensea.io",
                                   "referer": "https://opensea.io/",
                                   "sec-ch-ua": '" " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                                   "sec-ch-ua-mobile": "?0",
                                   "sec-ch-ua-platform": "Windows",
                                   "sec-fetch-dest": "empty",
                                   "sec-fetch-mode": "cors",
                                   "sec-fetch-site": "same-site",
                                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
                                   "x-api-key": "2f6f419a083c46de9d83ce3dbe7db601",
                                   "x-build-id": "cpZ03TUwNXXMXlX1EFIV2",
                                   "x-datadog-origin": "rum",
                                   "x-datadog-parent-id": "6625360975196433345",
                                   "x-datadog-sampled": "1",
                                   "x-datadog-sampling-priority": "1",
                                   "x-datadog-trace-id": "7601407751590475561",
                                   "x-signed-query": "c9e930e4edb22588d672233ed06bcd592177894fa5ad9c1821edf2a92f92dfef"
                               }, data=make_json(rankings_page_query(chain, limit, sort_by, parents)))
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.status_code, response.json(), response.text)
    except httpx.HTTPError as e:
        raise Exception(e)
    except Exception as e:
        log('Error get_tokens', str(e))
