# Stock Portfolio Tracker

def stock_portfolio_tracker():
    # Hardcoded dictionary with stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2700,
        "AMZN": 3400
    }

    # User inputs
    portfolio = {}
    total_investment = 0

    # User input for stock names and quantities
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break
        if stock_name in stock_prices:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            portfolio[stock_name] = quantity
        else:
            print("Stock not found. Please enter a valid stock name.")

    # Calculate total investment
    for stock, quantity in portfolio.items():
        total_investment += stock_prices[stock] * quantity

    # Display total investment
    print(f"Total Investment Value: ${total_investment}")

    # Optional: Save the result to a .txt or .csv file
    save_option = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter filename (with .txt or .csv extension): ")
        with open(filename, 'w') as f:
            f.write(f"Total Investment Value: ${total_investment}\n")
            f.write("Portfolio Details:\n")
            for stock, quantity in portfolio.items():
                f.write(f"{stock}: {quantity}\n")
        print(f"Results saved to {filename}")

# Run the tracker
stock_portfolio_tracker()
