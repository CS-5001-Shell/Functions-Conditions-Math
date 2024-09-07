"""
Implement a program that will prompt the user for the following three pieces of information (1) the amount of a restaurant bill; (2) the quality of service; and (3) the number of diners. The program will add a tip to the bill amount and will output the amount each diner owes. 

Requirements:

  - The quality of service will be specified as fair, good, or excellent. The corresponding tip amounts will be 18%, 20%, and 25% respectively.
  - The program will print an error message and exit if the quality of service entered is not one of fair/good/excellent.
  - If the total amount owed for the bill + tip does not divide evenly among the diners then you will simply round to two decimals.

"""

def get_per_diner_amount(bill_total: float, 
                         service: str, 
                         num_diners: int) -> float:
    """Returns the amount owed by each diner.
    Parameters:
      bill_total (float): total amount of the bill
      service (str): fair/good/excellent
      num_diners (int): number of people splitting the bill
    Return:
      amount owed by each diner
    
    Return -1 if the service provided is not one of the accepted values.
    """
    pass

def main():
    pass

if __name__ == '__main__':
    main()
