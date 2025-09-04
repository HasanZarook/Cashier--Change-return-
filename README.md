💵 Cashier Change Return System
📖 Overview

This is a simple Python program that calculates the balance amount (change) to be returned to a customer after a bill payment.
The program breaks the balance into different Pakistani currency denominations (notes and coins) for easier handling.

🛠️ Features

Takes total bill amount and paid amount as input.

Calculates the remaining balance (if paid amount ≥ bill amount).

Breaks down the balance into available Pakistani currency denominations:

Rs. 5000, Rs. 1000, Rs. 500, Rs. 100, Rs. 50, Rs. 20, Rs. 10, Rs. 5, Rs. 2, Rs. 1.

Displays the exact number of notes/coins needed for each denomination.

Handles the case where the paid amount is less than the bill amount.

📂 Project Structure
cashier-change-system/
│── Cashier--change-return.py    # Main source code
│── README.md           # Documentation
│── LICENSE             # License file (MIT recommended)
│── .gitignore          # Ignore unnecessary files

🚀 Getting Started
Prerequisites

Python 3.x installed on your system.

Running the Program
python Cashier--change-return.py

Example Run
enter the total bill amount: 2370
enter the paid amount by customer: 10000

bill is 2370 Pakistan rupees
paid amount is 10000 Pakistan rupees
your balance is 7630
5000rs: 1
1000rs: 2
500rs: 1
100rs: 1
50rs: 0
20rs: 1
10rs: 0
5rs: 0
2rs: 0
1rs: 0

📊 Output Explanation

The customer paid 10000 for a bill of 2370.

Balance is 7630.

The program breaks it into 1 × 5000, 2 × 1000, 1 × 500, 1 × 100, 1 × 20.

📘 Future Improvements

Add support for other currencies.

Build a GUI version with Tkinter or PyQt.

Store transactions in a database.

🤝 Author

A.G. Hasan Zarook
