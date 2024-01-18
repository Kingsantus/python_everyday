"""Secret Auction project"""
print("Welcome to the scret auction program.")
auction_dict = {}

def find_highest_bidder(bidding_record):
    highest_bidder = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")

auction_close = False
while not auction_close:
    name = input('What is your name?: ')
    bid_price = int(input("What is your bid?: $"))
    auction_dict[name] = bid_price
    should_close = input("Are there any other bidders? 'yes' or 'no'.\n").lower()
    if should_close == 'no':
        auction_close = True
        find_highest_bidder(auction_dict)
    else:
        auction_close = False