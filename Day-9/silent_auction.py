from replit import clear
from art import logo
import  os
auction_bids = { }
go = 'yes'
print(logo)
print("Welcome to the secret auction Program.")

while go == 'yes':
    name = input("What is your name? \n")
    bid = float(input("Enter your bid amount \n$"))
    auction_bids[name] = bid
    go = input("Are there any new bidders?\n").lower()
    # os.system('cls' if os.name == 'nt' else 'clear')
    clear()

max_bid = 0
winning_bidder = None
for bidder in auction_bids:
    if auction_bids[bidder] > max_bid:
        max_bid = auction_bids[bidder]
        winning_bidder = bidder
print(f"Winning bidder is {winning_bidder} with bid price ${max_bid}")
