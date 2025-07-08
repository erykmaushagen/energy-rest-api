
from typing import List
import pandas as pd
from datetime import datetime
from power_analysis.market import Market

class MarketPriceRecord:
    """
    class for all relevant price information regarding a certain timestamp.

    Attributes: 
        hour_utc: 
            represents hour in coordinated universal time
        price_area: 
            represents market spezific time zone e.g. 'GER' = Germany, 'SE4' = Swedne Price Zone 4
        spot_price_eur: 
            represents price per MWh in Euro 
    """
    def __init__(self, 
            hour_utc: datetime, 
            price_area: str,  
            spot_price_eur: float
        ):
        self.hour_utc = pd.to_datetime(hour_utc)
        self.price_area = price_area
        self.spot_price_eur = spot_price_eur

    def __repr__(self):
        return f"<MarketPriceRecord {self.price_area} {self.hour_utc} - {self.spot_price_eur} EUR>"


class MarketPriceData:
    """
    class capsulating an input dataframe into an List of MarketPriceRecords

    Attributes: 
        records:
            list of MarketPriceRecords extracted out of an input dataframe
    """
    def __init__(self, market: Market=None, records: List[MarketPriceRecord] = None):
        self.market = market
        self.records = records or []
    
    # currently specified in the kaggle dataset from a .csv file, loop up the README.md for more information
    def from_dataframe(self, df: pd.DataFrame) -> List[MarketPriceRecord]: 
        """
        converts in README.md descirbe .csv row format into a List of MarketPriceRecords 

        Args: 
            df: datafram with rows: "HourUTC", "HourDK", "PriceArea", "SpotPriceDKK",  "SpotPriceEUR"
        """
        self.records = []
        for index, row in df.iterrows():
            rec = MarketPriceRecord(
                hour_utc=row["HourUTC"],
                price_area=str(row["PriceArea"]),
                spot_price_eur=float(row["SpotPriceEUR"])
            )
            self.records.append(rec)
        return self.records
    
    def to_dataframe(self) -> pd.DataFrame: 
        """
        processes List of MarketPriceRecords into 

        Returns: 
            Pandas Dataframe with columns "HourUTC", "PriceArea", "SpotPriceEUR"
        """
        data = { 
            "HourUTC": [row.hour_utc for row in self.records],
            "PriceArea": [row.price_area for row in self.records],
            "SpotPriceEUR": [row.spot_price_eur for row in self.records]
        }

        return pd.DataFrame(data)
    
    def filter_by_area(self, area: str) -> None:
        """
        filters List of MarketPriceRecords into 

        Args: 
            String with short definition of price area e.g. "CWE" ~ Central Western Europe
        """
        self.records = [row for row in self.records if row.price_area == area]
    
    def filter_by_date(self, start_date: datetime, end_date: datetime) -> None:
        """
        filter by timeframe
        
        Args: 
            startdate and enddate in datetime format
        """
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        self.records = [row for row in self.records if start_date <= row.hour_utc <= end_date]
