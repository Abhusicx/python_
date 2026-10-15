scores=[96,64,43,98,12,24,62,19,23,67]

highest_score=0
for score in scores:
    if score>highest_score:
        highest_score=score

print(f"The highest score in the list is: {highest_score}")