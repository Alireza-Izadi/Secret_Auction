from art import logo
import os
bidders = []
def blind_auction(bider_name, bider_price):
    bidder = {}
    bidder["name"] = bider_name
    bidder["price"] = bider_price
    bidders.append(bidder)

bidding_finished = False

while not bidding_finished:
    print(logo)
    name = input("What is Your Name?: ").lower()
    bid = int(input("What is your bid price? $"))
    blind_auction(name, bid)
    should_continue = input("Is ther any other bidders? Type 'yes' or 'no'").lower()
    if should_continue == "no":
        bidding_finished = True
        sorted_bidders = sorted(bidders, key=lambda x:x["price"])
        winner_index = len(sorted_bidders) - 1
        os.system('cls')
        print("**********************************************************************")
        print(f"The Highest Bidder is {sorted_bidders[winner_index]['name'].capitalize()} with a bid of ${sorted_bidders[winner_index]['price']}")
        print("**********************************************************************")
    elif should_continue == "yes":
        os.system('cls')
    else:
        should_continue = input("Is ther any other bidders? Type 'yes' or 'no'").lower()
        os.system('cls')