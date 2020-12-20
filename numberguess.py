from random import *
print('guess this number')
number=random(1,9)
chances=5

while chances>=5:
    guess=input('guess the number i am thinking of:')
    if guess==number:
        print('you win what a pro')
    break
if chances==0:
    print('you lose noob')