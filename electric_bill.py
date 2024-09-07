"""
Write a program to calculate the amount of money the user must pay for their electric bill. Your program will prompt the user for (1) their base kilowatt hour (kWh) rate and (2) the number of kWh they have used in a month. Your program will calculate and print as output the the total amount due. Your program will appropriately calculate overage as follows: up to 1,000 kWh are charged at the base rate, and any kWh used in excess of 1,000 kWh are charged at 125% of the base rate. For example, if the user used 1,250 kWh at $0.14 per kWh the total due would be (1000*.14)+(250*(.14*1.25)). 
"""

def calculate_bill(base_rate: float, kwh_used: int) -> float:
    """Returns the total amount a user owes on their electric bill.
    Parameters:
      base_rate (float): rate per kWh
      kwh_used (int): number of kWhs used in the month
    Return:
      total of the bill (float)
    """
    pass

def main():
    pass

if __name__ == '__main__':
    main()