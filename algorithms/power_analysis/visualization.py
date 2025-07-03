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
        Zeigt den Spotpreis in EUR/MWh als Liniendiagramm für einen Zeitraum.
        """
        fig = px.line(self.df, x=self.df["HourUTC"], y=self.df["SpotPriceEUR"]) 
        fig.update_layout(
            title="Spotpreise EUR/MWh",
            xaxis_title="Zeit",
            yaxis_title="Preis (EUR/MWh)"
        )

        fig.show()
        
    
    def price_distribution() -> None: 
        """
        Zeigt die Verteilung der Spotpreise für ein Gebiet als Histogramm.
        """
        return
    
    def heat_map() -> None:
        """
        Heatmap der durchschnittlichen Preise nach Stunde und Wochentag.
        """
        return
    
    def compare_areas() -> None: 
        """
        Vergleicht die Preisentwicklung in mehreren Preiszonen in einem Plot.
        """
        return 
    
    def negative_price_events() -> None:
        """
        Markiert Zeitpunkte, an denen der Spotpreis negativ war.
        """
        return
    