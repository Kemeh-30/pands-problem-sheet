# bank.py
# Author : Adedoyinsola Fifo
# Prompt the user and read in two money amounts (in cent)
Amount1 = int(input('Enter Amount1 in cent: '))
Amount2 = int(input('Enter Amount2 in cent: '))
# Add the two amounts
Total_Amount = (Amount1 + Amount2)
# Print out the answer in a human readable format with a euro sign and decimal point
print (f"The Sum of these is: \u20AC{Total_Amount:.2f}")


