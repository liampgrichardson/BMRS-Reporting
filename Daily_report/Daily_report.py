"""
This script generates a daily report of the system imbalance cost and price for the previous day
using BMRS reports Imbalance Prices (B1770) and Aggregated Imbalance Volumes (B1780)
"""

from datetime import datetime, timedelta
import pandas as pd
import BMRS_getters as bmrs
import matplotlib.pyplot as plt

today = datetime.today().date()
yesterday = today-timedelta(days=1)
date = yesterday

print(f"getting b1780 data from api...")
df_B1780_yesterday = bmrs.get_b1780_day(str(date))
print(f"getting b1770 data from api...")
df_B1770_yesterday = bmrs.get_b1770_day(str(date))

# Daily report
print(f"\n### Daily Report for {date} ###")
daily_report_df = pd.merge(df_B1780_yesterday, df_B1770_yesterday, on="Settlement Period")
daily_report_df.rename(columns={'ImbalancePriceAmount': 'ImbalancePriceAmount (GBP/MWh)'}, inplace=True)
daily_report_df = daily_report_df[["ImbalancePriceAmount (GBP/MWh)", "Settlement Period", "Imbalance Quantity (MAW)"]]

# total daily imbalance cost
daily_report_df["Imbalance Cost (GBP)"] = daily_report_df["ImbalancePriceAmount (GBP/MWh)"]*daily_report_df["Imbalance Quantity (MAW)"]
tot_daily_imbalance_cost = daily_report_df["Imbalance Cost (GBP)"].sum()

# daily imbalance unit rate
tot_daily_imbalance_amount = daily_report_df["Imbalance Quantity (MAW)"].sum()
daily_imbalance_unit_rate = tot_daily_imbalance_cost/tot_daily_imbalance_amount

# hour with the highest absolute imbalance volumes
daily_report_df["Hourly Imbalance Amount (MAW)"] = daily_report_df["Imbalance Quantity (MAW)"].rolling(2).sum()
imbalance_amount_max_hour = daily_report_df["Settlement Period"].iloc[daily_report_df['Hourly Imbalance Amount (MAW)'].idxmax()]/2

# Print daily report messages
print(f"Total Daily Imbalance Cost = {tot_daily_imbalance_cost} GBP")
print(f"Daily Imbalance Unit Rate = {daily_imbalance_unit_rate} GBP/MWh")
print(f"Imbalance Amount Max Hour = {imbalance_amount_max_hour}, "
      f"corresponds to half-hour settlement periods "
      f"{imbalance_amount_max_hour*2} and {imbalance_amount_max_hour*2 + 1}")

# Plot the daily report data over half-hour settlement period
fig, axs = plt.subplots(nrows=len(daily_report_df.set_index('Settlement Period').columns))
fig.suptitle(f"Daily Report over half-hour settlement periods for {date}", fontsize=14)
for ax, col in zip(axs.flatten(), daily_report_df.set_index('Settlement Period').columns):
    ax.plot(daily_report_df.set_index('Settlement Period')[col], label=col)
    ax.legend(loc="best")
plt.show()
