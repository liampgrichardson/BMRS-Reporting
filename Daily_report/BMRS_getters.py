"""
This script contains function definitions for getting data from the Elexon Insights API.
Replaces the defunct api.bmreports.com BMRS API.
No API key required.
"""
import pandas as pd
import requests

BASE_URL = "https://data.elexon.co.uk/bmrs/api/v1"


def get_settlement_system_prices(settlement_date: str) -> pd.DataFrame:
    """
    Fetch settlement system prices for all 48 settlement periods on a given date.
    Consolidates the old B1770 (Imbalance Prices) and B1780 (Imbalance Volumes) endpoints.
    """
    url = f"{BASE_URL}/balancing/settlement/system-prices/{settlement_date}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return pd.DataFrame(response.json()["data"])


def get_b1770_day(settlement_date: str):
    """
    Get imbalance prices (System Buy Price) for all settlement periods on a given date.
    Replaces the old BMRS B1770 report.
    :param settlement_date: "YYYY-MM-DD"
    :return: pandas dataframe with columns: Settlement Period, ImbalancePriceAmount
    """
    df = get_settlement_system_prices(settlement_date)
    result = df[["settlementPeriod", "systemBuyPrice"]].copy()
    result.columns = ["Settlement Period", "ImbalancePriceAmount"]
    return result.reset_index(drop=True)


def get_b1780_day(settlement_date: str):
    """
    Get net imbalance volumes for all settlement periods on a given date.
    Replaces the old BMRS B1780 report.
    :param settlement_date: "YYYY-MM-DD"
    :return: pandas dataframe with columns: Settlement Period, Imbalance Quantity (MAW)
    """
    df = get_settlement_system_prices(settlement_date)
    result = df[["settlementPeriod", "netImbalanceVolume"]].copy()
    result.columns = ["Settlement Period", "Imbalance Quantity (MAW)"]
    return result.reset_index(drop=True)
