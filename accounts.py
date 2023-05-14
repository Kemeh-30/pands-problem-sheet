# accounts.py
# Author : Adedoyinsola Fifo
# Account number display
# Read in a 10 character account number
account_number = input("1234567890: ")
last_four_digits= account_number[-4:]
# Output the account number with only the last 4 digits showing and the first 6 digits replaced with Xs
print("Account Number: ****" + last_four_digits)

