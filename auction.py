import os

print('Welcome to the secret auction program.')

bidders = {}

while True:
    user_name = input('What is your name?\n')
    user_bid = int(input('What is your bid?\n$'))
    bidders[user_name] = user_bid

    other_bidder = input(
        "Are there other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidder == 'yes':
        os.system('clear')
    elif other_bidder == 'no':
        break
    else:
        print('Invalid selection\n')
print(bidders)
