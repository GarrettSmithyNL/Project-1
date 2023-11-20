# This program is going calculate recipt for One Stop Insurance Company
# Garrett Smith
# Nov 29, 2023

# Imports
from Gar_Util import Gar_Validate as validator
from Gar_Util import Gar_Format as formater
from Gar_Util import Gar_Utility as utility
import datetime

# Constants
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
DISCOUNT_ADD_CAR = 0.25
EXTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_CAR_COST = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99
FIRST_OF_MONTH = 1
TODAY_DATE = datetime.datetime.now()
PAYMENT_OPTIONS = ["FULL", "MONTHLY", "DOWN PAYMENT", "DOWNPAYMENT"]

# Functions


def printClaims(claimDates, claimAmounts):
    print(f"Claim #  Claim Date        Amount")
    print(f"---------------------------------")
    for i in range(len(claimDates)):
        print(
            f"  {i+1}.     {formater.dateMedium(claimDates[i])}    {formater.formatMoney(claimAmounts[i]):>9s}")


# Main
while True:
    # Get user input
    # while True:
    #     firstName = input("Please enter your first name: ")
    #     if validator.validateString(firstName):
    #         break
    firstName = "Garrett"

    # while True:
    #     lastName = input("Please enter your last name: ")
    #     if validator.validateString(lastName):
    #         break
    lastName = "Smith"

    # while True:
    #     address = input("Please enter your address: ")
    #     if validator.validateString(address):
    #         break
    address = "123 Fake Street"

    # while True:
    #     city = input("Please enter your city: ")
    #     if validator.validateString(city):
    #         break
    city = "Toronto"

    # while True:
    #     province = input("Please enter your province (XX): ")
    #     if validator.validateProv(province):
    #         break
    province = "ON"

    # while True:
    #     postalCode = input("Please enter your postal code: ")
    #     if validator.validatePostalCode(postalCode):
    #         break
    postalCode = "M1M1M1"

    # while True:
    #     phoneNumber = input("Please enter your phone number(9999999999): ")
    #     if validator.validateString(phoneNumber):
    #         break
    phoneNumber = "4161234567"

    # while True:
    #     numCars = input("Please enter the number of cars you own: ")
    #     if validator.validateInt(numCars):
    #         numCars = int(numCars)
    #         break
    numCars = 2

    while True:
        # extraLiability = input(
        #     "Would you like extra liability coverage? (Y/N): "
        # ).upper()
        extraLiability = "Y"
        if extraLiability == "":
            print("Please enter a valid input.")
        elif extraLiability == "Y":
            extraLiabCost = EXTRA_LIABILITY_COST
            break
        elif extraLiability == "N":
            extraLiabCost = 0
            break
        else:
            print("Please enter a valid input.")

    while True:
        # glassCoverage = input("Would you like glass coverage? (Y/N): ").upper()
        glassCoverage = "Y"
        if glassCoverage == "":
            print("Please enter a valid input.")
        elif glassCoverage == "Y":
            glassCovCost = GLASS_COVERAGE_COST
            break
        elif glassCoverage == "N":
            glassCovCost = 0
            break
        else:
            print("Please enter a valid input.")

    while True:
        # loanerCar = input(
        #     "Would you like loaner car coverage? (Y/N): ").upper()
        loanerCar = "Y"
        if loanerCar == "":
            print("Please enter a valid input.")
        elif loanerCar == "Y":
            loanerCarCost = LOANER_CAR_COST
            break
        elif loanerCar == "N":
            loanerCarCost = 0
            break
        else:
            print("Please enter a valid input.")

    while True:
        # paymentOption = input(
        #     "Please enter your payment option (Full, Monthly, Down Payment): "
        # ).upper()
        paymentOption = "DOWN PAYMENT"

        if paymentOption == "":
            print("Please enter a valid input.")
        elif paymentOption in PAYMENT_OPTIONS[2:4]:
            while True:
                # downPayment = input("Please enter your down payment: ")
                downPayment = 200.00
                if validator.validatefloat(downPayment):
                    downPayment = float(downPayment)
                    break
            break
        elif paymentOption in PAYMENT_OPTIONS:
            break
        else:
            print("Please enter a valid input.")

    claimDates = []
    claimAmounts = []
    while True:
        # print("Enter your claims in format separated by commas.")
        # print("Example: 1999-01-01 1000, 1999-01-02 200, .... ")
        # claims = input("Please enter previous claims: ")
        claims = "1999-01-01 1000, 1999-01-02 200, 1999-01-03 200, 1999-01-04 250"
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

    # Calculate
    extraCarCost = (numCars * BASIC_PREMIUM) * DISCOUNT_ADD_CAR
    extaCost = extraLiabCost + glassCovCost + loanerCarCost
    insuraceCost = BASIC_PREMIUM + extraCarCost + extaCost
    hstCost = insuraceCost * HST_RATE
    totalCost = insuraceCost + hstCost

    # payments
    if paymentOption == PAYMENT_OPTIONS[1]:
        payments = (totalCost + PROCESSING_FEE) / 12
    elif paymentOption == PAYMENT_OPTIONS[2:3]:
        payments = (totalCost - downPayment + PROCESSING_FEE) / 12

    # Dates
    nextMonth = TODAY_DATE.month + 1
    firstPaymentDate = datetime.datetime(
        TODAY_DATE.year, nextMonth, FIRST_OF_MONTH)

    # Output

    printClaims(claimDates, claimAmounts)

    if utility.exit("Thanks for using One Stop Insurance!"):
        break
