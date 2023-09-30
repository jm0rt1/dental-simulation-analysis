import pandas as pd
import matplotlib.pyplot as plt

from src.app.analysis.idr.data_classes.report import Report


def create_burndown_chart(df: pd.DataFrame, starting_cash: float):
    # Calculate net income
    # Adjust these column names based on your DataFrame

    # Calculate cumulative net income
    df['cumulative_net_income'] = df['income_expense_data*profit_loss_this_qtr'].cumsum()

    # Calculate cash balance
    # df['cash_management_data*ending_cash_this_quarter'] = starting_cash + df['cumulative_net_income']

    # Plotting
    plt.figure(figsize=(10, 6))  # type:ignore
    plt.plot(df['cash_management_data*ending_cash_this_quarter'], label='Cash Balance',  # type:ignore
             color='red')  # type:ignore
    # Line indicating zero cash balance #type:ignore
    plt.axhline(0, color='black', linestyle='--')  # type:ignore
    plt.title('Burn-down Chart')  # type:ignore
    plt.xlabel('Time Period')  # type:ignore
    plt.ylabel('Cash Balance')  # type:ignore
    plt.legend()  # type:ignore
    plt.grid(True)  # type:ignore
    plt.tight_layout()  # type:ignore
    plt.show()  # type:ignore


def project_burndown_chart(reports: list[Report], projection_quarters: int = 4):

    # Extracting the necessary data from the provided reports
    net_incomes = [r.income_expense_data.profit_loss_this_qtr for r in reports]
    cash_balances = [
        r.cash_management_data.ending_cash_this_quarter for r in reports]

    # Get the most recent quarter's net income and cash balance
    recent_quarter_net_income = net_incomes[-1]
    recent_quarter_cash_balance = cash_balances[-1]

    # Project future net incomes and cash balances based on the most recent quarter
    future_net_incomes = [recent_quarter_net_income] * projection_quarters
    future_cash_balances = [recent_quarter_cash_balance +
                            sum(future_net_incomes[:i+1]) for i in range(projection_quarters)]

    # Combine historical and projected data
    combined_cash_balances = cash_balances + future_cash_balances

    # Create x-axis labels
    total_quarters = len(reports) + projection_quarters
    x_labels = [f'Quarter {i+1}' for i in range(total_quarters)]

    # Plotting
    plt.figure(figsize=(12, 7))
    plt.plot(x_labels, combined_cash_balances,
             label='Cash Balance', color='red', marker='o')
    # Line indicating zero cash balance
    plt.axhline(0, color='black', linestyle='--')
    plt.title('Projected Burn-down Chart (Quarterly)')
    plt.xlabel('Time')
    plt.ylabel('Cash Balance')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Find out when cash runs out
    if min(combined_cash_balances) <= 0:
        zero_cash_quarter = x_labels[combined_cash_balances.index(
            min(combined_cash_balances))]
        print(f"Projected to run out of money by: {zero_cash_quarter}")
    else:
        print("Based on current projections, the company will not run out of money in the projected quarters.")


def project_burndown_chart_advanced(reports: list[Report], projection_quarters: int = 12, annual_growth_rate=0, one_off_events={}):
    """
    :param reports: List of Report objects
    :param projection_quarters: Number of quarters to project
    :param annual_growth_rate: Expected annual growth rate in net income (e.g., 0.05 for 5%)
    :param one_off_events: A dictionary with quarter numbers as keys and amounts as values.
                           Positive values for income, negative for costs.
                           E.g., {2: -5000} means a one-off cost of 5000 in the 2nd projected quarter.
    """

    if one_off_events is None:
        one_off_events = {}

    # Extract the necessary data from the provided reports
    net_incomes = [r.income_expense_data.profit_loss_this_qtr for r in reports]
    cash_balances = [
        r.cash_management_data.ending_cash_this_quarter for r in reports]

    # Calculate the quarterly growth rate
    quarterly_growth_rate = (1 + annual_growth_rate) ** (1/4) - 1

    # Project future net incomes
    future_net_incomes = [
        net_incomes[-1] * (1 + quarterly_growth_rate) ** i for i in range(1, projection_quarters + 1)]

    # Apply one-off events
    for quarter, amount in one_off_events.items():
        if quarter < len(future_net_incomes):
            future_net_incomes[quarter-1] += amount

    # Project future cash balances
    future_cash_balances = [
        cash_balances[-1] + sum(future_net_incomes[:i+1]) for i in range(projection_quarters)]

    # Combine historical and projected data
    combined_cash_balances = cash_balances + future_cash_balances

    # Create x-axis labels
    total_quarters = len(reports) + projection_quarters
    x_labels = [f'Quarter {i+1}' for i in range(total_quarters)]

    # Plotting
    plt.figure(figsize=(12, 7))
    plt.plot(x_labels, combined_cash_balances,
             label='Cash Balance', color='red', marker='o')
    plt.axhline(0, color='black', linestyle='--')
    plt.title('Projected Burn-down Chart (Quarterly)')
    plt.xlabel('Time')
    plt.ylabel('Cash Balance')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Find out when cash runs out
    if min(combined_cash_balances) <= 0:
        zero_cash_quarter = x_labels[combined_cash_balances.index(
            min(combined_cash_balances))]
        print(f"Projected to run out of money by: {zero_cash_quarter}")
    else:
        print("Based on current projections, the company will not run out of money in the projected quarters.")
