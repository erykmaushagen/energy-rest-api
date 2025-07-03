# visualization an plots of relevant data

from typing import List
import matplotlib.pyplot as plt
from data import MarketPriceData

class DataVisualizer: 
    def __init__(self, records: List[MarketPriceData]):
        self.records = records
        
