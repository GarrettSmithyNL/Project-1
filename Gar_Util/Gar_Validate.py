# This is a library that is for validation
# Garrett Smith
# Nov 9 2023

import datetime

PROV_LIST = ["ON", "QC", "NS", "NB", "MB", "BC",
             "PE", "SK", "AB", "NL", "NT", "YT", "NU"]


def validateInt(value,  min=None, max=None):
    try:
        number = int(value)
    except ValueError or TypeError:
        print("Value not an int.")
        return False
    else:
        if min != None and number < min:
            print("Value under min.")
            return False
        if max != None and number > max:
            print("Value over max.")
            return False
        else:
            return True


def validatefloat(value,  min=None, max=None):
    try:
        number = float(value)
    except ValueError or TypeError:
        print("Value not a float.")
        return False
    else:
        if min != None and number < min:
            print("Value under min.")
            return False
        if max != None and number > max:
            print("Value over max.")
            return False

        return True


def validateString(value, minLen=None, maxLen=None):
    if value == "":
        print("Value is empty.")
        return False
    elif maxLen != None and len(value) > maxLen:
        print("Value is too long.")
        return False
    elif minLen != None and len(value) < minLen:
        print("Value is too short.")
        return False
    else:
        return True


def validatePostalCode(value):
    if len(value) != 6:
        print("Value is not the correct length(6).")
        return False
    if not value[0].isdigit() or not value[2].isdigit() or not value[4].isdigit():
        print("Value does not follow X0X0X0.")
        return False
    if not value[1].isalpha() or not value[3].isalpha() or not value[5].isalpha():
        print("Value does not follow X0X0X0.")
        return False
    else:
        return True


def validateShortDate(value):  # YYYY-MM-DD
    if value == "":
        print("Value is empty.")
        return False
    else:
        try:
            datetime.datetime.strftime(value, "%Y-%m-%d")
        except ValueError:
            print("Value is not a valid date.")
            return False
        else:
            return True


def validateProv(value):
    if value.upper() in PROV_LIST:
        return True
    else:
        print("Value is not a valid province.")
        return False
