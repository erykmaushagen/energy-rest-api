
from typing import List
import pandas as pd


from datetime import datetime


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
        self.hour_utc = hour_utc
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
    def __init__(self, records: List[MarketPriceRecord] = None):
        self.records = records or []
    
    # currently specified in the kaggle dataset from a .csv file, loop up the README.md for more information
    def from_dataframe(self, df: pd.DataFrame) -> List[MarketPriceRecord]: 
        """
        converts in README.md descirbe .csv row format into a List of MarketPriceRecords 

        Args: 
            df: datafram with rows: "HourUTC", "HourDK", "PriceArea", "SpotPriceDKK",  "SpotPriceEUR"
        """
        self.records = []
        for row in df.iterrows:
            rec = MarketPriceRecord(
                hour_utc=row["HourUTC"],
                price_area=row["PriceArea"],
                spot_price_eur=["SpotPriceEUR"]
            )
            self.records.append(rec)
        return self.records
    
    def filter_by_area(self, area: str) -> List[MarketPriceRecord]:
        """
        filters List of MarketPriceRecords into 

        Args: 
            String with short definition of price area e.g. "CWE" ~ Central Western Europe
        Returns:
            List of MarketPriceRecords of specific prize area
        """
        return [row for row in self.records if row.price_area == area]

    
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

# import pandas as pd

# # pandas DataFrame aus CSV oder anderen Quellen laden
# df = pd.read_csv("marktpreise.csv", parse_dates=["HourUTC", "HourDK"])

# # MarketPriceData Objekt erzeugen
# mpd = MarketPriceData.from_dataframe(df)

# # Beispiel: alle Records für "DK1"
# dk1_records = mpd.filter_by_area("DK1")

# # zurück zu DataFrame konvertieren, z.B. für Plotly
# df_dk1 = MarketPriceData(dk1_records).to_dataframe()