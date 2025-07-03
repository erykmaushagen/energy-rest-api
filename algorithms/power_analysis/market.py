
from typing import List, Optional


class Market: 
    """
    class for market information.
    
    Attributes:
        id: 
            String of ID e.g. "EPEX_DE"
        country_coverage:
            Optional list of countries the market covers e.g. ["DE"]
        products:
            Optional prducts exhcange trades e.g. ["day-ahead", "intraday"]
        resolution: 
            Data resolution e.g. "15min"
        coupled:
            Optional bool if coupled or not
        negative_prices. 
            Optional bool if market allows negative prices
        auction_times: 
            Optional list of times for auctions ["12:00", "13:00"] 
    """
    def __init__(
        self, 
        id: str,
        country_coverage: Optional[List[str]] = None,
        products: Optional[List[str]] = None,
        resolution: Optional[str] = None,
        coupled: bool = False,
        negative_prices: bool = False,
        auction_times: Optional[List[str]] = None
    ):
        self.id = id
        self.country_coverage = country_coverage or []
        self.products = products or []
        self.resolution = resolution
        self.coupled = coupled
        self.negative_prices = negative_prices
        self.auction_times = auction_times or []

    def description(self) -> None: 
        print(f"Market ID:{self.id}")
        print(f"Countries: {', '.join(self.country_coverage or [])}")
        print(f"Products: {', '.join(self.products or [])}")
        print(f"Resolution: {self.resolution}")
        print("Coupled" if self.coupled else "Not coupled")
        print("Negative prices allowed" if self.negative_prices else "No negative prices")
        print(f"Auction times: {', '.join(self.auction_times or [])}")
    
    def suppports_country(self, country: str) -> bool: 
        return country in self.country_coverage
    
    