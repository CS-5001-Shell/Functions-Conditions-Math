# Functions, Conditions, and Math Operators

This lab assignment requires the following concepts:
- Functions
- Conditionals
- Mathematical Operators

For this assignment, you will complete the following four programs:

## Electric Bill
Write a program to calculate the amount of money the user must pay for their electric bill. Your program will prompt the user for (1) their base kilowatt hour (kWh) rate and (2) the number of kWh they have used in a month. Your program will calculate and print as output the the total amount due. Your program will appropriately calculate overage as follows: up to 1,000 kWh are charged at the base rate, and any kWh used in excess of 1,000 kWh are charged at 125% of the base rate. For example, if the user used 1,250 kWh at $0.14 per kWh the total due would be (1000*.14)+(250*(.14*1.25)). 

This program will be implemented in the file named *electric_bill.py*. 

It is required that you complete the following function outlined in *electric_bill.py*.

```python
def calculate_bill(base_rate: float, kwh_used: int) -> float:
    """Returns the total amount a user owes on their electric bill.
    Parameters:
      base_rate (float): rate per kWh
      kwh_used (int): number of kWhs used in the month
    Return:
      total of the bill (float)
    """
```

## Card Game Helper
One of my favorite card games is called Hand and Foot. The goal of the game is to generate piles of cards of the same rank. Cards with different ranks have different values. For this question, you will implement a Hand and Foot helper that will prompt the user for a card rank and will output the value for the given card. The value for each rank is as follows:

| Rank | Value |
| -- | -- | 
| Joker | 50 points |
| Two & Ace | 20 points|
| Nine, Ten, Jack, Queen, King | 10 points |
| Four, Five, Six, Seven, Eight	| 5 points |
| Black Threes | 5 points |
| Red Threes | No value |

*Note that the value of a Three will differ based upon the color. Your program will prompt the user for the rank and, if the rank is a Three, it will need to also prompt the user for the color.*

This program will be implemented in the file named *card_game_helper.py*.

It is required that you complete the following function outlined in *card_game_helper.py*.

```python
def get_point_value(rank: str, color: str=None):
    """Returns the value associated with the given rank and color.
    Ranks are: 
      Joker, Two, Ace, Nine, Ten, Jack, Queen, King, Four
      Five, Six, Seven, Eight, Three
    Colors are:
      Red, Black
    You may assume that the function is case sensitive.
    Parameters:
      rank (str): rank of the card
      color (str): color of the card (red or black) default to None
    Return:
      point value of the card or -1 if input is invalid.
    """
```

## Bill Splitter
Implement a program that will prompt the user for the following three pieces of information (1) the amount of a restaurant bill; (2) the quality of service; and (3) the number of diners. The program will add a tip to the bill amount and will output the amount each diner owes. 

Requirements:

  - The quality of service will be specified as fair, good, or excellent. The corresponding tip amounts will be 18%, 20%, and 25% respectively.
  - The program will print an error message and exit if the quality of service entered is not one of fair/good/excellent.
  - If the total amount owed for the bill + tip does not divide evenly among the diners then you will simply round to two decimals.

This program will be implemented in the file named *bill_splitter.py*.

It is required that you complete the following function outlined in *bill_splitter.py*.

```python
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
```

## Shopping Cart
For this exercise you will write a program to calculate the total of a user's shopping cart and the amount of change he/she is owed given the amount they wish to pay.

Requirements:

  - Your store will offer at least three items. Your program will prompt the user to enter the number of each item they wish to purchase.
  - At least one of the items must have a price that is not a whole number.
  - Your program will display for the user the total amount owed.
  - Your program will prompt the user to enter the amount of payment.
  - If the payment is less than the amount owed, your program will tell the user they are short and exit.
  - If the payment is more than the amount owed, your program will calculate the user's change. You will display for the user the number of $20, $10, $5, $1, quarters, nickels, dimes, and pennies to be returned.
  - Your store may offer any three (or more) items. 

Hints:
  
  - It is not required to use loops. Remember, you can use the / // and % operators. 

Below are three example executions of a sample program.

```
Welcome to Sami's Bakery!
We offer chocolate cake, chocolate muffins, and hot chocolate.
How many slices of chocolate cake would you like ($5/slice)? 1
How many chocolate muffins would you like ($3.25/muffin)? 4
How many cups of hot chocolate would you like ($4.25/cup)? 0
Your total is $18.0.
Enter payment amount: 20
Your total change is $2.0.
You are owed:
    $20 - 0
    $10 - 0
    $5 - 0
    $1 - 2.0
    $.25 - 0
    $.10 - 0
    $.05 - 0
    $.01 - 0
```
```
Welcome to Sami's Bakery!
We offer chocolate cake, chocolate muffins, and hot chocolate.
How many slices of chocolate cake would you like ($5/slice)? 1
How many chocolate muffins would you like ($3.25/muffin)? 1
How many cups of hot chocolate would you like ($4.25/cup)? 2
Your total is $16.75.
Enter payment amount: 20
Your total change is $3.25.
You are owed:
    $20 - 0
    $10 - 0
    $5 - 0
    $1 - 3.0
    $.25 - 1
    $.10 - 0
    $.05 - 0
    $.01 - 0
```
```
Welcome to Sami's Bakery!
We offer chocolate cake, chocolate muffins, and hot chocolate.
How many slices of chocolate cake would you like ($5/slice)? 2
How many chocolate muffins would you like ($3.25/muffin)? 1
How many cups of hot chocolate would you like ($4.25/cup)? 1
Your total is $17.5.
Enter payment amount: 10
Sorry, you are $7.5 short.
```

This program will be implemented in the file named *shopping_cart.py*.

There are no required functions; however, much of your grade will depend upon the design that you choose for your program.

## Assignment Submission

To earn credit for this assignment you must commit all of your changes to your GitHub repository prior to the deadline. It is strongly recommended that you commit your changes regularly. Do not wait until you complete all parts of the assignment to upload your (partial) solution.

Step 1 - *Stage Changes*: Select the Source Control icon in the VSCode left menu. In the Changes section, click the + to *Stage All Changes*.

Step 2 - Commit Message: In the text box that says Message enter a meaningful message that describes the change you just completed.

Step 3 - *Commit & Push*: Select the down arrow in the blue box that says Commit. Choose *Commit & Push*.

Step 4 - Verify: Visit the repository on GitHub to confirm that your changes were uploaded successfully
