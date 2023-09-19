import pandas as pd
import matplotlib.pyplot as plt


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


def project_burndown_chart(df: pd.DataFrame, starting_cash: float = 0, projection_months=12):

    # Calculate average monthly net income
    avg_monthly_net_income = df['income_expense_data*profit_loss_this_qtr'].mean()

    # Project future net incomes
    future_net_incomes = [avg_monthly_net_income] * projection_months
    future_dates = pd.date_range(
        start=df.index[-1] + pd.DateOffset(1), periods=projection_months, freq='Q')

    future_df = pd.DataFrame({
        'income_expense_data*profit_loss_this_qtr': future_net_incomes,
    }, index=future_dates)

    # Combine historical and projected data
    combined_df = pd.concat([df, future_df], axis=0)

    # Calculate cumulative net income
    combined_df['cumulative_net_income'] = combined_df['income_expense_data*profit_loss_this_qtr'].cumsum()

    # Calculate cash balance
    combined_df['cash_management_data*ending_cash_this_quarter'] = starting_cash + \
        combined_df['cumulative_net_income']

    # Plotting
    plt.figure(figsize=(12, 7))
    plt.plot(combined_df['cash_management_data*ending_cash_this_quarter'],
             label='Cash Balance', color='red')
    # Line indicating zero cash balance
    plt.axhline(0, color='black', linestyle='--')
    plt.title('Projected Burn-down Chart')
    plt.xlabel('Time')
    plt.ylabel('Cash Balance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Find out when cash runs out
    negative_cash = combined_df[combined_df['cash_management_data*ending_cash_this_quarter'] <= 0]
    if not negative_cash.empty:
        print(f"Projected to run out of money by: {negative_cash.index[0]}")
    else:
        print("Based on current projections, the company will not run out of money in the next year.")

# Example usage:
# df should be indexed by date for this to work
# project_burndown_chart(df, starting_cash=100000)  # Replace 100000 with your actual starting cash
