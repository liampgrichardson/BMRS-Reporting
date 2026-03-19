## Daily Report: Purpose and Explanation

The daily report analyzes the previous day's system imbalance cost and price using BMRS (Balancing Mechanism Reporting Service) data. It provides a clear summary of:

- **Total daily imbalance cost**: The total amount spent to correct imbalances in the electricity system.
- **Average unit rate for imbalances**: The cost per MWh for imbalances.
- **Periods with the highest imbalance volumes**: Identifies when the system was most out of balance.
- **Visual trends**: Plots of imbalance price and volume throughout the day.


## Key Terms Explained

- **Imbalance Cost**: The total financial amount paid (or received) to correct differences between electricity supply and demand. It is calculated as:

	$$
		ext{Imbalance Cost} = \text{Imbalance Volume} \times \text{Imbalance Price}
	$$
	This cost incentivizes accurate forecasting and balancing by market participants.

- **Imbalance Volume**: The quantity (in MWh or MAW) by which generation and demand differ during a settlement period. It measures the size of the mismatch that needs to be corrected by the system operator.

- **Imbalance Price**: The rate (£/MWh) applied to any difference between a participant’s contracted position and their actual generation or consumption. It is set by the system operator for each settlement period and reflects the real-time cost of balancing the grid. The imbalance price can be positive or negative, depending on system conditions.

### Why is this useful?

For energy suppliers and aggregators, this report helps to:
- Understand market conditions and the cost of imbalances, which affect trading and balancing strategies.
- Identify periods of high system stress or volatility, supporting operational and risk management decisions.
- Provide transparent, data-driven insights for compliance and reporting.
- Inform future bidding, forecasting, and settlement activities, improving profitability and reducing exposure to imbalance charges.


## Repo Usage Instructions

To avoid commiting and pushing ipynb outputs to git, use the following:
- pip install nbstripout 
(also in requirements.txt)
- nbstripout --install
