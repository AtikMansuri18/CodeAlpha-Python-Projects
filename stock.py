'''
✅ TASK 2: Stock Portfolio Tracker
● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock
prices.
● Simplified Scope:
○ User inputs stock names and quantity.
○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
○ Display total investment value and optionally save the result in a .txt or .csv file.
● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling
(optional).

'''

print("Stock Portfolio Tracker")

# Define  Dictionary to store stock prices
#s stand for stock
s = {
    "AAPL": 180,
    "TSLA": 250,
    "ANDR": 200,
    "IOS": 300
}

# Take stock name from user define name
n = input("Enter Stock Name :- ").upper()

# Take quantity from user define quntity
q= int(input("Enter Quantity :- "))

# Check stock is Available  or not
if n in s:

    # Define stock price
    p = s[n]

    # Calculate total investment
    t = p * q

    # Display result
    print("\nStock Found")

    print("Stock Name :-", n)

    print("Stock Price :-", p)

    print("Quantity :-", q)

    print("Total Investment :-", t)

    # Save Stock result in text file
    file = open("portfolio.txt", "w")#w stand for write

    file.write("Stock Portfolio Details\n")
    file.write("----------------------\n")

    file.write("Stock Name :- " + n + "\n")

    file.write("Stock Price :- " + str(p) + "\n")#price is integer convert in string

    file.write("Quantity :- " + str(q) + "\n")#quantity is integer convert in string

    file.write("Total Investment :- " + str(t))#total are integer convert in string

    # Close file
    file.close()
    print("\n Data Saved in portfolio.txt")

else:
    print(" Stock Not Found")
