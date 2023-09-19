import pandas as pd
import matplotlib.pyplot as plt


def create_burndown_chart(df: pd.DataFrame, starting_cash: float):
    # Calculate net income
    # Adjust these column names based on your DataFrame
    df['net_income'] = df['income_total'] - df['expenses_total']

    # Calculate cumulative net income
    df['cumulative_net_income'] = df['net_income'].cumsum()

    # Calculate cash balance
    df['cash_balance'] = starting_cash + df['cumulative_net_income']

    # Plotting
    plt.figure(figsize=(10, 6))  # type:ignore
    plt.plot(df['cash_balance'], label='Cash Balance',  # type:ignore
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
