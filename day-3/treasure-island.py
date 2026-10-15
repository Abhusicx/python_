print("WELCOME TO TREASURE ISLAND")
direction=input("choose the direction? left and right? ")

if direction=="right":
    print("Game over")
else :
    print("swim or wait?")
    decision=input("what would you choose ? swim or wait? ")
    if decision == "swim":
        print("GAme over")
    else:
        print("door!")
        door=input("which door you'll choose? red, yello, blue")
        if door == "yello":
            print("you win")
        else : 
            print("game over")
