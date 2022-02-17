#TO FIND THE PROBABILITY OF GETTING A WHITE PEN BY TAKING THE VALUE OF THE NUMBER OF BLACK AND WHITE PEN FROM USER
print("enter the number of black pen")
black_pen=int(input())
print('enter the number of white pen')
white_pen=int(input())
probability=white_pen/(white_pen+black_pen)
print(probability)