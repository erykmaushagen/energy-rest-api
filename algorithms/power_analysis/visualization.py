# visualization an plots of relevant data

from typing import List
import pandas as pd
from datetime import datetime 
import plotly.express as px
import plotly.graph_objects as go
from power_analysis.data import MarketPriceData

class DataVisualizer: 
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def line_plot(self) -> None: 
        """
        Shows Spot-Price in EUR/MWh as linediagram for a certain timeline.
        """
        fig = px.line(self.df, x=self.df["HourUTC"], y=self.df["SpotPriceEUR"]) 
        fig.update_layout(
            title="Spotpreise EUR/MWh",
            xaxis_title="Zeit",
            yaxis_title="Preis (EUR/MWh)"
        )
        fig.show()        
    
    def price_distribution(self) -> None: 
        """
        Shows the distribution of prices in 0.1 EUR steps in definied range.
        """
        fig = px.histogram(
            self.df,
            x=self.df["SpotPriceEUR"], 
            title="Preisverteilung (SpootPriceEUR)",
            labels={"SpotPriceEUR": "Preis (EUR)", "count": "Häufigkeit"},
            color_discrete_sequence=["#0077b6"]
        )
        fig.update_traces(
            xbins=dict(
                size=0.1, 
                start=-50, 
                end=200
                )
            ) 
        fig.show()
    
    def heat_map(self) -> None:
        """
        Heatmap der durchschnittlichen Preise nach Stunde und Wochentag.
        """
        print(self.df["SpotPriceEUR"].dtype)

        start_date = self.df["HourUTC"].min()
        end_date = self.df["HourUTC"].max()

        self.df["Hour"] = pd.to_datetime(self.df["HourUTC"]).dt.hour
        agg_df = self.df.groupby(["PriceArea", "Hour"])["SpotPriceEUR"].mean().reset_index()
        print(agg_df.head())
        fig = px.density_heatmap(
            agg_df,
            x="Hour",
            y="PriceArea",
            z="SpotPriceEUR",
            color_continuous_scale="Plasma",
            title=f"Durchschnittlicher Preis pro Stunde und Region von {start_date} bis {end_date}"
        )
        fig.update_xaxes(type="category")
        fig.show()
    
    def compare_areas(self, areas: List[str] ) -> None: 
        """
        Vergleicht die Preisentwicklung in mehreren Preiszonen in einem Plot.
        """
        
        return 
    
    def negative_price_events(self) -> None:
        """
        Markiert Zeitpunkte, an denen der Spotpreis negativ war.
        """
        return
    