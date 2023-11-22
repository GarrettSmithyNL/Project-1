"""
This program gathers information for an insurance policy and generates a receipt for the policy. 
It prompts the user to enter their personal information, coverage options, 
payment option, and previous claims. It then calculates the insurance cost, HST, total cost, 
and financing amount based on the payment option. Finally, 
it prints a receipt with all the details of the insurance policy, including the customer's information, 
policy number, coverage details, costs, and any additional information based on the payment option chosen.

The program also provides functions to print the claims information and the receipt. 
The printClaims() function prints the claim number, claim date, 
and claim amount for each claim, or "No claims." if there are no claims. 
The printReceipt() function prints the details of the insurance policy, 
including the customer's name, address, phone number, policy number, payment option, 
number of cars, coverage details, insurance cost, HST, total cost, 
and any additional information based on the payment option chosen.

Note: This program relies on the Gar_Util module for validation and formatting functions.

By: Garrett Smith
Date: Nov 29 2023
"""
# Imports
from Gar_Util import Gar_Validate as validator
from Gar_Util import Gar_Format as formater
from Gar_Util import Gar_Utility as utility
import datetime

# Constants
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
DISCOUNT_ADD_CAR = 0.75
EXTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_CAR_COST = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99
FIRST_OF_MONTH = 1
TODAY_DATE = datetime.datetime.now()
PAYMENT_OPTIONS = ["FULL", "MONTHLY", "DOWN PAYMENT"]

# Functions


def printClaims():
    """
    Prints the claims information.

    If there are no claims, it prints "No claims.".
    Otherwise, it prints the claim number, claim date, and claim amount for each claim.
    """
    if claims == "NONE":
        print("No claims.")
        return
    else:
        print(f"Claim #  Claim Date        Amount")
        print(f"---------------------------------")
        for i in range(len(claimDates)):
            print(
                f"  {i+1}.     {formater.dateMedium(claimDates[i])}    {formater.formatMoney(claimAmounts[i]):>9s}")


def printRecipt():
    """
    Prints the receipt for the insurance policy.

    This function prints the details of the insurance policy, including the customer's name, address, phone number,
    policy number, payment option, number of cars, coverage details, insurance cost, HST, total cost, and any additional
    information based on the payment option chosen.
    """

    fullName = firstName + " " + lastName
    bottomAddress = city + ", " + province + " " + postalCode

    print(f"----------------------------------------")
    print(f"       One Stop Insurance Company       ")
    print(f"----------------------------------------")
    print(f" Name:{fullName:>33s}")
    print(f" Address:{address:>30s}")
    print(f" {bottomAddress:>38s}")
    print(f" Phone Number:{formater.formatPhone(phoneNumber):>25s}")
    print(f"----------------------------------------")
    print(f" Policy Number:{POLICY_NUMBER:>24d}")
    print(f" Payment Option:{paymentOption.title():>23s}")
    print(f" Number of cars:{numCars:>23d}")
    print(f"----------------------------------------")
    print(f" First Car Coverage:{formater.formatMoney(BASIC_PREMIUM):>19s}")
    print(f" Extra Car Coverage:{formater.formatMoney(extraCarCost):>19s}")
    if extraLiability == "Y":
        print(
            f" Extra Liability Coverage:{formater.formatMoney(extraLiabCost):>13s}")
    if glassCoverage == "Y":
        print(f" Glass Coverage:{formater.formatMoney(glassCovCost):>23s}")
    if loanerCar == "Y":
        print(
            f" Loaner Car Coverage:{formater.formatMoney(loanerCarCost):>18s}")
    print(f"----------------------------------------")
    print(f" Insurance Cost:{formater.formatMoney(insuraceCost):>23s}")
    print(f" HST:{formater.formatMoney(hstCost):>34s}")
    print(f" Total Cost:{formater.formatMoney(totalCost):>27s}")
    print(f"----------------------------------------")

    if paymentOption == PAYMENT_OPTIONS[0]:
        print(f"       Thanks for paying in full!       ")
        print(f"----------------------------------------")
        print(f"      Thank you for your business!      ")
    else:
        print(f" Processing Fee:{formater.formatMoney(PROCESSING_FEE):>23s}")
        if paymentOption == PAYMENT_OPTIONS[2]:
            print(f" Down Payment:{formater.formatMoney(downPayment):>25s}")
        print(f" Financed Amount:{formater.formatMoney(financingAmount):>22s}")
        print(f" Number of Payments:                  8")
        print(f"----------------------------------------")
        print(f" Payment Amount:{formater.formatMoney(payments):>23s}")
        print(
            f" Date of first Payment:{formater.dateMedium(firstPaymentDate):>14s}")
        print(f"----------------------------------------")
        print(f"      Thank you for your business!      ")


# Main
while True:
    """
    This is the Gathering of the generic infomration for the insurance policy.

    All of these inputs are validated using the Gar_Validate.py library.
    """
    while True:
        firstName = input("Please enter your first name: ")
        if validator.validateString(firstName):
            break

    while True:
        lastName = input("Please enter your last name: ")
        if validator.validateString(lastName):
            break

    while True:
        address = input("Please enter your address: ")
        if validator.validateString(address):
            break

    while True:
        city = input("Please enter your city: ")
        if validator.validateString(city):
            break

    while True:
        province = input("Please enter your province (XX): ")
        if validator.validateProv(province):
            break

    while True:
        postalCode = input("Please enter your postal code: ")
        if validator.validatePostalCode(postalCode):
            break

    while True:
        phoneNumber = input("Please enter your phone number(9999999999): ")
        if validator.validateString(phoneNumber):
            break

    while True:
        numCars = input("Please enter the number of cars you own: ")
        if validator.validateInt(numCars):
            numCars = int(numCars)
            break
    """
    This is the gathering of the yes and no questions for the insurance policy.
    Each of these inputs taken as a string and 
    then sets the cost to 0 or the cost of the coverage.

    These inputs are validated using the Gar_Validate.py library.
    """
    while True:
        extraLiability = input(
            "Would you like extra liability coverage? (Y/N): "
        ).upper()
        if validator.validateYesNo(extraLiability):
            if extraLiability == "Y":
                extraLiabCost = EXTRA_LIABILITY_COST
            elif extraLiability == "N":
                extraLiabCost = 0
            break

    while True:
        glassCoverage = input("Would you like glass coverage? (Y/N): ").upper()
        if validator.validateYesNo(glassCoverage):
            if glassCoverage == "Y":
                glassCovCost = GLASS_COVERAGE_COST
            elif glassCoverage == "N":
                glassCovCost = 0
            break

    while True:
        loanerCar = input(
            "Would you like loaner car coverage? (Y/N): ").upper()
        if validator.validateYesNo(loanerCar):
            if loanerCar == "Y":
                loanerCarCost = LOANER_CAR_COST
            elif loanerCar == "N":
                loanerCarCost = 0
            break

    """
    This is the gathering of the payment option for the insurance policy.
    Each of these inputs taken as a string and compared to list of possible
    payment options. If the payment option is down payment, then the down
    payment is gathered.

    The Down Payment is validated using the Gar_Validate.py library.
    """
    while True:
        paymentOption = input(
            "Please enter your payment option (Full, Monthly, Down Payment): "
        ).upper()

        if paymentOption == "":
            print("Please enter a valid input.")
        elif paymentOption in PAYMENT_OPTIONS[2]:
            while True:
                downPayment = input("Please enter your down payment: ")
                if validator.validatefloat(downPayment):
                    downPayment = float(downPayment)
                    break
            break
        elif paymentOption in PAYMENT_OPTIONS:
            break
        else:
            print("Please enter a valid input.")

    """
    This is the gathering of the previous claims for the insurance policy. 
    Each of these inputs taken as a string and then split into a list of
    touple pairs. The date is then converted into a datetime object and the
    amount is converted into a float. Each of these values are validated
    using the Gar_Validate.py library. Then the pairs are split into two
    lists, one for the dates and one for the amounts.

    If there is no claims, then the loop is broken.
    """
    claimDates = []
    claimAmounts = []
    while True:
        print("Enter your claims in format separated by commas.")
        print("Example: 1999-01-01 1000, 1999-01-02 200, .... ")
        print("If you have no claims, enter None.")
        claims = input("Please enter previous claims: ").upper()
        if claims == "":
            print("Please enter a valid input.")
        elif claims == "NONE":
            break
        claimPairs = claims.split(", ")
        for claims in claimPairs:
            temp = claims.split(" ")
            claimDates.append(datetime.datetime.strptime(temp[0], "%Y-%m-%d"))
            claimAmounts.append(temp[1])
        valid = True
        for i in range(len(claimDates)):
            if not validator.validateShortDate(claimDates[i]) or not validator.validatefloat(claimAmounts[i]):
                valid = False
                temp.clear()
                claimAmounts.clear()
                claimDates.clear()
        if valid:
            break

    """
    These are the calculations for the insurance policy.
    """
    extraCarCost = (numCars * BASIC_PREMIUM) * DISCOUNT_ADD_CAR
    extaCost = extraLiabCost + glassCovCost + loanerCarCost
    insuraceCost = BASIC_PREMIUM + extraCarCost + extaCost
    hstCost = insuraceCost * HST_RATE
    totalCost = insuraceCost + hstCost

    """
    This is calculations for the financing of the insurance policy.
    The calculations are based on the payment option.
    """
    financingAmount = 0
    if paymentOption == PAYMENT_OPTIONS[1]:
        financingAmount = totalCost + PROCESSING_FEE
    elif paymentOption == PAYMENT_OPTIONS[2]:
        financingAmount = totalCost - downPayment + PROCESSING_FEE
    payments = financingAmount / 8

    """
    This is the calculations for the next payment date.
    """
    nextMonth = TODAY_DATE.month + 1
    firstPaymentDate = datetime.datetime(
        TODAY_DATE.year, nextMonth, FIRST_OF_MONTH)

    """
    This is the printing of the recipt and claims.
    These functions are above
    """
    printRecipt()
    print(f"")
    printClaims()

    """
    This is the exit function for the program.

    The exit function is in the Gar_Utility.py library.
    """
    if utility.exit("Thanks for using One Stop Insurance!"):
        break
