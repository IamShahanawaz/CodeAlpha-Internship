def stock_portfolio_tracker():
    print("📈 Welcome to the Stock Portfolio Tracker!")

    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 125,
        "INFY": 1500
    }

    print("Available Stocks:", ", ".join(stock_prices.keys()))

    portfolio = {}
    total_investment = 0

    while True:
        stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("❌ Stock not found in our list.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = quantity
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

    print("\n🧾 Your Investment Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_investment += value
        print(f"{stock}: {qty} x ₹{stock_prices[stock]} = ₹{value}")

    print(f"\n💰 Total Investment Value: ₹{total_investment}")

    # Optional: Save to text file
    save = input("Do you want to save this report to a file? (yes/no): ").lower()
    if save == 'yes':
        with open("portfolio_summary.txt", "w") as file:
            file.write("Your Stock Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} x ₹{stock_prices[stock]} = ₹{value}\n")
            file.write(f"\nTotal Investment: ₹{total_investment}\n")
        print("📂 Saved as 'portfolio_summary.txt'")

if __name__ == "__main__":
    stock_portfolio_tracker()
