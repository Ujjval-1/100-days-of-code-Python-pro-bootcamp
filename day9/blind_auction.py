from art import logo
print(logo)

def auction():
    bid_dict={}

    other_bidders = True
    while other_bidders:
        name=input("Enter your name:\n")
        bid_amount=float(input("Enter your bid amount:\n$"))
        bid_dict[name]=bid_amount

        other_bids=input("Are there other bidders? Type 'yes' or 'no'").lower()
        if other_bids=='yes':
            print('\n'*100)
        elif other_bids=="no":
            other_bidders=False
        else:
            print("Invalid input")
            other_bidders=False

    maximum_bid=0
    winner=""
    for name in bid_dict:
        if bid_dict[name]>maximum_bid:
            maximum_bid=bid_dict[name]
            winner=name
    print(f"Maximum bid is {maximum_bid} by {winner}")
auction()