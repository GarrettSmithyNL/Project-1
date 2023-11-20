# This is a library that is for formating
# Garrett Smith
# Nov 9 2023

import datetime

INT_FORMATTING = "{:,d}"
DATE_SHORT_FORMATTING = "%d/%m/%y"
DATE_MEDIUM_FORMATTING = "%Y-%b-%d"
DATE_LONG_FORMATTING = "%d %B %Y"
DATE_SHORT_WEEKDAY = "%a, %d-%b-%y"
DATE_LONG_WEEKDAY = "%A, %B %d %Y"


def formatFloat(num, roundLen=2):
    floatTemp = "{:,." + str(roundLen) + "f}"
    return floatTemp.format(float(num))


def formatInt(num):
    return INT_FORMATTING.format(num)


def formatMoney(amount):
    return "$" + formatFloat(amount)


def formatPercent(num, roundLen=2):
    return formatFloat(num, roundLen) + "%"


def dateShort(pDate):
    return pDate.strftime(DATE_SHORT_FORMATTING)


def dateMedium(pDate):
    return pDate.strftime(DATE_MEDIUM_FORMATTING)


def dateLong(pDate):
    return pDate.strftime(DATE_LONG_FORMATTING)


def dateShortWeekDay(pDate):
    return pDate.strftime(DATE_SHORT_WEEKDAY)


def dateLongWeekDay(pDate):
    return pDate.strftime(DATE_LONG_WEEKDAY)
