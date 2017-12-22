# Developer : Hamdy Abou El Anein

import datetime
from datetime import date
from easygui import *
import sys

allahakbar = "./images/AllahAkbar.gif"
ramadanpic = "./images/ramadan.gif"


def year2018():
    d1 = date(int(2018), int(5), int(16))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2018 ramadan will be the 16 May 2018")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2019():
    d1 = date(int(2019), int(5), int(6))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2019 ramadan will be the 6 May 2019")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2020():
    d1 = date(int(2020), int(4), int(24))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2020 ramadan will be the 24 April 2020")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2021():
    d1 = date(int(2021), int(4), int(13))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2021 ramadan will be the 13 April 2021")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2022():
    d1 = date(int(2022), int(4), int(3))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2022 ramadan will be the 3 April 2022")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2023():
    d1 = date(int(2023), int(3), int(23))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2023 ramadan will be the 23 March 2023")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2024():
    d1 = date(int(2024), int(3), int(11))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2024 ramadan will be the 11 March 2024")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2025():
    d1 = date(int(2025), int(3), int(1))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2025 ramadan will be the 1 March 2025")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2026():
    d1 = date(int(2026), int(2), int(18))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2026 ramadan will be the 18 February 2026")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2027():
    d1 = date(int(2027), int(2), int(8))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2027 ramadan will be the 8 February 2027")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2028():
    d1 = date(int(2028), int(1), int(28))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2028 ramadan will be the 28 January 2028")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2029():
    d1 = date(int(2029), int(1), int(16))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2029 ramadan will be the 16 January 2029")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2030():
    d1 = date(int(2030), int(1), int(6))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2030 ramadan will be the 6 January 2030")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2031():
    d1 = date(int(2030), int(12), int(26))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2031 ramadan will be the 26 December 2030")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2032():
    d1 = date(int(2031), int(12), int(15))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2032 ramadan will be the 15 December 2031")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)


def year2033():
    d1 = date(int(2032), int(12), int(4))
    now = datetime.datetime.now()
    d0 = date(now.year, now.month, now.day)
    delta = d1 - d0

    image = ramadanpic
    msg = "You have to wait "+str(delta.days)+str(" days \n\n\nthe 2033 ramadan will be the 4 December 2032")
    choices = ["Select another year ?","Quit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Select another year ?":
        year()
    elif reply == "./images/ramadan.gif":
        year()
    else:
        sys.exit(0)




def year():
    msg = "Select the Ramadan year to calculate how many days from now until this date"
    title = "Select the Ramadan year"
    choices = ["2018", "2019", "2020", "2021","2022","2023","2024","2025","2026","2027","2028","2029","2030","2031","2032","2033"]
    choice = choicebox(msg, title, choices)
    if choice == "2018":
        year2018()
    elif choice == "2019":
        year2019()
    elif choice == "2020":
        year2020()
    elif choice == "2021":
        year2021()
    elif choice == "2022":
        year2022()
    elif choice == "2023":
        year2023()
    elif choice == "2024":
        year2024()
    elif choice == "2025":
        year2025()
    elif choice == "2026":
        year2026()
    elif choice == "2027":
        year2027()
    elif choice == "2028":
        year2028()
    elif choice == "2029":
        year2029()
    elif choice == "2030":
        year2030()
    elif choice == "2031":
        year2031()
    elif choice == "2032":
        year2032()
    elif choice == "2033":
        year2033()
    else:
        sys.exit(0)



def begin():
    image = allahakbar
    msg = "                 Islamic How many days to the Ramadan Calculator\n\n\nThis software calculate how many days you have to wait until the ramadan you select\n\n\nThis software work from the ramadan of 2018 to the ramadan of 2033"
    choices = ["Begin"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Begin":
        year()
    elif reply == "./images/AllahAkbar.gif":
        year()
    else:
        sys.exit(0)


begin()


