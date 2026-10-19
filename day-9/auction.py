print("Hi, welcome to the auction")

def find_max_value_in_dictionary(dictionary):
    winner = ""
    highest_amount = 0
    for bidder in dictionary:
        bid_amount = dictionary[bidder]
        if(bid_amount > highest_amount):
            highest_amount = bid_amount
            winner = bidder 

    print(f"the {winner} takes it all in {highest_amount}")

auction = {} 
continue_bid = True
while continue_bid : 
    name = input("what is your name? ")
    amount = int(input("what is your amount? "))
    auction[name] = amount
    should_continue = input("do you want to continue? type 'yes' or 'no'\n")
    if should_continue == "no":
        find_max_value_in_dictionary(auction)
