class Token:
    id: int
    symbol: str
    address: str
    image_url: str
    name: str
    decimals: int
    eth_price: str
    usd_price: str

    def __init__(self, id: int, symbol: str, address: str, image_url: str, name: str, decimals: int, eth_price: str,
                 usd_price: str):
        self.id = id
        self.symbol = symbol
        self.address = address
        self.image_url = image_url
        self.name = name
        self.decimals = decimals
        self.eth_price = eth_price
        self.usd_price = usd_price
