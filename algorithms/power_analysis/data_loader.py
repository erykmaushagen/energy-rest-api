# gets data trough .csv or extendible to fetch_data from apis

import pandas as pd 
import matplotlib.pyplot as plt
import datetime
import os 

class Visualizer():
    def __init__(self, df: pd.DataFrame, point_size, line_size) -> None:
        self.df = df
        self.point_size = point_size
        self.line_size = line_size

    def plot_point(start_date, end_date) -> None: 
        plt.plot(Visualizer.df, markersize=Visualizer.point_size, linewidth=Visualizer.line_size)
        plt.title("Line-Plot")
        # 
    def plot_line(start_date, end_date) -> None:
        plt.plot(Visualizer.df, markersize=Visualizer.point_size, linewidth=Visualizer.line_size)
        plt.title("Line-Plot")
        



def fetch_data(path):

    df = pd.read_csv(path, sep=';', skip_blank_lines=True)

    df['SpotPriceDKK'] = df['SpotPriceDKK'].str.replace(',', '.').astype(float)
    df['SpotPriceEUR'] = df['SpotPriceEUR'].str.replace(',', '.').astype(float)
    df['HourDK'] = pd.to_datetime(df['HourDK'])
    df['HourUTC'] = pd.to_datetime(df['HourUTC'])

    market_df = df[df['PriceArea'] == 'DK1']

    # print(market_df.head())
    # print(df.dtypes)
    return market_df

def plot_data(start_date, end_date, df):
    # Konvertiere die HourDK-Spalte in Datetime
    
    print(start_date, end_date, df_unfiltered)
    # Erstellen des Plots
    df = df_unfiltered[(df_unfiltered['HourUTC'] > start_date) & (df_unfiltered['HourUTC'] < end_date)]
    plt.figure(figsize=(10, 5))  # Größe des Plots
    plt.plot(df['HourDK'], df['SpotPriceEUR'], marker='o', label='SpotPriceEUR', markersize=0.1, linewidth=0.5)  # Liniendiagramm
    plt.xlabel('Hour DK')  # X-Achsenbeschriftung
    plt.ylabel('Spot Price in EUR')  # Y-Achsenbeschriftung
    plt.title('Spot Prices in EUR over Time')  # Titel des Plots
    plt.xticks(rotation=45)  # X-Achsen-Beschriftungen rotieren
    plt.grid(True)  # Gitterlinien anzeigen
    plt.legend()  # Legende anzeigen
    plt.tight_layout()  # Layout anpassen
    plt.savefig('spotpreise_eur.png')  # Speichern des Plots als PNG-Datei
    plt.close()  # Schließen des Plots

if __name__ == "__main__":
    path = "dataset/Elspotprices_2015_2024.csv"
    df_unfiltered = fetch_data(path)
    plot_data('2023-02-22 22:00:00', '2023-07-22 22:00:00', df_unfiltered)

    # plt.plot(market_df['SpotPriceDKK'])
    # plt.show()




