import random


low = 1
high = 100
guesses = 0
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# number = random.random() is for floating numbers
#number = random.randint(low, high) # for integers
random.shuffle(cards)
#option = random.choice(options)
print(cards)
