# includes price, trade_metrics, signal_classes

# market for ex. EPEX Spot, NordPool 
# for example information about: 
#   - countries covered 
#   - 

from typing import List

# example-instance::
# epex_de = PowerMarketInfo(
#     id="EPEX_DE",
#     name="EPEX Spot Germany",
#     countries=["DE"],
#     products=["day-ahead", "intraday"],
#     resolution="15min",
#     coupled=True,
#     allows_negative_prices=True,
#     auction_times=["12:00"]
# )

class Market(): 
    def __init__(self, id: str, country_coverge: List[str], products: List[str], 
                  resolution: str,  coupled: bool, allows_negative_prices: bool, auction_times: List[str] ) -> None:
        self.id = id
        self.country_coverage= country_coverge
        self.products = products       # z. B. ["day-ahead", "intraday"]
        self.resolution = resolution          # z. B. "15min", "1h"
        self.coupled = coupled
        self.allows_negative_prices = allows_negative_prices
        self.auction_times = auction_times






    
    def description(self) -> None: 
        print(Market.country)