def show_homepage():
    print("           === DONATE HOMEPAGE ===           ")
    print("---------------------------------------------")
    print("|  1.    LOGIN    |  2.   REGISTER          |")
    print("---------------------------------------------")
    print("|  3.    DONATE   |  4.   SHOW DONATIONS    |")
    print("---------------------------------------------")
    print("|              5. EXIT                      |")
    print("---------------------------------------------")


def donate(username):
    donate_amt = float(input('Enter amount to donate: '))
    donation_string = username.capitalize() + ' donated $' + str(donate_amt)
    print('Thank you for your donation!')
    return donation_string


def show_donations(donations):
    print("\n--------- All Donations ---------")
    if len(donations) == 0:
        print("Currently, there are no donations.\n")
    else:
        for donor in donations:
            print(donor)
