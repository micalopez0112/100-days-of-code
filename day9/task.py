
people_bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

cont = True
while cont:
    print("welcome to the ")
    name = input("what is your name?: ")
    bid = int(input("what is your bid?: "))
    people_bids[name] = bid
    more = input("are there any other bidders? Type 'yes' or 'no': ")
    if more == "no":
        cont = False
        find_highest_bidder(people_bids)
    


